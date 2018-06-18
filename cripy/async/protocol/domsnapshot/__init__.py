from typing import Any, List, Optional, Union
from cripy.async.protocol.domsnapshot import types as Types


class DOMSnapshot(object):
    """
    This domain facilitates obtaining document snapshots with DOM, layout, and style information.
    """

    dependencies = ["CSS", "DOM", "DOMDebugger", "Page"]

    def __init__(self, chrome):
        self.chrome = chrome

    async def disable(self) -> Optional[dict]:
        mayberes = await self.chrome.send("DOMSnapshot.disable")
        return mayberes

    async def enable(self) -> Optional[dict]:
        mayberes = await self.chrome.send("DOMSnapshot.enable")
        return mayberes

    async def getSnapshot(
        self,
        computedStyleWhitelist: List[str],
        includeEventListeners: Optional[bool] = None,
        includePaintOrder: Optional[bool] = None,
        includeUserAgentShadowTree: Optional[bool] = None,
    ) -> Optional[dict]:
        """
        :param computedStyleWhitelist: Whitelist of computed styles to return.
        :type computedStyleWhitelist: List[str]
        :param includeEventListeners: Whether or not to retrieve details of DOM listeners (default false).
        :type includeEventListeners: Optional[bool]
        :param includePaintOrder: Whether to determine and include the paint order index of LayoutTreeNodes (default false).
        :type includePaintOrder: Optional[bool]
        :param includeUserAgentShadowTree: Whether to include UA shadow tree in the snapshot (default false).
        :type includeUserAgentShadowTree: Optional[bool]
        """
        msg_dict = dict()
        if computedStyleWhitelist is not None:
            msg_dict["computedStyleWhitelist"] = computedStyleWhitelist
        if includeEventListeners is not None:
            msg_dict["includeEventListeners"] = includeEventListeners
        if includePaintOrder is not None:
            msg_dict["includePaintOrder"] = includePaintOrder
        if includeUserAgentShadowTree is not None:
            msg_dict["includeUserAgentShadowTree"] = includeUserAgentShadowTree
        mayberes = await self.chrome.send("DOMSnapshot.getSnapshot", msg_dict)
        res = await mayberes
        res["domNodes"] = Types.DOMNode.safe_create_from_list(res["domNodes"])
        res["layoutTreeNodes"] = Types.LayoutTreeNode.safe_create_from_list(
            res["layoutTreeNodes"]
        )
        res["computedStyles"] = Types.ComputedStyle.safe_create_from_list(
            res["computedStyles"]
        )
        return res

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return None
