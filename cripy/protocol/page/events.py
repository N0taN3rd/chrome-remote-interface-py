from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
from cripy.protocol.runtime import types as Runtime
from cripy.protocol.network import types as Network
from cripy.protocol.page.types import (
    ScreencastFrameMetadata,
    FrameId,
    DialogType,
    Frame,
)


class DomContentEventFiredEvent(BaseEvent):

    event = "Page.domContentEventFired"

    def __init__(self, timestamp: Network.MonotonicTime) -> None:
        """
        :param timestamp: The timestamp
        :type timestamp: float
        """
        super().__init__()
        self.timestamp = timestamp

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['DomContentEventFiredEvent']:
        if init is not None:
            return DomContentEventFiredEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['DomContentEventFiredEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DomContentEventFiredEvent(**it))
            return list_of_self
        else:
            return init


class FrameAttachedEvent(BaseEvent):
    """
    Fired when frame has been attached to its parent.
    """

    event = "Page.frameAttached"

    def __init__(self, frameId: FrameId, parentFrameId: FrameId, stack: Optional[Union[Runtime.StackTrace, dict]] = None) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['FrameAttachedEvent']:
        if init is not None:
            return FrameAttachedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['FrameAttachedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FrameAttachedEvent(**it))
            return list_of_self
        else:
            return init


class FrameClearedScheduledNavigationEvent(BaseEvent):
    """
    Fired when frame no longer has a scheduled navigation.
    """

    event = "Page.frameClearedScheduledNavigation"

    def __init__(self, frameId: FrameId) -> None:
        """
        :param frameId: Id of the frame that has cleared its scheduled navigation.
        :type frameId: str
        """
        super().__init__()
        self.frameId = frameId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['FrameClearedScheduledNavigationEvent']:
        if init is not None:
            return FrameClearedScheduledNavigationEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['FrameClearedScheduledNavigationEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FrameClearedScheduledNavigationEvent(**it))
            return list_of_self
        else:
            return init


class FrameDetachedEvent(BaseEvent):
    """
    Fired when frame has been detached from its parent.
    """

    event = "Page.frameDetached"

    def __init__(self, frameId: FrameId) -> None:
        """
        :param frameId: Id of the frame that has been detached.
        :type frameId: str
        """
        super().__init__()
        self.frameId = frameId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['FrameDetachedEvent']:
        if init is not None:
            return FrameDetachedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['FrameDetachedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FrameDetachedEvent(**it))
            return list_of_self
        else:
            return init


class FrameNavigatedEvent(BaseEvent):
    """
    Fired once navigation of the frame has completed.
	Frame is now associated with the new loader.
    """

    event = "Page.frameNavigated"

    def __init__(self, frame: Union[Frame, dict]) -> None:
        """
        :param frame: Frame object.
        :type frame: dict
        """
        super().__init__()
        self.frame = Frame.safe_create(frame)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['FrameNavigatedEvent']:
        if init is not None:
            return FrameNavigatedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['FrameNavigatedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FrameNavigatedEvent(**it))
            return list_of_self
        else:
            return init


class FrameResizedEvent(BaseEvent):

    event = "Page.frameResized"

    def __init__(self, ) -> None:
        super().__init__()

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['FrameResizedEvent']:
        if init is not None:
            return FrameResizedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['FrameResizedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FrameResizedEvent(**it))
            return list_of_self
        else:
            return init


class FrameScheduledNavigationEvent(BaseEvent):
    """
    Fired when frame schedules a potential navigation.
    """

    event = "Page.frameScheduledNavigation"

    def __init__(self, frameId: FrameId, delay: float, reason: str, url: str) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['FrameScheduledNavigationEvent']:
        if init is not None:
            return FrameScheduledNavigationEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['FrameScheduledNavigationEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FrameScheduledNavigationEvent(**it))
            return list_of_self
        else:
            return init


class FrameStartedLoadingEvent(BaseEvent):
    """
    Fired when frame has started loading.
    """

    event = "Page.frameStartedLoading"

    def __init__(self, frameId: FrameId) -> None:
        """
        :param frameId: Id of the frame that has started loading.
        :type frameId: str
        """
        super().__init__()
        self.frameId = frameId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['FrameStartedLoadingEvent']:
        if init is not None:
            return FrameStartedLoadingEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['FrameStartedLoadingEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FrameStartedLoadingEvent(**it))
            return list_of_self
        else:
            return init


class FrameStoppedLoadingEvent(BaseEvent):
    """
    Fired when frame has stopped loading.
    """

    event = "Page.frameStoppedLoading"

    def __init__(self, frameId: FrameId) -> None:
        """
        :param frameId: Id of the frame that has stopped loading.
        :type frameId: str
        """
        super().__init__()
        self.frameId = frameId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['FrameStoppedLoadingEvent']:
        if init is not None:
            return FrameStoppedLoadingEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['FrameStoppedLoadingEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FrameStoppedLoadingEvent(**it))
            return list_of_self
        else:
            return init


class InterstitialHiddenEvent(BaseEvent):
    """
    Fired when interstitial page was hidden
    """

    event = "Page.interstitialHidden"

    def __init__(self, ) -> None:
        super().__init__()

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['InterstitialHiddenEvent']:
        if init is not None:
            return InterstitialHiddenEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['InterstitialHiddenEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(InterstitialHiddenEvent(**it))
            return list_of_self
        else:
            return init


class InterstitialShownEvent(BaseEvent):
    """
    Fired when interstitial page was shown
    """

    event = "Page.interstitialShown"

    def __init__(self, ) -> None:
        super().__init__()

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['InterstitialShownEvent']:
        if init is not None:
            return InterstitialShownEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['InterstitialShownEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(InterstitialShownEvent(**it))
            return list_of_self
        else:
            return init


class JavascriptDialogClosedEvent(BaseEvent):
    """
    Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) has been closed.
    """

    event = "Page.javascriptDialogClosed"

    def __init__(self, result: bool, userInput: str) -> None:
        """
        :param result: Whether dialog was confirmed.
        :type result: bool
        :param userInput: User input in case of prompt.
        :type userInput: str
        """
        super().__init__()
        self.result = result
        self.userInput = userInput

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['JavascriptDialogClosedEvent']:
        if init is not None:
            return JavascriptDialogClosedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['JavascriptDialogClosedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(JavascriptDialogClosedEvent(**it))
            return list_of_self
        else:
            return init


class JavascriptDialogOpeningEvent(BaseEvent):
    """
    Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) is about to open.
    """

    event = "Page.javascriptDialogOpening"

    def __init__(self, url: str, message: str, type: DialogType, hasBrowserHandler: bool, defaultPrompt: Optional[str] = None) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['JavascriptDialogOpeningEvent']:
        if init is not None:
            return JavascriptDialogOpeningEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['JavascriptDialogOpeningEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(JavascriptDialogOpeningEvent(**it))
            return list_of_self
        else:
            return init


class LifecycleEventEvent(BaseEvent):
    """
    Fired for top level page lifecycle events such as navigation, load, paint, etc.
    """

    event = "Page.lifecycleEvent"

    def __init__(self, frameId: FrameId, loaderId: Network.LoaderId, name: str, timestamp: Network.MonotonicTime) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['LifecycleEventEvent']:
        if init is not None:
            return LifecycleEventEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['LifecycleEventEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LifecycleEventEvent(**it))
            return list_of_self
        else:
            return init


class LoadEventFiredEvent(BaseEvent):

    event = "Page.loadEventFired"

    def __init__(self, timestamp: Network.MonotonicTime) -> None:
        """
        :param timestamp: The timestamp
        :type timestamp: float
        """
        super().__init__()
        self.timestamp = timestamp

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['LoadEventFiredEvent']:
        if init is not None:
            return LoadEventFiredEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['LoadEventFiredEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LoadEventFiredEvent(**it))
            return list_of_self
        else:
            return init


class NavigatedWithinDocumentEvent(BaseEvent):
    """
    Fired when same-document navigation happens, e.g.
	due to history API usage or anchor navigation.
    """

    event = "Page.navigatedWithinDocument"

    def __init__(self, frameId: FrameId, url: str) -> None:
        """
        :param frameId: Id of the frame.
        :type frameId: str
        :param url: Frame's new url.
        :type url: str
        """
        super().__init__()
        self.frameId = frameId
        self.url = url

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['NavigatedWithinDocumentEvent']:
        if init is not None:
            return NavigatedWithinDocumentEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['NavigatedWithinDocumentEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(NavigatedWithinDocumentEvent(**it))
            return list_of_self
        else:
            return init


class ScreencastFrameEvent(BaseEvent):
    """
    Compressed image data requested by the `startScreencast`.
    """

    event = "Page.screencastFrame"

    def __init__(self, data: str, metadata: Union[ScreencastFrameMetadata, dict], sessionId: int) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ScreencastFrameEvent']:
        if init is not None:
            return ScreencastFrameEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ScreencastFrameEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ScreencastFrameEvent(**it))
            return list_of_self
        else:
            return init


class ScreencastVisibilityChangedEvent(BaseEvent):
    """
    Fired when the page with currently enabled screencast was shown or hidden `.
    """

    event = "Page.screencastVisibilityChanged"

    def __init__(self, visible: bool) -> None:
        """
        :param visible: True if the page is visible.
        :type visible: bool
        """
        super().__init__()
        self.visible = visible

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ScreencastVisibilityChangedEvent']:
        if init is not None:
            return ScreencastVisibilityChangedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ScreencastVisibilityChangedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ScreencastVisibilityChangedEvent(**it))
            return list_of_self
        else:
            return init


class WindowOpenEvent(BaseEvent):
    """
    Fired when a new window is going to be opened, via window.open(), link click, form submission, etc.
    """

    event = "Page.windowOpen"

    def __init__(self, url: str, windowName: str, windowFeatures: List[str], userGesture: bool) -> None:
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

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['WindowOpenEvent']:
        if init is not None:
            return WindowOpenEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['WindowOpenEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WindowOpenEvent(**it))
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

