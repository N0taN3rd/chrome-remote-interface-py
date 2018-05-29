from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent
from cripy.protocol.runtime import types as Runtime
from cripy.protocol.network import types as Network
from cripy.protocol.page.types import (
    DialogType,
    Frame,
    ScreencastFrameMetadata,
    FrameId,
)


class DomContentEventFiredEvent(BaseEvent):

    event: str = "Page.domContentEventFired"

    def __init__(self, timestamp: Network.MonotonicTime) -> None:
        """
        :param timestamp: The timestamp
        :type timestamp: Network.MonotonicTime
        """
        super().__init__()
        self.timestamp: Network.MonotonicTime = timestamp


class FrameAttachedEvent(BaseEvent):
    """Fired when frame has been attached to its parent."""

    event: str = "Page.frameAttached"

    def __init__(
        self,
        frameId: FrameId,
        parentFrameId: FrameId,
        stack: Optional[Runtime.StackTrace] = None,
    ) -> None:
        """
        :param frameId: Id of the frame that has been attached.
        :type frameId: FrameId
        :param parentFrameId: Parent frame identifier.
        :type parentFrameId: FrameId
        :param stack: JavaScript stack trace of when frame was attached, only set if frame initiated from script.
        :type stack: Runtime.StackTrace
        """
        super().__init__()
        self.frameId: FrameId = frameId
        self.parentFrameId: FrameId = parentFrameId
        self.stack: Optional[Runtime.StackTrace] = stack


class FrameClearedScheduledNavigationEvent(BaseEvent):
    """Fired when frame no longer has a scheduled navigation."""

    event: str = "Page.frameClearedScheduledNavigation"

    def __init__(self, frameId: FrameId) -> None:
        """
        :param frameId: Id of the frame that has cleared its scheduled navigation.
        :type frameId: FrameId
        """
        super().__init__()
        self.frameId: FrameId = frameId


class FrameDetachedEvent(BaseEvent):
    """Fired when frame has been detached from its parent."""

    event: str = "Page.frameDetached"

    def __init__(self, frameId: FrameId) -> None:
        """
        :param frameId: Id of the frame that has been detached.
        :type frameId: FrameId
        """
        super().__init__()
        self.frameId: FrameId = frameId


class FrameNavigatedEvent(BaseEvent):
    """Fired once navigation of the frame has completed.
	Frame is now associated with the new loader."""

    event: str = "Page.frameNavigated"

    def __init__(self, frame: Frame) -> None:
        """
        :param frame: Frame object.
        :type frame: Frame
        """
        super().__init__()
        self.frame: Frame = frame


class FrameResizedEvent(BaseEvent):

    event: str = "Page.frameResized"

    def __init__(self,) -> None:
        super().__init__()


class FrameScheduledNavigationEvent(BaseEvent):
    """Fired when frame schedules a potential navigation."""

    event: str = "Page.frameScheduledNavigation"

    def __init__(self, frameId: FrameId, delay: float, reason: str, url: str) -> None:
        """
        :param frameId: Id of the frame that has scheduled a navigation.
        :type frameId: FrameId
        :param delay: Delay (in seconds) until the navigation is scheduled to begin. The navigation is not guaranteed to start.
        :type delay: float
        :param reason: The reason for the navigation.
        :type reason: str
        :param url: The destination URL for the scheduled navigation.
        :type url: str
        """
        super().__init__()
        self.frameId: FrameId = frameId
        self.delay: float = delay
        self.reason: str = reason
        self.url: str = url


class FrameStartedLoadingEvent(BaseEvent):
    """Fired when frame has started loading."""

    event: str = "Page.frameStartedLoading"

    def __init__(self, frameId: FrameId) -> None:
        """
        :param frameId: Id of the frame that has started loading.
        :type frameId: FrameId
        """
        super().__init__()
        self.frameId: FrameId = frameId


class FrameStoppedLoadingEvent(BaseEvent):
    """Fired when frame has stopped loading."""

    event: str = "Page.frameStoppedLoading"

    def __init__(self, frameId: FrameId) -> None:
        """
        :param frameId: Id of the frame that has stopped loading.
        :type frameId: FrameId
        """
        super().__init__()
        self.frameId: FrameId = frameId


class InterstitialHiddenEvent(BaseEvent):
    """Fired when interstitial page was hidden"""

    event: str = "Page.interstitialHidden"

    def __init__(self,) -> None:
        super().__init__()


class InterstitialShownEvent(BaseEvent):
    """Fired when interstitial page was shown"""

    event: str = "Page.interstitialShown"

    def __init__(self,) -> None:
        super().__init__()


class JavascriptDialogClosedEvent(BaseEvent):
    """Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) has been closed."""

    event: str = "Page.javascriptDialogClosed"

    def __init__(self, result: bool, userInput: str) -> None:
        """
        :param result: Whether dialog was confirmed.
        :type result: bool
        :param userInput: User input in case of prompt.
        :type userInput: str
        """
        super().__init__()
        self.result: bool = result
        self.userInput: str = userInput


class JavascriptDialogOpeningEvent(BaseEvent):
    """Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) is about to open."""

    event: str = "Page.javascriptDialogOpening"

    def __init__(
        self,
        url: str,
        message: str,
        type: DialogType,
        hasBrowserHandler: bool,
        defaultPrompt: Optional[str] = None,
    ) -> None:
        """
        :param url: Frame url.
        :type url: str
        :param message: Message that will be displayed by the dialog.
        :type message: str
        :param type: Dialog type.
        :type type: DialogType
        :param hasBrowserHandler: True iff browser is capable showing or acting on the given dialog. When browser has no dialog handler for given target, calling alert while Page domain is engaged will stall the page execution. Execution can be resumed via calling Page.handleJavaScriptDialog.
        :type hasBrowserHandler: bool
        :param defaultPrompt: Default dialog prompt.
        :type defaultPrompt: str
        """
        super().__init__()
        self.url: str = url
        self.message: str = message
        self.type: DialogType = type
        self.hasBrowserHandler: bool = hasBrowserHandler
        self.defaultPrompt: Optional[str] = defaultPrompt


class LifecycleEventEvent(BaseEvent):
    """Fired for top level page lifecycle events such as navigation, load, paint, etc."""

    event: str = "Page.lifecycleEvent"

    def __init__(
        self,
        frameId: FrameId,
        loaderId: Network.LoaderId,
        name: str,
        timestamp: Network.MonotonicTime,
    ) -> None:
        """
        :param frameId: Id of the frame.
        :type frameId: FrameId
        :param loaderId: Loader identifier. Empty string if the request is fetched from worker.
        :type loaderId: Network.LoaderId
        :param name: The name
        :type name: str
        :param timestamp: The timestamp
        :type timestamp: Network.MonotonicTime
        """
        super().__init__()
        self.frameId: FrameId = frameId
        self.loaderId: Network.LoaderId = loaderId
        self.name: str = name
        self.timestamp: Network.MonotonicTime = timestamp


class LoadEventFiredEvent(BaseEvent):

    event: str = "Page.loadEventFired"

    def __init__(self, timestamp: Network.MonotonicTime) -> None:
        """
        :param timestamp: The timestamp
        :type timestamp: Network.MonotonicTime
        """
        super().__init__()
        self.timestamp: Network.MonotonicTime = timestamp


class NavigatedWithinDocumentEvent(BaseEvent):
    """Fired when same-document navigation happens, e.g.
	due to history API usage or anchor navigation."""

    event: str = "Page.navigatedWithinDocument"

    def __init__(self, frameId: FrameId, url: str) -> None:
        """
        :param frameId: Id of the frame.
        :type frameId: FrameId
        :param url: Frame's new url.
        :type url: str
        """
        super().__init__()
        self.frameId: FrameId = frameId
        self.url: str = url


class ScreencastFrameEvent(BaseEvent):
    """Compressed image data requested by the `startScreencast`."""

    event: str = "Page.screencastFrame"

    def __init__(
        self, data: str, metadata: ScreencastFrameMetadata, sessionId: int
    ) -> None:
        """
        :param data: Base64-encoded compressed image.
        :type data: str
        :param metadata: Screencast frame metadata.
        :type metadata: ScreencastFrameMetadata
        :param sessionId: Frame number.
        :type sessionId: int
        """
        super().__init__()
        self.data: str = data
        self.metadata: ScreencastFrameMetadata = metadata
        self.sessionId: int = sessionId


class ScreencastVisibilityChangedEvent(BaseEvent):
    """Fired when the page with currently enabled screencast was shown or hidden `."""

    event: str = "Page.screencastVisibilityChanged"

    def __init__(self, visible: bool) -> None:
        """
        :param visible: True if the page is visible.
        :type visible: bool
        """
        super().__init__()
        self.visible: bool = visible


class WindowOpenEvent(BaseEvent):
    """Fired when a new window is going to be opened, via window.open(), link click, form submission, etc."""

    event: str = "Page.windowOpen"

    def __init__(
        self, url: str, windowName: str, windowFeatures: List[str], userGesture: bool
    ) -> None:
        """
        :param url: The URL for the new window.
        :type url: str
        :param windowName: Window name.
        :type windowName: str
        :param windowFeatures: An array of enabled window features.
        :type windowFeatures: array
        :param userGesture: Whether or not it was triggered by user gesture.
        :type userGesture: bool
        """
        super().__init__()
        self.url: str = url
        self.windowName: str = windowName
        self.windowFeatures: List[str] = windowFeatures
        self.userGesture: bool = userGesture


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
