# -*- coding: utf-8 -*-
"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy.types import ConnectionType, SessionType

__all__ = ["Target"]


@attr.dataclass(slots=True)
class Target(object):
    """
    Supports additional targets discovery and allows to attach to them.
    """

    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def activateTarget(self, targetId: str) -> Awaitable[Optional[dict]]:
        """
        Activates (focuses) the target.

        :param targetId: The targetId
        :type targetId: str
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict["targetId"] = targetId
        return self.client.send("Target.activateTarget", msg_dict)

    def attachToTarget(
        self, targetId: str, flatten: Optional[bool] = None
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Target.attachToTarget", msg_dict)

    def attachToBrowserTarget(self) -> Awaitable[Optional[dict]]:
        """
        Attaches to the browser target, only uses flat sessionId mode.
        """
        return self.client.send("Target.attachToBrowserTarget")

    def closeTarget(self, targetId: str) -> Awaitable[Optional[dict]]:
        """
        Closes the target. If the target is a page that gets closed too.

        :param targetId: The targetId
        :type targetId: str
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict["targetId"] = targetId
        return self.client.send("Target.closeTarget", msg_dict)

    def exposeDevToolsProtocol(
        self, targetId: str, bindingName: Optional[str] = None
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Target.exposeDevToolsProtocol", msg_dict)

    def createBrowserContext(self) -> Awaitable[Optional[dict]]:
        """
        Creates a new empty BrowserContext. Similar to an incognito profile but you can have more than
one.
        """
        return self.client.send("Target.createBrowserContext")

    def getBrowserContexts(self) -> Awaitable[Optional[dict]]:
        """
        Returns all browser contexts created with `Target.createBrowserContext` method.
        """
        return self.client.send("Target.getBrowserContexts")

    def createTarget(
        self,
        url: str,
        width: Optional[int] = None,
        height: Optional[int] = None,
        browserContextId: Optional[str] = None,
        enableBeginFrameControl: Optional[bool] = None,
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Target.createTarget", msg_dict)

    def detachFromTarget(
        self, sessionId: Optional[str] = None, targetId: Optional[str] = None
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Target.detachFromTarget", msg_dict)

    def disposeBrowserContext(self, browserContextId: str) -> Awaitable[Optional[dict]]:
        """
        Deletes a BrowserContext. All the belonging pages will be closed without calling their
beforeunload hooks.

        :param browserContextId: The browserContextId
        :type browserContextId: str
        """
        msg_dict = dict()
        if browserContextId is not None:
            msg_dict["browserContextId"] = browserContextId
        return self.client.send("Target.disposeBrowserContext", msg_dict)

    def getTargetInfo(
        self, targetId: Optional[str] = None
    ) -> Awaitable[Optional[dict]]:
        """
        Returns information about a target.

        :param targetId: The targetId
        :type targetId: Optional[str]
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict["targetId"] = targetId
        return self.client.send("Target.getTargetInfo", msg_dict)

    def getTargets(self) -> Awaitable[Optional[dict]]:
        """
        Retrieves a list of available targets.
        """
        return self.client.send("Target.getTargets")

    def sendMessageToTarget(
        self,
        message: str,
        sessionId: Optional[str] = None,
        targetId: Optional[str] = None,
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Target.sendMessageToTarget", msg_dict)

    def setAutoAttach(
        self,
        autoAttach: bool,
        waitForDebuggerOnStart: bool,
        flatten: Optional[bool] = None,
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Target.setAutoAttach", msg_dict)

    def setDiscoverTargets(self, discover: bool) -> Awaitable[Optional[dict]]:
        """
        Controls whether to discover available targets and notify via
`targetCreated/targetInfoChanged/targetDestroyed` events.

        :param discover: Whether to discover available targets.
        :type discover: bool
        """
        msg_dict = dict()
        if discover is not None:
            msg_dict["discover"] = discover
        return self.client.send("Target.setDiscoverTargets", msg_dict)

    def setRemoteLocations(self, locations: List[dict]) -> Awaitable[Optional[dict]]:
        """
        Enables target discovery for the specified locations, when `setDiscoverTargets` was set to
`true`.

        :param locations: List of remote locations.
        :type locations: List[dict]
        """
        msg_dict = dict()
        if locations is not None:
            msg_dict["locations"] = locations
        return self.client.send("Target.setRemoteLocations", msg_dict)

    def attachedToTarget(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Issued when attached to target because of auto-attach or `attachToTarget` command.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Target.attachedToTarget", _cb)

            return future

        self.client.on("Target.attachedToTarget", cb)

    def detachedFromTarget(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Issued when detached from target for any reason (including `detachFromTarget` command). Can be
        issued multiple times per target if multiple sessions have been attached to it.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Target.detachedFromTarget", _cb)

            return future

        self.client.on("Target.detachedFromTarget", cb)

    def receivedMessageFromTarget(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Notifies about a new protocol message received from the session (as reported in
        `attachedToTarget` event).
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Target.receivedMessageFromTarget", _cb)

            return future

        self.client.on("Target.receivedMessageFromTarget", cb)

    def targetCreated(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Issued when a possible inspection target is created.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Target.targetCreated", _cb)

            return future

        self.client.on("Target.targetCreated", cb)

    def targetDestroyed(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Issued when a target is destroyed.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Target.targetDestroyed", _cb)

            return future

        self.client.on("Target.targetDestroyed", cb)

    def targetCrashed(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Issued when a target has crashed.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Target.targetCrashed", _cb)

            return future

        self.client.on("Target.targetCrashed", cb)

    def targetInfoChanged(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Issued when some information about a target has changed. This only happens between
        `targetCreated` and `targetDestroyed`.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Target.targetInfoChanged", _cb)

            return future

        self.client.on("Target.targetInfoChanged", cb)
