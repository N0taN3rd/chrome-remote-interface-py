from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class DomContentEventFiredEvent(BaseEvent):

    event: str = "Page.domContentEventFired"

    def __init__(self) -> None:
        """
        :param Network.MonotonicTime timestamp: The timestamp
        :type timestamp: Network.MonotonicTime
        """
        super().__init__()


class FrameAttachedEvent(BaseEvent):
    """Fired when frame has been attached to its parent."""

    event: str = "Page.frameAttached"

    def __init__(self) -> None:
        """
        :param FrameId frameId: Id of the frame that has been attached.
        :type frameId: FrameId
        :param FrameId parentFrameId: Parent frame identifier.
        :type parentFrameId: FrameId
        :param Runtime.StackTrace stack: JavaScript stack trace of when frame was attached, only set if frame initiated from script.
        :type stack: Runtime.StackTrace
        """
        super().__init__()


class FrameClearedScheduledNavigationEvent(BaseEvent):
    """Fired when frame no longer has a scheduled navigation."""

    event: str = "Page.frameClearedScheduledNavigation"

    def __init__(self) -> None:
        """
        :param FrameId frameId: Id of the frame that has cleared its scheduled navigation.
        :type frameId: FrameId
        """
        super().__init__()


class FrameDetachedEvent(BaseEvent):
    """Fired when frame has been detached from its parent."""

    event: str = "Page.frameDetached"

    def __init__(self) -> None:
        """
        :param FrameId frameId: Id of the frame that has been detached.
        :type frameId: FrameId
        """
        super().__init__()


class FrameNavigatedEvent(BaseEvent):
    """Fired once navigation of the frame has completed.
	Frame is now associated with the new loader."""

    event: str = "Page.frameNavigated"

    def __init__(self) -> None:
        """
        :param Frame frame: Frame object.
        :type frame: Frame
        """
        super().__init__()


class FrameResizedEvent(BaseEvent):

    event: str = "Page.frameResized"

    def __init__(self) -> None:
        super().__init__()


class FrameScheduledNavigationEvent(BaseEvent):
    """Fired when frame schedules a potential navigation."""

    event: str = "Page.frameScheduledNavigation"

    def __init__(self) -> None:
        """
        :param FrameId frameId: Id of the frame that has scheduled a navigation.
        :type frameId: FrameId
        :param float delay: Delay (in seconds) until the navigation is scheduled to begin. The navigation is not guaranteed to start.
        :type delay: float
        :param str reason: The reason for the navigation.
        :type reason: str
        :param str url: The destination URL for the scheduled navigation.
        :type url: str
        """
        super().__init__()


class FrameStartedLoadingEvent(BaseEvent):
    """Fired when frame has started loading."""

    event: str = "Page.frameStartedLoading"

    def __init__(self) -> None:
        """
        :param FrameId frameId: Id of the frame that has started loading.
        :type frameId: FrameId
        """
        super().__init__()


class FrameStoppedLoadingEvent(BaseEvent):
    """Fired when frame has stopped loading."""

    event: str = "Page.frameStoppedLoading"

    def __init__(self) -> None:
        """
        :param FrameId frameId: Id of the frame that has stopped loading.
        :type frameId: FrameId
        """
        super().__init__()


class InterstitialHiddenEvent(BaseEvent):
    """Fired when interstitial page was hidden"""

    event: str = "Page.interstitialHidden"

    def __init__(self) -> None:
        super().__init__()


class InterstitialShownEvent(BaseEvent):
    """Fired when interstitial page was shown"""

    event: str = "Page.interstitialShown"

    def __init__(self) -> None:
        super().__init__()


class JavascriptDialogClosedEvent(BaseEvent):
    """Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) has been closed."""

    event: str = "Page.javascriptDialogClosed"

    def __init__(self) -> None:
        """
        :param bool result: Whether dialog was confirmed.
        :type result: bool
        :param str userInput: User input in case of prompt.
        :type userInput: str
        """
        super().__init__()


class JavascriptDialogOpeningEvent(BaseEvent):
    """Fired when a JavaScript initiated dialog (alert, confirm, prompt, or onbeforeunload) is about to open."""

    event: str = "Page.javascriptDialogOpening"

    def __init__(self) -> None:
        """
        :param str url: Frame url.
        :type url: str
        :param str message: Message that will be displayed by the dialog.
        :type message: str
        :param DialogType type: Dialog type.
        :type type: DialogType
        :param bool hasBrowserHandler: True iff browser is capable showing or acting on the given dialog. When browser has no dialog handler for given target, calling alert while Page domain is engaged will stall the page execution. Execution can be resumed via calling Page.handleJavaScriptDialog.
        :type hasBrowserHandler: bool
        :param str defaultPrompt: Default dialog prompt.
        :type defaultPrompt: str
        """
        super().__init__()


class LifecycleEventEvent(BaseEvent):
    """Fired for top level page lifecycle events such as navigation, load, paint, etc."""

    event: str = "Page.lifecycleEvent"

    def __init__(self) -> None:
        """
        :param FrameId frameId: Id of the frame.
        :type frameId: FrameId
        :param Network.LoaderId loaderId: Loader identifier. Empty string if the request is fetched from worker.
        :type loaderId: Network.LoaderId
        :param str name: The name
        :type name: str
        :param Network.MonotonicTime timestamp: The timestamp
        :type timestamp: Network.MonotonicTime
        """
        super().__init__()


class LoadEventFiredEvent(BaseEvent):

    event: str = "Page.loadEventFired"

    def __init__(self) -> None:
        """
        :param Network.MonotonicTime timestamp: The timestamp
        :type timestamp: Network.MonotonicTime
        """
        super().__init__()


class NavigatedWithinDocumentEvent(BaseEvent):
    """Fired when same-document navigation happens, e.g.
	due to history API usage or anchor navigation."""

    event: str = "Page.navigatedWithinDocument"

    def __init__(self) -> None:
        """
        :param FrameId frameId: Id of the frame.
        :type frameId: FrameId
        :param str url: Frame's new url.
        :type url: str
        """
        super().__init__()


class ScreencastFrameEvent(BaseEvent):
    """Compressed image data requested by the `startScreencast`."""

    event: str = "Page.screencastFrame"

    def __init__(self) -> None:
        """
        :param str data: Base64-encoded compressed image.
        :type data: str
        :param ScreencastFrameMetadata metadata: Screencast frame metadata.
        :type metadata: ScreencastFrameMetadata
        :param int sessionId: Frame number.
        :type sessionId: int
        """
        super().__init__()


class ScreencastVisibilityChangedEvent(BaseEvent):
    """Fired when the page with currently enabled screencast was shown or hidden `."""

    event: str = "Page.screencastVisibilityChanged"

    def __init__(self) -> None:
        """
        :param bool visible: True if the page is visible.
        :type visible: bool
        """
        super().__init__()


class WindowOpenEvent(BaseEvent):
    """Fired when a new window is going to be opened, via window.open(), link click, form submission, etc."""

    event: str = "Page.windowOpen"

    def __init__(self) -> None:
        """
        :param str url: The URL for the new window.
        :type url: str
        :param str windowName: Window name.
        :type windowName: str
        :param array windowFeatures: An array of enabled window features.
        :type windowFeatures: array
        :param bool userGesture: Whether or not it was triggered by user gesture.
        :type userGesture: bool
        """
        super().__init__()


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

