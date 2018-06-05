from typing import Any, List, Optional, Union
from cripy.protocol.target import events as Events
from cripy.protocol.target import types as Types


class Target(object):
    """
    Supports additional targets discovery and allows to attach to them.
    """

    def __init__(self, chrome):
        self.chrome = chrome

    async def activateTarget(self, targetId: str) -> Optional[dict]:
        """
        :param targetId: The targetId
        :type targetId: str
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict["targetId"] = targetId
        mayberes = await self.chrome.send("Target.activateTarget", msg_dict)
        return mayberes

    async def attachToTarget(self, targetId: str) -> Optional[dict]:
        """
        :param targetId: The targetId
        :type targetId: str
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict["targetId"] = targetId
        mayberes = await self.chrome.send("Target.attachToTarget", msg_dict)
        res = await mayberes
        return res

    async def closeTarget(self, targetId: str) -> Optional[dict]:
        """
        :param targetId: The targetId
        :type targetId: str
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict["targetId"] = targetId
        mayberes = await self.chrome.send("Target.closeTarget", msg_dict)
        res = await mayberes
        return res

    async def createBrowserContext(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Target.createBrowserContext")
        res = await mayberes
        return res

    async def getBrowserContexts(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Target.getBrowserContexts")
        res = await mayberes
        return res

    async def createTarget(
        self,
        url: str,
        width: Optional[int] = None,
        height: Optional[int] = None,
        browserContextId: Optional[str] = None,
        enableBeginFrameControl: Optional[bool] = None,
    ) -> Optional[dict]:
        """
        :param url: The initial URL the page will be navigated to.
        :type url: str
        :param width: Frame width in DIP (headless chrome only).
        :type width: Optional[int]
        :param height: Frame height in DIP (headless chrome only).
        :type height: Optional[int]
        :param browserContextId: The browser context to create the page in.
        :type browserContextId: Optional[str]
        :param enableBeginFrameControl: Whether BeginFrames for this target will be controlled via DevTools (headless chrome only, not supported on MacOS yet, false by default).
        :type enableBeginFrameControl: Optional[bool]
        """
        msg_dict = dict()
        if url is not None:
            msg_dict["url"] = url
        if width is not None:
            msg_dict["width"] = width
        if height is not None:
            msg_dict["height"] = height
        if browserContextId is not None:
            msg_dict["browserContextId"] = browserContextId
        if enableBeginFrameControl is not None:
            msg_dict["enableBeginFrameControl"] = enableBeginFrameControl
        mayberes = await self.chrome.send("Target.createTarget", msg_dict)
        res = await mayberes
        return res

    async def detachFromTarget(
        self, sessionId: Optional[str] = None, targetId: Optional[str] = None
    ) -> Optional[dict]:
        """
        :param sessionId: Session to detach.
        :type sessionId: Optional[str]
        :param targetId: Deprecated.
        :type targetId: Optional[str]
        """
        msg_dict = dict()
        if sessionId is not None:
            msg_dict["sessionId"] = sessionId
        if targetId is not None:
            msg_dict["targetId"] = targetId
        mayberes = await self.chrome.send("Target.detachFromTarget", msg_dict)
        return mayberes

    async def disposeBrowserContext(self, browserContextId: str) -> Optional[dict]:
        """
        :param browserContextId: The browserContextId
        :type browserContextId: str
        """
        msg_dict = dict()
        if browserContextId is not None:
            msg_dict["browserContextId"] = browserContextId
        mayberes = await self.chrome.send("Target.disposeBrowserContext", msg_dict)
        return mayberes

    async def getTargetInfo(self, targetId: str) -> Optional[dict]:
        """
        :param targetId: The targetId
        :type targetId: str
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict["targetId"] = targetId
        mayberes = await self.chrome.send("Target.getTargetInfo", msg_dict)
        res = await mayberes
        res["targetInfo"] = Types.TargetInfo.safe_create(res["targetInfo"])
        return res

    async def getTargets(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Target.getTargets")
        res = await mayberes
        res["targetInfos"] = Types.TargetInfo.safe_create_from_list(res["targetInfos"])
        return res

    async def sendMessageToTarget(
        self,
        message: str,
        sessionId: Optional[str] = None,
        targetId: Optional[str] = None,
    ) -> Optional[dict]:
        """
        :param message: The message
        :type message: str
        :param sessionId: Identifier of the session.
        :type sessionId: Optional[str]
        :param targetId: Deprecated.
        :type targetId: Optional[str]
        """
        msg_dict = dict()
        if message is not None:
            msg_dict["message"] = message
        if sessionId is not None:
            msg_dict["sessionId"] = sessionId
        if targetId is not None:
            msg_dict["targetId"] = targetId
        mayberes = await self.chrome.send("Target.sendMessageToTarget", msg_dict)
        return mayberes

    async def setAutoAttach(
        self, autoAttach: bool, waitForDebuggerOnStart: bool
    ) -> Optional[dict]:
        """
        :param autoAttach: Whether to auto-attach to related targets.
        :type autoAttach: bool
        :param waitForDebuggerOnStart: Whether to pause new targets when attaching to them. Use `Runtime.runIfWaitingForDebugger` to run paused targets.
        :type waitForDebuggerOnStart: bool
        """
        msg_dict = dict()
        if autoAttach is not None:
            msg_dict["autoAttach"] = autoAttach
        if waitForDebuggerOnStart is not None:
            msg_dict["waitForDebuggerOnStart"] = waitForDebuggerOnStart
        mayberes = await self.chrome.send("Target.setAutoAttach", msg_dict)
        return mayberes

    async def setDiscoverTargets(self, discover: bool) -> Optional[dict]:
        """
        :param discover: Whether to discover available targets.
        :type discover: bool
        """
        msg_dict = dict()
        if discover is not None:
            msg_dict["discover"] = discover
        mayberes = await self.chrome.send("Target.setDiscoverTargets", msg_dict)
        return mayberes

    async def setRemoteLocations(self, locations: List[dict]) -> Optional[dict]:
        """
        :param locations: List of remote locations.
        :type locations: List[dict]
        """
        msg_dict = dict()
        if locations is not None:
            msg_dict["locations"] = locations
        mayberes = await self.chrome.send("Target.setRemoteLocations", msg_dict)
        return mayberes

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return Events.EVENT_TO_CLASS
