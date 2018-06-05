"""Coverage module."""

import asyncio
from functools import cmp_to_key
from typing import Any, Dict, List

from cripy.chrome import helper
from cripy.chrome.connection import CDPSession
from cripy.chrome.errors import PageError
from cripy.chrome.util import merge_dict


class Coverage(object):

    def __init__(self, client: CDPSession) -> None:
        self._jsCoverage = JSCoverage(client)
        self._cssCoverage = CSSCoverage(client)

    async def startJSCoverage(self, options: Dict = None, **kwargs: Any) -> None:
        options = merge_dict(options, kwargs)
        await self._jsCoverage.start(options)

    async def stopJSCoverage(self) -> List:
        return await self._jsCoverage.stop()

    async def startCSSCoverage(self, options: Dict = None, **kwargs: Any) -> None:
        options = merge_dict(options, kwargs)
        await self._cssCoverage.start(options)

    async def stopCSSCoverage(self) -> List:
        return await self._cssCoverage.stop()


class JSCoverage(object):

    def __init__(self, client: CDPSession) -> None:
        self._client = client
        self._enabled = False
        self._scriptURLs: Dict = dict()
        self._scriptSources: Dict = dict()
        self._eventListeners: List = list()
        self._resetOnNavigation = False

    async def start(self, options: Dict = None, **kwargs: Any) -> None:
        options = merge_dict(options, kwargs)
        if self._enabled:
            raise PageError("JSCoverage is always enabled.")
        self._resetOnNavigation = (
            True
            if "resetOnNavigation" not in options
            else bool(options["resetOnNavigation"])
        )
        self._enabled = True
        self._scriptURLs.clear()
        self._scriptSources.clear()
        self._eventListeners = [
            helper.addEventListener(
                self._client,
                "Debugger.scriptParsed",
                lambda e: asyncio.ensure_future(self._onScriptParsed(e)),
            ),
            helper.addEventListener(
                self._client,
                "Runtime.executionContextsCleared",
                self._onExecutionContextsCleared,
            ),
        ]
        await self._client.send("Profiler.enable")
        await self._client.send(
            "Profiler.startPreciseCoverage", {"callCount": False, "detailed": True}
        )
        await self._client.send("Debugger.enable")
        await self._client.send("Debugger.setSkipAllPauses", {"skip": True})

    def _onExecutionContextsCleared(self, event: Dict) -> None:
        if not self._resetOnNavigation:
            return
        self._scriptURLs.clear()
        self._scriptSources.clear()

    async def _onScriptParsed(self, event: Dict) -> None:
        if "url" not in event:
            return
        scriptId = event.get("scriptId")
        url = event.get("url")
        try:
            response = await self._client.send(
                "Debugger.getScriptSource", {"scriptId": scriptId}
            )
            self._scriptURLs[scriptId] = url
            self._scriptSources[scriptId] = response.get("scriptSource")
        except Exception:
            # This might happen if the page has already navigated away.
            pass

    async def stop(self) -> List:
        """Stop coverage measurement and return results."""
        if not self._enabled:
            raise PageError("JSCoverage is not enabled.")
        self._enabled = False

        result = await self._client.send("Profiler.takePreciseCoverage")
        await self._client.send("Profiler.stopPreciseCoverage")
        await self._client.send("Profiler.disable")
        await self._client.send("Debugger.disable")
        helper.removeEventListeners(self._eventListeners)

        coverage: List = []
        for entry in result.get("result", []):
            url = self._scriptURLs.get(entry.get("scriptId"))
            text = self._scriptSources.get(entry.get("scriptId"))
            if text is None or url is None:
                continue
            flattenRanges: List = []
            for func in entry.get("functions", []):
                flattenRanges.extend(func.get("ranges", []))
            ranges = convertToDisjointRanges(flattenRanges)
            coverage.append({"url": url, "ranges": ranges, "text": text})
        return coverage


class CSSCoverage(object):
    """CSS Coverage class."""

    def __init__(self, client: CDPSession) -> None:
        self._client = client
        self._enabled = False
        self._stylesheetURLs: Dict = dict()
        self._stylesheetSources: Dict = dict()
        self._eventListeners: List = []
        self._resetOnNavigation = False

    async def start(self, options: Dict = None, **kwargs: Any) -> None:
        """Start coverage measurement."""
        options = merge_dict(options, kwargs)
        if self._enabled:
            raise PageError("CSSCoverage is already enabled.")
        self._resetOnNavigation = (
            True
            if "resetOnNavigation" not in options
            else bool(options["resetOnNavigation"])
        )
        self._enabled = True
        self._stylesheetURLs.clear()
        self._stylesheetSources.clear()
        self._eventListeners = [
            helper.addEventListener(
                self._client,
                "CSS.styleSheetAdded",
                lambda e: asyncio.ensure_future(self._onStyleSheet(e)),
            ),
            helper.addEventListener(
                self._client,
                "Runtime.executionContextsCleared",
                self._onExecutionContextsCleared,
            ),
        ]
        await self._client.send("DOM.enable")
        await self._client.send("CSS.enable")
        await self._client.send("CSS.startRuleUsageTracking")

    def _onExecutionContextsCleared(self, event: Dict) -> None:
        if not self._resetOnNavigation:
            return
        self._stylesheetURLs.clear()
        self._stylesheetSources.clear()

    async def _onStyleSheet(self, event: Dict) -> None:
        header = event.get("header", {})
        # Ignore anonymous scripts
        if "sourceURL" not in header:
            return
        try:
            response = await self._client.send(
                "CSS.getStyleSheetText", {"styleSheetId": header["styleSheetId"]}
            )
            self._stylesheetURLs[header["styleSheetId"]] = header["sourceURL"]
            self._stylesheetSources[header["styleSheetId"]] = response["text"]
        except Exception:
            # This might happen if the page has already navigated away.
            pass

    async def stop(self) -> List:
        """Stop coverage measurement and return results."""
        if not self._enabled:
            raise PageError("CSSCoverage is not enabled.")
        self._enabled = False
        result = await self._client.send("CSS.stopRuleUsageTracking")
        await self._client.send("CSS.disable")
        await self._client.send("DOM.disable")
        helper.removeEventListeners(self._eventListeners)

        # aggregate by styleSheetId
        styleSheetIdToCoverage: Dict = {}
        for entry in result["ruleUsage"]:
            ranges = styleSheetIdToCoverage.get(entry["styleSheetId"])
            if not ranges:
                ranges = []
                styleSheetIdToCoverage[entry["styleSheetId"]] = ranges
            ranges.append(
                {
                    "startOffset": entry["startOffset"],
                    "endOffset": entry["endOffset"],
                    "count": 1 if entry["used"] else 0,
                }
            )

        coverage = []
        for styleSheetId in self._stylesheetURLs:
            url = self._stylesheetURLs.get(styleSheetId)
            text = self._stylesheetSources.get(styleSheetId)
            ranges = convertToDisjointRanges(
                styleSheetIdToCoverage.get(styleSheetId, [])
            )
            coverage.append({"url": url, "ranges": ranges, "text": text})

        return coverage


def convertToDisjointRanges(nestedRanges: List[Any]) -> List[Any]:  # noqa: C901
    """Convert ranges."""
    points: List = []
    for range in nestedRanges:
        points.append({"offset": range["startOffset"], "type": 0, "range": range})
        points.append({"offset": range["endOffset"], "type": 1, "range": range})

    # Sort points to form a valid parenthesis sequence.
    def _sort_func(a: Dict, b: Dict) -> int:
        # Sort with increasing offsets.
        if a["offset"] != b["offset"]:
            return a["offset"] - b["offset"]
        # All "end" points should go before "start" points.
        if a["type"] != b["type"]:
            return b["type"] - a["type"]
        aLength = a["range"]["endOffset"] - a["range"]["startOffset"]
        bLength = b["range"]["endOffset"] - b["range"]["startOffset"]
        # For two "start" points, the one with longer range goes first.
        if a["type"] == 0:
            return bLength - aLength
        # For two "end" points, the one with shorter range goes first.
        return aLength - bLength

    points.sort(key=cmp_to_key(_sort_func))

    hitCountStack: List[int] = []
    results: List[Dict] = []
    lastOffset = 0
    # Run scanning line to intersect all ranges.
    for point in points:
        if (
            hitCountStack
            and lastOffset < point["offset"]
            and hitCountStack[len(hitCountStack) - 1] > 0
        ):
            lastResult = results[-1] if results else None
            if lastResult and lastResult["end"] == lastOffset:
                lastResult["end"] = point["offset"]
            else:
                results.append({"start": lastOffset, "end": point["offset"]})
        lastOffset = point["offset"]
        if point["type"] == 0:
            hitCountStack.append(point["range"]["count"])
        else:
            hitCountStack.pop()
    # Filter out empty ranges.
    return [range for range in results if range["end"] - range["start"] > 1]
