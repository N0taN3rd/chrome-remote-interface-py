"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Target"]


class Target:
    """
    Supports additional targets discovery and allows to attach to them.
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/Target`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of Target

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def activateTarget(self, targetId: str) -> Awaitable[Dict]:
        """
        Activates (focuses) the target.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Target#method-activateTarget`

        :param targetId: The targetId
        :return: The results of the command
        """
        return self.client.send("Target.activateTarget", {"targetId": targetId})

    def attachToTarget(
        self, targetId: str, flatten: Optional[bool] = None
    ) -> Awaitable[Dict]:
        """
        Attaches to the target with given id.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Target#method-attachToTarget`

        :param targetId: The targetId
        :param flatten: Enables "flat" access to the session via specifying sessionId attribute in the commands.
        :return: The results of the command
        """
        msg = {"targetId": targetId}
        if flatten is not None:
            msg["flatten"] = flatten
        return self.client.send("Target.attachToTarget", msg)

    def attachToBrowserTarget(self) -> Awaitable[Dict]:
        """
        Attaches to the browser target, only uses flat sessionId mode.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Target#method-attachToBrowserTarget`

        :return: The results of the command
        """
        return self.client.send("Target.attachToBrowserTarget", {})

    def closeTarget(self, targetId: str) -> Awaitable[Dict]:
        """
        Closes the target. If the target is a page that gets closed too.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Target#method-closeTarget`

        :param targetId: The targetId
        :return: The results of the command
        """
        return self.client.send("Target.closeTarget", {"targetId": targetId})

    def exposeDevToolsProtocol(
        self, targetId: str, bindingName: Optional[str] = None
    ) -> Awaitable[Dict]:
        """
        Inject object to the target's main frame that provides a communication
        channel with browser target.
        
        Injected object will be available as `window[bindingName]`.
        
        The object has the follwing API:
        - `binding.send(json)` - a method to send messages over the remote debugging protocol
        - `binding.onmessage = json => handleMessage(json)` - a callback that will be called for the protocol notifications and command responses.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Target#method-exposeDevToolsProtocol`

        :param targetId: The targetId
        :param bindingName: Binding name, 'cdp' if not specified.
        :return: The results of the command
        """
        msg = {"targetId": targetId}
        if bindingName is not None:
            msg["bindingName"] = bindingName
        return self.client.send("Target.exposeDevToolsProtocol", msg)

    def createBrowserContext(self) -> Awaitable[Dict]:
        """
        Creates a new empty BrowserContext. Similar to an incognito profile but you can have more than
        one.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Target#method-createBrowserContext`

        :return: The results of the command
        """
        return self.client.send("Target.createBrowserContext", {})

    def getBrowserContexts(self) -> Awaitable[Dict]:
        """
        Returns all browser contexts created with `Target.createBrowserContext` method.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Target#method-getBrowserContexts`

        :return: The results of the command
        """
        return self.client.send("Target.getBrowserContexts", {})

    def createTarget(
        self,
        url: str,
        width: Optional[int] = None,
        height: Optional[int] = None,
        browserContextId: Optional[str] = None,
        enableBeginFrameControl: Optional[bool] = None,
    ) -> Awaitable[Dict]:
        """
        Creates a new page.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Target#method-createTarget`

        :param url: The initial URL the page will be navigated to.
        :param width: Frame width in DIP (headless chrome only).
        :param height: Frame height in DIP (headless chrome only).
        :param browserContextId: The browser context to create the page in.
        :param enableBeginFrameControl: Whether BeginFrames for this target will be controlled via DevTools (headless chrome only,
         not supported on MacOS yet, false by default).
        :return: The results of the command
        """
        msg = {"url": url}
        if width is not None:
            msg["width"] = width
        if height is not None:
            msg["height"] = height
        if browserContextId is not None:
            msg["browserContextId"] = browserContextId
        if enableBeginFrameControl is not None:
            msg["enableBeginFrameControl"] = enableBeginFrameControl
        return self.client.send("Target.createTarget", msg)

    def detachFromTarget(
        self, sessionId: Optional[str] = None, targetId: Optional[str] = None
    ) -> Awaitable[Dict]:
        """
        Detaches session with given id.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Target#method-detachFromTarget`

        :param sessionId: Session to detach.
        :param targetId: Deprecated.
        :return: The results of the command
        """
        msg = {}
        if sessionId is not None:
            msg["sessionId"] = sessionId
        if targetId is not None:
            msg["targetId"] = targetId
        return self.client.send("Target.detachFromTarget", msg)

    def disposeBrowserContext(self, browserContextId: str) -> Awaitable[Dict]:
        """
        Deletes a BrowserContext. All the belonging pages will be closed without calling their
        beforeunload hooks.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Target#method-disposeBrowserContext`

        :param browserContextId: The browserContextId
        :return: The results of the command
        """
        return self.client.send(
            "Target.disposeBrowserContext", {"browserContextId": browserContextId}
        )

    def getTargetInfo(self, targetId: Optional[str] = None) -> Awaitable[Dict]:
        """
        Returns information about a target.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Target#method-getTargetInfo`

        :param targetId: The targetId
        :return: The results of the command
        """
        msg = {}
        if targetId is not None:
            msg["targetId"] = targetId
        return self.client.send("Target.getTargetInfo", msg)

    def getTargets(self) -> Awaitable[Dict]:
        """
        Retrieves a list of available targets.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Target#method-getTargets`

        :return: The results of the command
        """
        return self.client.send("Target.getTargets", {})

    def sendMessageToTarget(
        self,
        message: str,
        sessionId: Optional[str] = None,
        targetId: Optional[str] = None,
    ) -> Awaitable[Dict]:
        """
        Sends protocol message over session with given id.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Target#method-sendMessageToTarget`

        :param message: The message
        :param sessionId: Identifier of the session.
        :param targetId: Deprecated.
        :return: The results of the command
        """
        msg = {"message": message}
        if sessionId is not None:
            msg["sessionId"] = sessionId
        if targetId is not None:
            msg["targetId"] = targetId
        return self.client.send("Target.sendMessageToTarget", msg)

    def setAutoAttach(
        self,
        autoAttach: bool,
        waitForDebuggerOnStart: bool,
        flatten: Optional[bool] = None,
    ) -> Awaitable[Dict]:
        """
        Controls whether to automatically attach to new targets which are considered to be related to
        this one. When turned on, attaches to all existing related targets as well. When turned off,
        automatically detaches from all currently attached targets.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Target#method-setAutoAttach`

        :param autoAttach: Whether to auto-attach to related targets.
        :param waitForDebuggerOnStart: Whether to pause new targets when attaching to them. Use `Runtime.runIfWaitingForDebugger`
         to run paused targets.
        :param flatten: Enables "flat" access to the session via specifying sessionId attribute in the commands.
        :return: The results of the command
        """
        msg = {
            "autoAttach": autoAttach,
            "waitForDebuggerOnStart": waitForDebuggerOnStart,
        }
        if flatten is not None:
            msg["flatten"] = flatten
        return self.client.send("Target.setAutoAttach", msg)

    def setDiscoverTargets(self, discover: bool) -> Awaitable[Dict]:
        """
        Controls whether to discover available targets and notify via
        `targetCreated/targetInfoChanged/targetDestroyed` events.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Target#method-setDiscoverTargets`

        :param discover: Whether to discover available targets.
        :return: The results of the command
        """
        return self.client.send("Target.setDiscoverTargets", {"discover": discover})

    def setRemoteLocations(self, locations: List[Dict[str, Any]]) -> Awaitable[Dict]:
        """
        Enables target discovery for the specified locations, when `setDiscoverTargets` was set to
        `true`.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Target#method-setRemoteLocations`

        :param locations: List of remote locations.
        :return: The results of the command
        """
        return self.client.send("Target.setRemoteLocations", {"locations": locations})

    def attachedToTarget(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Issued when attached to target because of auto-attach or `attachToTarget` command.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Target#event-attachedToTarget`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Target.attachedToTarget"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def detachedFromTarget(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Issued when detached from target for any reason (including `detachFromTarget` command). Can be
        issued multiple times per target if multiple sessions have been attached to it.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Target#event-detachedFromTarget`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Target.detachedFromTarget"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def receivedMessageFromTarget(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Notifies about a new protocol message received from the session (as reported in
        `attachedToTarget` event).

        See `https://chromedevtools.github.io/devtools-protocol/tot/Target#event-receivedMessageFromTarget`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Target.receivedMessageFromTarget"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def targetCreated(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Issued when a possible inspection target is created.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Target#event-targetCreated`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Target.targetCreated"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def targetDestroyed(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Issued when a target is destroyed.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Target#event-targetDestroyed`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Target.targetDestroyed"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def targetCrashed(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Issued when a target has crashed.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Target#event-targetCrashed`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Target.targetCrashed"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def targetInfoChanged(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Issued when some information about a target has changed. This only happens between
        `targetCreated` and `targetDestroyed`.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Target#event-targetInfoChanged`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Target.targetInfoChanged"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
