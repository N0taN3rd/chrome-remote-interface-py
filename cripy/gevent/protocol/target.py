__all__ = ["Target"]


class Target(object):
    """
    Supports additional targets discovery and allows to attach to them.
    """

    def __init__(self, chrome):
        """
        Construct a new Target object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def activateTarget(self, targetId):
        """
        Activates (focuses) the target.

        :param targetId: The targetId
        :type targetId: str
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict['targetId'] = targetId
        wres = self.chrome.send('Target.activateTarget', msg_dict)
        return wres.get()

    def attachToTarget(self, targetId):
        """
        Attaches to the target with given id.

        :param targetId: The targetId
        :type targetId: str
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict['targetId'] = targetId
        wres = self.chrome.send('Target.attachToTarget', msg_dict)
        return wres.get()

    def closeTarget(self, targetId):
        """
        Closes the target. If the target is a page that gets closed too.

        :param targetId: The targetId
        :type targetId: str
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict['targetId'] = targetId
        wres = self.chrome.send('Target.closeTarget', msg_dict)
        return wres.get()

    def createBrowserContext(self):
        """
        Creates a new empty BrowserContext. Similar to an incognito profile but you can have more than
one.
        """
        wres = self.chrome.send('Target.createBrowserContext')
        return wres.get()

    def getBrowserContexts(self):
        """
        Returns all browser contexts created with `Target.createBrowserContext` method.
        """
        wres = self.chrome.send('Target.getBrowserContexts')
        return wres.get()

    def createTarget(self, url, width=None, height=None, browserContextId=None, enableBeginFrameControl=None):
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
            msg_dict['url'] = url
        if width is not None:
            msg_dict['width'] = width
        if height is not None:
            msg_dict['height'] = height
        if browserContextId is not None:
            msg_dict['browserContextId'] = browserContextId
        if enableBeginFrameControl is not None:
            msg_dict['enableBeginFrameControl'] = enableBeginFrameControl
        wres = self.chrome.send('Target.createTarget', msg_dict)
        return wres.get()

    def detachFromTarget(self, sessionId=None, targetId=None):
        """
        Detaches session with given id.

        :param sessionId: Session to detach.
        :type sessionId: Optional[str]
        :param targetId: Deprecated.
        :type targetId: Optional[str]
        """
        msg_dict = dict()
        if sessionId is not None:
            msg_dict['sessionId'] = sessionId
        if targetId is not None:
            msg_dict['targetId'] = targetId
        wres = self.chrome.send('Target.detachFromTarget', msg_dict)
        return wres.get()

    def disposeBrowserContext(self, browserContextId):
        """
        Deletes a BrowserContext. All the belonging pages will be closed without calling their
beforeunload hooks.

        :param browserContextId: The browserContextId
        :type browserContextId: str
        """
        msg_dict = dict()
        if browserContextId is not None:
            msg_dict['browserContextId'] = browserContextId
        wres = self.chrome.send('Target.disposeBrowserContext', msg_dict)
        return wres.get()

    def getTargetInfo(self, targetId):
        """
        Returns information about a target.

        :param targetId: The targetId
        :type targetId: str
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict['targetId'] = targetId
        wres = self.chrome.send('Target.getTargetInfo', msg_dict)
        return wres.get()

    def getTargets(self):
        """
        Retrieves a list of available targets.
        """
        wres = self.chrome.send('Target.getTargets')
        return wres.get()

    def sendMessageToTarget(self, message, sessionId=None, targetId=None):
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
            msg_dict['message'] = message
        if sessionId is not None:
            msg_dict['sessionId'] = sessionId
        if targetId is not None:
            msg_dict['targetId'] = targetId
        wres = self.chrome.send('Target.sendMessageToTarget', msg_dict)
        return wres.get()

    def setAutoAttach(self, autoAttach, waitForDebuggerOnStart):
        """
        Controls whether to automatically attach to new targets which are considered to be related to
this one. When turned on, attaches to all existing related targets as well. When turned off,
automatically detaches from all currently attached targets.

        :param autoAttach: Whether to auto-attach to related targets.
        :type autoAttach: bool
        :param waitForDebuggerOnStart: Whether to pause new targets when attaching to them. Use `Runtime.runIfWaitingForDebugger` to run paused targets.
        :type waitForDebuggerOnStart: bool
        """
        msg_dict = dict()
        if autoAttach is not None:
            msg_dict['autoAttach'] = autoAttach
        if waitForDebuggerOnStart is not None:
            msg_dict['waitForDebuggerOnStart'] = waitForDebuggerOnStart
        wres = self.chrome.send('Target.setAutoAttach', msg_dict)
        return wres.get()

    def setDiscoverTargets(self, discover):
        """
        Controls whether to discover available targets and notify via
`targetCreated/targetInfoChanged/targetDestroyed` events.

        :param discover: Whether to discover available targets.
        :type discover: bool
        """
        msg_dict = dict()
        if discover is not None:
            msg_dict['discover'] = discover
        wres = self.chrome.send('Target.setDiscoverTargets', msg_dict)
        return wres.get()

    def setRemoteLocations(self, locations):
        """
        Enables target discovery for the specified locations, when `setDiscoverTargets` was set to
`true`.

        :param locations: List of remote locations.
        :type locations: List[dict]
        """
        msg_dict = dict()
        if locations is not None:
            msg_dict['locations'] = locations
        wres = self.chrome.send('Target.setRemoteLocations', msg_dict)
        return wres.get()

    def attachedToTarget(self, fn, once=False):
        """
        Issued when attached to target because of auto-attach or `attachToTarget` command.
        """
        self.chrome.on("Target.attachedToTarget", fn, once=once)

    def detachedFromTarget(self, fn, once=False):
        """
        Issued when detached from target for any reason (including `detachFromTarget` command). Can be
        issued multiple times per target if multiple sessions have been attached to it.
        """
        self.chrome.on("Target.detachedFromTarget", fn, once=once)

    def receivedMessageFromTarget(self, fn, once=False):
        """
        Notifies about a new protocol message received from the session (as reported in
        `attachedToTarget` event).
        """
        self.chrome.on("Target.receivedMessageFromTarget", fn, once=once)

    def targetCreated(self, fn, once=False):
        """
        Issued when a possible inspection target is created.
        """
        self.chrome.on("Target.targetCreated", fn, once=once)

    def targetDestroyed(self, fn, once=False):
        """
        Issued when a target is destroyed.
        """
        self.chrome.on("Target.targetDestroyed", fn, once=once)

    def targetInfoChanged(self, fn, once=False):
        """
        Issued when some information about a target has changed. This only happens between
        `targetCreated` and `targetDestroyed`.
        """
        self.chrome.on("Target.targetInfoChanged", fn, once=once)


