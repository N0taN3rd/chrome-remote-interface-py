from types import SimpleNamespace
from cripy.sync.protocol.runtime import types as Runtime
from cripy.sync.protocol.network import types as Network
try:
    from cripy.sync.protocol.page.types import *
except ImportError:
    pass

__all__ = [
    "DomContentEventFiredEvent",
    "FrameAttachedEvent",
    "FrameClearedScheduledNavigationEvent",
    "FrameDetachedEvent",
    "FrameNavigatedEvent",
    "FrameResizedEvent",
    "FrameScheduledNavigationEvent",
    "FrameStartedLoadingEvent",
    "FrameStoppedLoadingEvent",
    "InterstitialHiddenEvent",
    "InterstitialShownEvent",
    "JavascriptDialogClosedEvent",
    "JavascriptDialogOpeningEvent",
    "LifecycleEventEvent",
    "LoadEventFiredEvent",
    "NavigatedWithinDocumentEvent",
    "ScreencastFrameEvent",
    "ScreencastVisibilityChangedEvent",
    "WindowOpenEvent",
]


class DomContentEventFiredEvent(object):

    event = "Page.domContentEventFired"

    def __init__(self, timestamp):
        """
        :param timestamp: The timestamp
        :type timestamp: float
        """
        super().__init__()
        self.timestamp = timestamp

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        return "DomContentEventFiredEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = DomContentEventFiredEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DomContentEventFiredEvent.safe_create(it))
            return list_of_self
        else:
            return init


class FrameAttachedEvent(object):
    """
    Fired when frame has been attached to its parent.
    """

    event = "Page.frameAttached"

    def __init__(self, frameId, parentFrameId, stack):
        """
        :param frameId: Id of the frame that has been attached.
        :type frameId: str
        :param parentFrameId: Parent frame identifier.
        :type parentFrameId: str
        :param stack: JavaScript stack trace of when frame was attached, only set if frame initiated from script.
        :type stack: Optional[dict]
        """
        super().__init__()
        self.frameId = frameId
        self.parentFrameId = parentFrameId
        self.stack = Runtime.StackTrace.safe_create(stack)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.frameId is not None:
            repr_args.append("frameId={!r}".format(self.frameId))
        if self.parentFrameId is not None:
            repr_args.append("parentFrameId={!r}".format(self.parentFrameId))
        if self.stack is not None:
            repr_args.append("stack={!r}".format(self.stack))
        return "FrameAttachedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = FrameAttachedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FrameAttachedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class FrameClearedScheduledNavigationEvent(object):
    """
    Fired when frame no longer has a scheduled navigation.
    """

    event = "Page.frameClearedScheduledNavigation"

    def __init__(self, frameId):
        """
        :param frameId: Id of the frame that has cleared its scheduled navigation.
        :type frameId: str
        """
        super().__init__()
        self.frameId = frameId

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.frameId is not None:
            repr_args.append("frameId={!r}".format(self.frameId))
        return "FrameClearedScheduledNavigationEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = FrameClearedScheduledNavigationEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FrameClearedScheduledNavigationEvent.safe_create(it))
            return list_of_self
        else:
            return init


class FrameDetachedEvent(object):
    """
    Fired when frame has been detached from its parent.
    """

    event = "Page.frameDetached"

    def __init__(self, frameId):
        """
        :param frameId: Id of the frame that has been detached.
        :type frameId: str
        """
        super().__init__()
        self.frameId = frameId

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.frameId is not None:
            repr_args.append("frameId={!r}".format(self.frameId))
        return "FrameDetachedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = FrameDetachedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FrameDetachedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class FrameNavigatedEvent(object):
    """
    Fired once navigation of the frame has completed.
	Frame is now associated with the new loader.
    """

    event = "Page.frameNavigated"

    def __init__(self, frame):
        """
        :param frame: Frame object.
        :type frame: dict
        """
        super().__init__()
        self.frame = Frame.safe_create(frame)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.frame is not None:
            repr_args.append("frame={!r}".format(self.frame))
        return "FrameNavigatedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = FrameNavigatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FrameNavigatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class FrameResizedEvent(dict):

    event = "Page.frameResized"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def __repr__(self):
        return "FrameResizedEvent(dict)"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = FrameResizedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FrameResizedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class FrameScheduledNavigationEvent(object):
    """
    Fired when frame schedules a potential navigation.
    """

    event = "Page.frameScheduledNavigation"

    def __init__(self, frameId, delay, reason, url):
        """
        :param frameId: Id of the frame that has scheduled a navigation.
        :type frameId: str
        :param delay: Delay (in seconds) until the navigation is scheduled to begin. The navigation is not guaranteed to start.
        :type delay: float
        :param reason: The reason for the navigation.
        :type reason: str
        :param url: The destination URL for the scheduled navigation.
        :type url: str
        """
        super().__init__()
        self.frameId = frameId
        self.delay = delay
        self.reason = reason
        self.url = url

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.frameId is not None:
            repr_args.append("frameId={!r}".format(self.frameId))
        if self.delay is not None:
            repr_args.append("delay={!r}".format(self.delay))
        if self.reason is not None:
            repr_args.append("reason={!r}".format(self.reason))
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        return "FrameScheduledNavigationEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = FrameScheduledNavigationEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FrameScheduledNavigationEvent.safe_create(it))
            return list_of_self
        else:
            return init


class FrameStartedLoadingEvent(object):
    """
    Fired when frame has started loading.
    """

    event = "Page.frameStartedLoading"

    def __init__(self, frameId):
        """
        :param frameId: Id of the frame that has started loading.
        :type frameId: str
        """
        super().__init__()
        self.frameId = frameId

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.frameId is not None:
            repr_args.append("frameId={!r}".format(self.frameId))
        return "FrameStartedLoadingEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = FrameStartedLoadingEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FrameStartedLoadingEvent.safe_create(it))
            return list_of_self
        else:
            return init


class FrameStoppedLoadingEvent(object):
    """
    Fired when frame has stopped loading.
    """

    event = "Page.frameStoppedLoading"

    def __init__(self, frameId):
        """
        :param frameId: Id of the frame that has stopped loading.
        :type frameId: str
        """
        super().__init__()
        self.frameId = frameId

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.frameId is not None:
            repr_args.append("frameId={!r}".format(self.frameId))
        return "FrameStoppedLoadingEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = FrameStoppedLoadingEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FrameStoppedLoadingEvent.safe_create(it))
            return list_of_self
        else:
            return init


class InterstitialHiddenEvent(dict):
    """
    Fired when interstitial page was hidden
    """

    event = "Page.interstitialHidden"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def __repr__(self):
        return "InterstitialHiddenEvent(dict)"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = InterstitialHiddenEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(InterstitialHiddenEvent.safe_create(it))
            return list_of_self
        else:
            return init


class InterstitialShownEvent(dict):
    """
    Fired when interstitial page was shown
    """

    event = "Page.interstitialShown"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def __repr__(self):
        return "InterstitialShownEvent(dict)"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = InterstitialShownEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(InterstitialShownEvent.safe_create(it))
            return list_of_self
        else:
            return init


class JavascriptDialogClosedEvent(object):
    """
    Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) has been closed.
    """

    event = "Page.javascriptDialogClosed"

    def __init__(self, result, userInput):
        """
        :param result: Whether dialog was confirmed.
        :type result: bool
        :param userInput: User input in case of prompt.
        :type userInput: str
        """
        super().__init__()
        self.result = result
        self.userInput = userInput

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.result is not None:
            repr_args.append("result={!r}".format(self.result))
        if self.userInput is not None:
            repr_args.append("userInput={!r}".format(self.userInput))
        return "JavascriptDialogClosedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = JavascriptDialogClosedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(JavascriptDialogClosedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class JavascriptDialogOpeningEvent(object):
    """
    Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) is about to open.
    """

    event = "Page.javascriptDialogOpening"

    def __init__(self, url, message, type, hasBrowserHandler, defaultPrompt):
        """
        :param url: Frame url.
        :type url: str
        :param message: Message that will be displayed by the dialog.
        :type message: str
        :param type: Dialog type.
        :type type: str
        :param hasBrowserHandler: True iff browser is capable showing or acting on the given dialog. When browser has no dialog handler for given target, calling alert while Page domain is engaged will stall the page execution. Execution can be resumed via calling Page.handleJavaScriptDialog.
        :type hasBrowserHandler: bool
        :param defaultPrompt: Default dialog prompt.
        :type defaultPrompt: Optional[str]
        """
        super().__init__()
        self.url = url
        self.message = message
        self.type = type
        self.hasBrowserHandler = hasBrowserHandler
        self.defaultPrompt = defaultPrompt

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.message is not None:
            repr_args.append("message={!r}".format(self.message))
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        if self.hasBrowserHandler is not None:
            repr_args.append("hasBrowserHandler={!r}".format(self.hasBrowserHandler))
        if self.defaultPrompt is not None:
            repr_args.append("defaultPrompt={!r}".format(self.defaultPrompt))
        return "JavascriptDialogOpeningEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = JavascriptDialogOpeningEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(JavascriptDialogOpeningEvent.safe_create(it))
            return list_of_self
        else:
            return init


class LifecycleEventEvent(object):
    """
    Fired for top level page lifecycle events such as navigation, load, paint, etc.
    """

    event = "Page.lifecycleEvent"

    def __init__(self, frameId, loaderId, name, timestamp):
        """
        :param frameId: Id of the frame.
        :type frameId: str
        :param loaderId: Loader identifier. Empty string if the request is fetched from worker.
        :type loaderId: str
        :param name: The name
        :type name: str
        :param timestamp: The timestamp
        :type timestamp: float
        """
        super().__init__()
        self.frameId = frameId
        self.loaderId = loaderId
        self.name = name
        self.timestamp = timestamp

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.frameId is not None:
            repr_args.append("frameId={!r}".format(self.frameId))
        if self.loaderId is not None:
            repr_args.append("loaderId={!r}".format(self.loaderId))
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        return "LifecycleEventEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = LifecycleEventEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LifecycleEventEvent.safe_create(it))
            return list_of_self
        else:
            return init


class LoadEventFiredEvent(object):

    event = "Page.loadEventFired"

    def __init__(self, timestamp):
        """
        :param timestamp: The timestamp
        :type timestamp: float
        """
        super().__init__()
        self.timestamp = timestamp

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        return "LoadEventFiredEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = LoadEventFiredEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LoadEventFiredEvent.safe_create(it))
            return list_of_self
        else:
            return init


class NavigatedWithinDocumentEvent(object):
    """
    Fired when same-document navigation happens, e.g.
	due to history API usage or anchor navigation.
    """

    event = "Page.navigatedWithinDocument"

    def __init__(self, frameId, url):
        """
        :param frameId: Id of the frame.
        :type frameId: str
        :param url: Frame's new url.
        :type url: str
        """
        super().__init__()
        self.frameId = frameId
        self.url = url

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.frameId is not None:
            repr_args.append("frameId={!r}".format(self.frameId))
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        return "NavigatedWithinDocumentEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = NavigatedWithinDocumentEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(NavigatedWithinDocumentEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ScreencastFrameEvent(object):
    """
    Compressed image data requested by the `startScreencast`.
    """

    event = "Page.screencastFrame"

    def __init__(self, data, metadata, sessionId):
        """
        :param data: Base64-encoded compressed image.
        :type data: str
        :param metadata: Screencast frame metadata.
        :type metadata: dict
        :param sessionId: Frame number.
        :type sessionId: int
        """
        super().__init__()
        self.data = data
        self.metadata = ScreencastFrameMetadata.safe_create(metadata)
        self.sessionId = sessionId

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.data is not None:
            repr_args.append("data={!r}".format(self.data))
        if self.metadata is not None:
            repr_args.append("metadata={!r}".format(self.metadata))
        if self.sessionId is not None:
            repr_args.append("sessionId={!r}".format(self.sessionId))
        return "ScreencastFrameEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = ScreencastFrameEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ScreencastFrameEvent.safe_create(it))
            return list_of_self
        else:
            return init


class ScreencastVisibilityChangedEvent(object):
    """
    Fired when the page with currently enabled screencast was shown or hidden `.
    """

    event = "Page.screencastVisibilityChanged"

    def __init__(self, visible):
        """
        :param visible: True if the page is visible.
        :type visible: bool
        """
        super().__init__()
        self.visible = visible

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.visible is not None:
            repr_args.append("visible={!r}".format(self.visible))
        return "ScreencastVisibilityChangedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = ScreencastVisibilityChangedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ScreencastVisibilityChangedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class WindowOpenEvent(object):
    """
    Fired when a new window is going to be opened, via window.open(), link click, form submission, etc.
    """

    event = "Page.windowOpen"

    def __init__(self, url, windowName, windowFeatures, userGesture):
        """
        :param url: The URL for the new window.
        :type url: str
        :param windowName: Window name.
        :type windowName: str
        :param windowFeatures: An array of enabled window features.
        :type windowFeatures: List[str]
        :param userGesture: Whether or not it was triggered by user gesture.
        :type userGesture: bool
        """
        super().__init__()
        self.url = url
        self.windowName = windowName
        self.windowFeatures = windowFeatures
        self.userGesture = userGesture

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.windowName is not None:
            repr_args.append("windowName={!r}".format(self.windowName))
        if self.windowFeatures is not None:
            repr_args.append("windowFeatures={!r}".format(self.windowFeatures))
        if self.userGesture is not None:
            repr_args.append("userGesture={!r}".format(self.userGesture))
        return "WindowOpenEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = WindowOpenEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WindowOpenEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "Page.domContentEventFired": DomContentEventFiredEvent,
   "Page.frameAttached": FrameAttachedEvent,
   "Page.frameClearedScheduledNavigation": FrameClearedScheduledNavigationEvent,
   "Page.frameDetached": FrameDetachedEvent,
   "Page.frameNavigated": FrameNavigatedEvent,
   "Page.frameResized": FrameResizedEvent,
   "Page.frameScheduledNavigation": FrameScheduledNavigationEvent,
   "Page.frameStartedLoading": FrameStartedLoadingEvent,
   "Page.frameStoppedLoading": FrameStoppedLoadingEvent,
   "Page.interstitialHidden": InterstitialHiddenEvent,
   "Page.interstitialShown": InterstitialShownEvent,
   "Page.javascriptDialogClosed": JavascriptDialogClosedEvent,
   "Page.javascriptDialogOpening": JavascriptDialogOpeningEvent,
   "Page.lifecycleEvent": LifecycleEventEvent,
   "Page.loadEventFired": LoadEventFiredEvent,
   "Page.navigatedWithinDocument": NavigatedWithinDocumentEvent,
   "Page.screencastFrame": ScreencastFrameEvent,
   "Page.screencastVisibilityChanged": ScreencastVisibilityChangedEvent,
   "Page.windowOpen": WindowOpenEvent,
}

EVENT_NS = SimpleNamespace(
  DomContentEventFired="Page.domContentEventFired",
  FrameAttached="Page.frameAttached",
  FrameClearedScheduledNavigation="Page.frameClearedScheduledNavigation",
  FrameDetached="Page.frameDetached",
  FrameNavigated="Page.frameNavigated",
  FrameResized="Page.frameResized",
  FrameScheduledNavigation="Page.frameScheduledNavigation",
  FrameStartedLoading="Page.frameStartedLoading",
  FrameStoppedLoading="Page.frameStoppedLoading",
  InterstitialHidden="Page.interstitialHidden",
  InterstitialShown="Page.interstitialShown",
  JavascriptDialogClosed="Page.javascriptDialogClosed",
  JavascriptDialogOpening="Page.javascriptDialogOpening",
  LifecycleEvent="Page.lifecycleEvent",
  LoadEventFired="Page.loadEventFired",
  NavigatedWithinDocument="Page.navigatedWithinDocument",
  ScreencastFrame="Page.screencastFrame",
  ScreencastVisibilityChanged="Page.screencastVisibilityChanged",
  WindowOpen="Page.windowOpen",
)
