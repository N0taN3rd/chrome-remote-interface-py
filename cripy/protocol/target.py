# -*- coding: utf-8 -*-
from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy.client import Client, TargetSession

__all__ = ["Target"]


class Target(object):
    """
    Supports additional targets discovery and allows to attach to them.
    """

    def __init__(self, client: Union["Client", "TargetSession"]) -> None:
        self.client: Union["Client", "TargetSession"] = client

    async def activateTarget(self, targetId: str) -> Optional[dict]:
        """
        Activates (focuses) the target.

        :param targetId: The targetId
        :type targetId: str
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict["targetId"] = targetId
        res = await self.client.send("Target.activateTarget", msg_dict)
        return res

    async def attachToTarget(
        self, targetId: str, flatten: Optional[bool] = None
    ) -> Optional[dict]:
        """
        Attaches to the target with given id.

        :param targetId: The targetId
        :type targetId: str
        :param flatten: Enables "flat" access to the session via specifying sessionId attribute in the commands.
        :type flatten: Optional[bool]
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict["targetId"] = targetId
        if flatten is not None:
            msg_dict["flatten"] = flatten
        res = await self.client.send("Target.attachToTarget", msg_dict)
        return res

    async def attachToBrowserTarget(self) -> Optional[dict]:
        """
        Attaches to the browser target, only uses flat sessionId mode.
        """
        res = await self.client.send("Target.attachToBrowserTarget")
        return res

    async def closeTarget(self, targetId: str) -> Optional[dict]:
        """
        Closes the target. If the target is a page that gets closed too.

        :param targetId: The targetId
        :type targetId: str
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict["targetId"] = targetId
        res = await self.client.send("Target.closeTarget", msg_dict)
        return res

    async def exposeDevToolsProtocol(
        self, targetId: str, bindingName: Optional[str] = None
    ) -> Optional[dict]:
        """
        Inject object to the target's main frame that provides a communication
channel with browser target.

Injected object will be available as `window[bindingName]`.

The object has the follwing API:
- `binding.send(json)` - a method to send messages over the remote debugging protocol
- `binding.onmessage = json => handleMessage(json)` - a callback that will be called for the protocol notifications and command responses.

        :param targetId: The targetId
        :type targetId: str
        :param bindingName: Binding name, 'cdp' if not specified.
        :type bindingName: Optional[str]
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict["targetId"] = targetId
        if bindingName is not None:
            msg_dict["bindingName"] = bindingName
        res = await self.client.send("Target.exposeDevToolsProtocol", msg_dict)
        return res

    async def createBrowserContext(self) -> Optional[dict]:
        """
        Creates a new empty BrowserContext. Similar to an incognito profile but you can have more than
one.
        """
        res = await self.client.send("Target.createBrowserContext")
        return res

    async def getBrowserContexts(self) -> Optional[dict]:
        """
        Returns all browser contexts created with `Target.createBrowserContext` method.
        """
        res = await self.client.send("Target.getBrowserContexts")
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
        Creates a new page.

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
        res = await self.client.send("Target.createTarget", msg_dict)
        return res

    async def detachFromTarget(
        self, sessionId: Optional[str] = None, targetId: Optional[str] = None
    ) -> Optional[dict]:
        """
        Detaches session with given id.

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
        res = await self.client.send("Target.detachFromTarget", msg_dict)
        return res

    async def disposeBrowserContext(self, browserContextId: str) -> Optional[dict]:
        """
        Deletes a BrowserContext. All the belonging pages will be closed without calling their
beforeunload hooks.

        :param browserContextId: The browserContextId
        :type browserContextId: str
        """
        msg_dict = dict()
        if browserContextId is not None:
            msg_dict["browserContextId"] = browserContextId
        res = await self.client.send("Target.disposeBrowserContext", msg_dict)
        return res

    async def getTargetInfo(self, targetId: Optional[str] = None) -> Optional[dict]:
        """
        Returns information about a target.

        :param targetId: The targetId
        :type targetId: Optional[str]
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict["targetId"] = targetId
        res = await self.client.send("Target.getTargetInfo", msg_dict)
        return res

    async def getTargets(self) -> Optional[dict]:
        """
        Retrieves a list of available targets.
        """
        res = await self.client.send("Target.getTargets")
        return res

    async def sendMessageToTarget(
        self,
        message: str,
        sessionId: Optional[str] = None,
        targetId: Optional[str] = None,
    ) -> Optional[dict]:
        """
        Sends protocol message over session with given id.

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
        res = await self.client.send("Target.sendMessageToTarget", msg_dict)
        return res

    async def setAutoAttach(
        self,
        autoAttach: bool,
        waitForDebuggerOnStart: bool,
        flatten: Optional[bool] = None,
    ) -> Optional[dict]:
        """
        Controls whether to automatically attach to new targets which are considered to be related to
this one. When turned on, attaches to all existing related targets as well. When turned off,
automatically detaches from all currently attached targets.

        :param autoAttach: Whether to auto-attach to related targets.
        :type autoAttach: bool
        :param waitForDebuggerOnStart: Whether to pause new targets when attaching to them. Use `Runtime.runIfWaitingForDebugger` to run paused targets.
        :type waitForDebuggerOnStart: bool
        :param flatten: Enables "flat" access to the session via specifying sessionId attribute in the commands.
        :type flatten: Optional[bool]
        """
        msg_dict = dict()
        if autoAttach is not None:
            msg_dict["autoAttach"] = autoAttach
        if waitForDebuggerOnStart is not None:
            msg_dict["waitForDebuggerOnStart"] = waitForDebuggerOnStart
        if flatten is not None:
            msg_dict["flatten"] = flatten
        res = await self.client.send("Target.setAutoAttach", msg_dict)
        return res

    async def setDiscoverTargets(self, discover: bool) -> Optional[dict]:
        """
        Controls whether to discover available targets and notify via
`targetCreated/targetInfoChanged/targetDestroyed` events.

        :param discover: Whether to discover available targets.
        :type discover: bool
        """
        msg_dict = dict()
        if discover is not None:
            msg_dict["discover"] = discover
        res = await self.client.send("Target.setDiscoverTargets", msg_dict)
        return res

    async def setRemoteLocations(self, locations: List[dict]) -> Optional[dict]:
        """
        Enables target discovery for the specified locations, when `setDiscoverTargets` was set to
`true`.

        :param locations: List of remote locations.
        :type locations: List[dict]
        """
        msg_dict = dict()
        if locations is not None:
            msg_dict["locations"] = locations
        res = await self.client.send("Target.setRemoteLocations", msg_dict)
        return res

    def attachedToTarget(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Issued when attached to target because of auto-attach or `attachToTarget` command.
        """
        if once:
            self.client.once("Target.attachedToTarget", fn)
        else:
            self.client.on("Target.attachedToTarget", fn)

    def detachedFromTarget(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Issued when detached from target for any reason (including `detachFromTarget` command). Can be
        issued multiple times per target if multiple sessions have been attached to it.
        """
        if once:
            self.client.once("Target.detachedFromTarget", fn)
        else:
            self.client.on("Target.detachedFromTarget", fn)

    def receivedMessageFromTarget(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        """
        Notifies about a new protocol message received from the session (as reported in
        `attachedToTarget` event).
        """
        if once:
            self.client.once("Target.receivedMessageFromTarget", fn)
        else:
            self.client.on("Target.receivedMessageFromTarget", fn)

    def targetCreated(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Issued when a possible inspection target is created.
        """
        if once:
            self.client.once("Target.targetCreated", fn)
        else:
            self.client.on("Target.targetCreated", fn)

    def targetDestroyed(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Issued when a target is destroyed.
        """
        if once:
            self.client.once("Target.targetDestroyed", fn)
        else:
            self.client.on("Target.targetDestroyed", fn)

    def targetCrashed(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Issued when a target has crashed.
        """
        if once:
            self.client.once("Target.targetCrashed", fn)
        else:
            self.client.on("Target.targetCrashed", fn)

    def targetInfoChanged(self, fn: Callable[..., Any], once: bool = False) -> None:
        """
        Issued when some information about a target has changed. This only happens between
        `targetCreated` and `targetDestroyed`.
        """
        if once:
            self.client.once("Target.targetInfoChanged", fn)
        else:
            self.client.on("Target.targetInfoChanged", fn)

    def __repr__(self):
        return f"Target()"
