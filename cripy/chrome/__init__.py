
import asyncio
from subprocess import Popen
from types import SimpleNamespace
from typing import Any, Awaitable, Callable, Dict, List, Optional, Union

from pyee import EventEmitter

from cripy.protocol.target.events import (
    EVENT_NS as TargetNS,
    TargetCreatedEvent,
    TargetDestroyedEvent,
    TargetInfoChangedEvent,
)
from cripy.protocol.target.types import TargetInfo
from cripy.chrome.connection import Connection, CDPSession
from cripy.chrome.errors import BrowserError
from cripy.chrome.page import Page


class Chrome(EventEmitter):
    Events = SimpleNamespace(
        TargetCreated="targetcreated",
        TargetDestroyed="targetdestroyed",
        TargetChanged="targetchanged",
        Disconnected="disconnected",
    )

    def __init__(
        self,
        connection: Connection,
        contextIds: List[str],
        ignoreHTTPSErrors: bool,
        setDefaultViewport: bool,
        process: Optional[Popen] = None,
        closeCallback: Callable[[], Awaitable[None]] = None,
    ) -> None:
        super().__init__()
        self._ignoreHTTPSErrors = ignoreHTTPSErrors
        self._setDefaultViewport = setDefaultViewport
        self._process = process
        self._screenshotTaskQueue: List = []
        self._connection = connection

        self._defaultContext = BrowserContext(self, None)

        self._contexts: Dict[str, BrowserContext] = dict()
        for contextId in contextIds:
            self._contexts[contextId] = BrowserContext(self, contextId)

        def _dummy_callback() -> Awaitable[None]:
            fut = asyncio.get_event_loop().create_future()
            fut.set_result(None)
            return fut

        if closeCallback:
            self._closeCallback = closeCallback
        else:
            self._closeCallback = _dummy_callback

        self._targets: Dict[str, Target] = dict()
        self._connection.set_close_callback(self._on_close)
        self._connection.on(TargetNS.TargetCreated, self._targetCreated)
        self._connection.on(TargetNS.TargetDestroyed, self._targetDestroyed)
        self._connection.on(
            "Target.targetInfoChanged", self._targetInfoChanged
        )  # noqa: E501

    def _on_close(self):
        self.emit(Chrome.Events.Disconnected, None)

    @staticmethod
    async def create(
        connection: Connection,
        contextIds: List[str],
        ignoreHTTPSErrors: bool,
        appMode: bool,
        process: Optional[Popen] = None,
        closeCallback: Callable[[], Awaitable[None]] = None,
    ) -> "Chrome":
        browser = Chrome(
            connection, contextIds, ignoreHTTPSErrors, appMode, process, closeCallback
        )
        await connection.Target.setDiscoverTargets(True)
        return browser

    def process(self) -> Optional[Popen]:
        return self._process

    async def createIncognitoBrowserContext(self) -> "BrowserContext":
        nc = await self._connection.Target.createBrowserContext()
        contextId = nc["browserContextId"]
        context = BrowserContext(self, contextId)
        self._contexts[contextId] = context
        return context

    def browserContexts(self) -> List["BrowserContext"]:
        contexts = [self._defaultContext]
        for cntx in self._contexts.values():
            contexts.append(cntx)
        return contexts

    async def _disposeContext(self, contextId: Optional[str]) -> None:
        await self._connection.Target.disposeBrowserContext(browserContextId=contextId)
        del self._contexts[contextId]

    @staticmethod
    async def create(
        connection: Connection,
        contextIds: List[str],
        ignoreHTTPSErrors: bool,
        setDefaultViewport: bool,
        process: Optional[Popen] = None,
        closeCallback: Callable[[], Awaitable[None]] = None,
    ) -> "Chrome":
        browser = Chrome(
            connection,
            contextIds,
            ignoreHTTPSErrors,
            setDefaultViewport,
            process,
            closeCallback,
        )
        await connection.Target.setDiscoverTargets(True)
        return browser

    async def _targetCreated(self, event: Union[TargetCreatedEvent, dict]) -> None:
        tinfo = event["targetInfo"]
        browserContextId = tinfo["browserContextId"]
        context = (
            self._contexts.get(browserContextId)
            if browserContextId in self._contexts
            else self._defaultContext
        )
        targetId = tinfo["targetId"]
        target = Target(tinfo, context, self)
        if event["targetInfo"]["targetId"] in self._targets:
            raise BrowserError("target should not exist before create.")
        self._targets[targetId] = target
        if await target._initializedPromise:
            self.emit(TargetNS.TargetCreated, target)

    async def _targetDestroyed(self, event: Union[TargetDestroyedEvent, dict]) -> None:
        target = self._targets[event["targetId"]]
        target._initializedCallback(False)
        del self._targets[event["targetId"]]
        if await target._initializedPromise:
            self.emit(Chrome.Events.TargetDestroyed, target)
            target.browserContext.emit(Chrome.Events.TargetDestroyed, target)

    async def _targetInfoChanged(
        self, event: Union[TargetInfoChangedEvent, dict]
    ) -> None:
        target = self._targets.get(event["targetInfo"]["targetId"])
        if not target:
            raise BrowserError("target should exist before targetInfoChanged")
        target._targetInfoChanged(event["targetInfo"])

    @property
    def wsEndpoint(self) -> str:
        """Retrun websocket end point url."""
        return self._connection.url

    async def newPage(self) -> Page:
        page = await self._defaultContext.newPage()
        return page

    async def _createPageInContext(self, contextId: Optional[str]) -> Page:
        createdTarget = await self._connection.Target.createTarget(
            url="about:blank", browserContextId=contextId
        )
        target = self._targets.get(createdTarget["targetId"])
        if not await target._initializedPromise:
            raise BrowserError("Failed to create target for new page.")
        page = await target.page()
        return page

    def targets(self) -> List["Target"]:
        """Get all targets of this browser."""
        return [target for target in self._targets.values() if target._isInitialized]

    async def pages(self) -> List[Page]:
        """Get all pages of this browser."""
        pages = []
        for target in self.targets():
            page = await target.page()
            if page:
                pages.append(page)
        return pages

    async def version(self) -> str:
        version = await self._getVersion()
        return version["product"]

    async def userAgent(self) -> str:
        version = await self._getVersion()
        return version.get("userAgent", "")

    async def close(self) -> None:
        await self._closeCallback()  # Launcher.killChrome()
        await self.disconnect()

    async def disconnect(self) -> None:
        await self._connection.dispose()

    def _getVersion(self) -> Awaitable:
        return self._connection.send("Browser.getVersion")


class BrowserContext(EventEmitter):
    Events = SimpleNamespace(
        TargetCreated="targetcreated",
        TargetDestroyed="targetdestroyed",
        TargetChanged="targetchanged",
    )

    def __init__(self, browser: Chrome, contextId) -> None:
        super().__init__()
        self._browser = browser
        self._id = contextId

    def targets(self) -> List["Target"]:
        targets = []
        for t in self._browser.targets():
            if t != self:
                targets.append(t)
        return targets

    def isIncognito(self) -> bool:
        return self._id is not None

    def newPage(self):
        return self._browser._createPageInContext(self._id)

    def browser(self) -> Chrome:
        return self._browser

    async def close(self):
        await self._browser._disposeContext(self._id)


class Target(object):
    """Browser's target class."""

    def __init__(
        self,
        targetInfo: Union[TargetInfo, dict],
        browserContext: BrowserContext,
        browser: Chrome,
    ) -> None:
        self._browser = browser
        self._browserContext = browserContext
        self._targetInfo = targetInfo
        self._targetId = targetInfo["targetId"]
        self._page = None

        self._initializedPromise = asyncio.get_event_loop().create_future()
        self._isInitialized = (
            self._targetInfo["type"] != "page" or self._targetInfo["url"] != ""
        )
        if self._isInitialized:
            self._initializedCallback(True)

    def _initializedCallback(self, bl: bool) -> None:
        self._initializedPromise.set_result(bl)

    async def createCDPSession(self) -> CDPSession:
        """Create a Chrome Devtools Protocol session attached to the target."""
        return await self._browser._connection.createSession(self._targetId)

    async def page(self) -> Optional[Page]:
        """Get page of this target."""
        if self._targetInfo["type"] == "page" and self._page is None:
            client = await self._browser._connection.createSession(self._targetId)
            new_page = await Page.create(
                client,
                self,
                self._browser._ignoreHTTPSErrors,
                self._browser._setDefaultViewport,
                self._browser._screenshotTaskQueue,
            )
            self._page = new_page
            return new_page
        return self._page

    @property
    def browserContext(self):
        return self._browserContext

    @property
    def url(self) -> str:
        """Get url of this target."""
        return self._targetInfo["url"]

    @property
    def type(self) -> str:
        """Get type of this target."""
        _type = self._targetInfo["type"]
        if (
            _type == "page"
            or _type == "service_worker"
            or _type == "page"
            or _type == "background_page"
            or _type == "browser"
        ):
            return _type
        return "other"

    def _targetInfoChanged(self, targetInfo: Union[TargetInfo, dict]) -> None:
        previousURL = self._targetInfo["url"]
        self._targetInfo = targetInfo

        if not self._isInitialized and (
            self._targetInfo["type"] != "page" or self._targetInfo["url"] != ""
        ):
            self._isInitialized = True
            self._initializedCallback(True)
            return
        if previousURL != targetInfo["url"]:
            self._browser.emit(Chrome.Events.TargetChanged, self)
