from typing import Any, List, Optional, Union
from collections import namedtuple
from cripy.async.protocol.runtime import types as Runtime
from cripy.async.protocol.network import types as Network
from cripy.async.protocol.page.types import *

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
    "PAGE_EVENTS_TO_CLASS",
    "PAGE_EVENTS_NS"
]

class DomContentEventFiredEvent(object):

    event = "Page.domContentEventFired"

    __slots__ = ["timestamp"]

    def __init__(self, timestamp: float) -> None:
        """
        Create a new instance of DomContentEventFiredEvent

        :param timestamp: The timestamp
        :type timestamp: float
        """
        super().__init__()
        self.timestamp = timestamp

    def __repr__(self) -> str:
        repr_args = []
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        return "DomContentEventFiredEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['DomContentEventFiredEvent', dict]]:
        """
        Safely create DomContentEventFiredEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of DomContentEventFiredEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of DomContentEventFiredEvent if creation did not fail
        :rtype: Optional[Union[dict, DomContentEventFiredEvent]]
        """
        if init is not None:
            try:
                ourselves = DomContentEventFiredEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['DomContentEventFiredEvent', dict]]]:
        """
        Safely create a new list DomContentEventFiredEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list DomContentEventFiredEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of DomContentEventFiredEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, DomContentEventFiredEvent]]]
        """
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

    __slots__ = ["frameId", "parentFrameId", "stack"]

    def __init__(self, frameId: str, parentFrameId: str, stack: Optional[Union[Runtime.StackTrace, dict]] = None) -> None:
        """
        Create a new instance of FrameAttachedEvent

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

    def __repr__(self) -> str:
        repr_args = []
        if self.frameId is not None:
            repr_args.append("frameId={!r}".format(self.frameId))
        if self.parentFrameId is not None:
            repr_args.append("parentFrameId={!r}".format(self.parentFrameId))
        if self.stack is not None:
            repr_args.append("stack={!r}".format(self.stack))
        return "FrameAttachedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['FrameAttachedEvent', dict]]:
        """
        Safely create FrameAttachedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of FrameAttachedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of FrameAttachedEvent if creation did not fail
        :rtype: Optional[Union[dict, FrameAttachedEvent]]
        """
        if init is not None:
            try:
                ourselves = FrameAttachedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['FrameAttachedEvent', dict]]]:
        """
        Safely create a new list FrameAttachedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list FrameAttachedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of FrameAttachedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, FrameAttachedEvent]]]
        """
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

    __slots__ = ["frameId"]

    def __init__(self, frameId: str) -> None:
        """
        Create a new instance of FrameClearedScheduledNavigationEvent

        :param frameId: Id of the frame that has cleared its scheduled navigation.
        :type frameId: str
        """
        super().__init__()
        self.frameId = frameId

    def __repr__(self) -> str:
        repr_args = []
        if self.frameId is not None:
            repr_args.append("frameId={!r}".format(self.frameId))
        return "FrameClearedScheduledNavigationEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['FrameClearedScheduledNavigationEvent', dict]]:
        """
        Safely create FrameClearedScheduledNavigationEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of FrameClearedScheduledNavigationEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of FrameClearedScheduledNavigationEvent if creation did not fail
        :rtype: Optional[Union[dict, FrameClearedScheduledNavigationEvent]]
        """
        if init is not None:
            try:
                ourselves = FrameClearedScheduledNavigationEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['FrameClearedScheduledNavigationEvent', dict]]]:
        """
        Safely create a new list FrameClearedScheduledNavigationEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list FrameClearedScheduledNavigationEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of FrameClearedScheduledNavigationEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, FrameClearedScheduledNavigationEvent]]]
        """
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

    __slots__ = ["frameId"]

    def __init__(self, frameId: str) -> None:
        """
        Create a new instance of FrameDetachedEvent

        :param frameId: Id of the frame that has been detached.
        :type frameId: str
        """
        super().__init__()
        self.frameId = frameId

    def __repr__(self) -> str:
        repr_args = []
        if self.frameId is not None:
            repr_args.append("frameId={!r}".format(self.frameId))
        return "FrameDetachedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['FrameDetachedEvent', dict]]:
        """
        Safely create FrameDetachedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of FrameDetachedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of FrameDetachedEvent if creation did not fail
        :rtype: Optional[Union[dict, FrameDetachedEvent]]
        """
        if init is not None:
            try:
                ourselves = FrameDetachedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['FrameDetachedEvent', dict]]]:
        """
        Safely create a new list FrameDetachedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list FrameDetachedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of FrameDetachedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, FrameDetachedEvent]]]
        """
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

    __slots__ = ["frame"]

    def __init__(self, frame: Union[Frame, dict]) -> None:
        """
        Create a new instance of FrameNavigatedEvent

        :param frame: Frame object.
        :type frame: dict
        """
        super().__init__()
        self.frame = Frame.safe_create(frame)

    def __repr__(self) -> str:
        repr_args = []
        if self.frame is not None:
            repr_args.append("frame={!r}".format(self.frame))
        return "FrameNavigatedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['FrameNavigatedEvent', dict]]:
        """
        Safely create FrameNavigatedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of FrameNavigatedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of FrameNavigatedEvent if creation did not fail
        :rtype: Optional[Union[dict, FrameNavigatedEvent]]
        """
        if init is not None:
            try:
                ourselves = FrameNavigatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['FrameNavigatedEvent', dict]]]:
        """
        Safely create a new list FrameNavigatedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list FrameNavigatedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of FrameNavigatedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, FrameNavigatedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FrameNavigatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class FrameResizedEvent(dict):

    event = "Page.frameResized"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return "FrameResizedEvent(dict)"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['FrameResizedEvent', dict]]:
        """
        Safely create FrameResizedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of FrameResizedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of FrameResizedEvent if creation did not fail
        :rtype: Optional[Union[dict, FrameResizedEvent]]
        """
        if init is not None:
            try:
                ourselves = FrameResizedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['FrameResizedEvent', dict]]]:
        """
        Safely create a new list FrameResizedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list FrameResizedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of FrameResizedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, FrameResizedEvent]]]
        """
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

    __slots__ = ["frameId", "delay", "reason", "url"]

    def __init__(self, frameId: str, delay: float, reason: str, url: str) -> None:
        """
        Create a new instance of FrameScheduledNavigationEvent

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

    def __repr__(self) -> str:
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
    def safe_create(init: Optional[dict]) -> Optional[Union['FrameScheduledNavigationEvent', dict]]:
        """
        Safely create FrameScheduledNavigationEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of FrameScheduledNavigationEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of FrameScheduledNavigationEvent if creation did not fail
        :rtype: Optional[Union[dict, FrameScheduledNavigationEvent]]
        """
        if init is not None:
            try:
                ourselves = FrameScheduledNavigationEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['FrameScheduledNavigationEvent', dict]]]:
        """
        Safely create a new list FrameScheduledNavigationEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list FrameScheduledNavigationEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of FrameScheduledNavigationEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, FrameScheduledNavigationEvent]]]
        """
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

    __slots__ = ["frameId"]

    def __init__(self, frameId: str) -> None:
        """
        Create a new instance of FrameStartedLoadingEvent

        :param frameId: Id of the frame that has started loading.
        :type frameId: str
        """
        super().__init__()
        self.frameId = frameId

    def __repr__(self) -> str:
        repr_args = []
        if self.frameId is not None:
            repr_args.append("frameId={!r}".format(self.frameId))
        return "FrameStartedLoadingEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['FrameStartedLoadingEvent', dict]]:
        """
        Safely create FrameStartedLoadingEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of FrameStartedLoadingEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of FrameStartedLoadingEvent if creation did not fail
        :rtype: Optional[Union[dict, FrameStartedLoadingEvent]]
        """
        if init is not None:
            try:
                ourselves = FrameStartedLoadingEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['FrameStartedLoadingEvent', dict]]]:
        """
        Safely create a new list FrameStartedLoadingEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list FrameStartedLoadingEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of FrameStartedLoadingEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, FrameStartedLoadingEvent]]]
        """
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

    __slots__ = ["frameId"]

    def __init__(self, frameId: str) -> None:
        """
        Create a new instance of FrameStoppedLoadingEvent

        :param frameId: Id of the frame that has stopped loading.
        :type frameId: str
        """
        super().__init__()
        self.frameId = frameId

    def __repr__(self) -> str:
        repr_args = []
        if self.frameId is not None:
            repr_args.append("frameId={!r}".format(self.frameId))
        return "FrameStoppedLoadingEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['FrameStoppedLoadingEvent', dict]]:
        """
        Safely create FrameStoppedLoadingEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of FrameStoppedLoadingEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of FrameStoppedLoadingEvent if creation did not fail
        :rtype: Optional[Union[dict, FrameStoppedLoadingEvent]]
        """
        if init is not None:
            try:
                ourselves = FrameStoppedLoadingEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['FrameStoppedLoadingEvent', dict]]]:
        """
        Safely create a new list FrameStoppedLoadingEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list FrameStoppedLoadingEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of FrameStoppedLoadingEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, FrameStoppedLoadingEvent]]]
        """
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

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return "InterstitialHiddenEvent(dict)"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['InterstitialHiddenEvent', dict]]:
        """
        Safely create InterstitialHiddenEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of InterstitialHiddenEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of InterstitialHiddenEvent if creation did not fail
        :rtype: Optional[Union[dict, InterstitialHiddenEvent]]
        """
        if init is not None:
            try:
                ourselves = InterstitialHiddenEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['InterstitialHiddenEvent', dict]]]:
        """
        Safely create a new list InterstitialHiddenEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list InterstitialHiddenEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of InterstitialHiddenEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, InterstitialHiddenEvent]]]
        """
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

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return "InterstitialShownEvent(dict)"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['InterstitialShownEvent', dict]]:
        """
        Safely create InterstitialShownEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of InterstitialShownEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of InterstitialShownEvent if creation did not fail
        :rtype: Optional[Union[dict, InterstitialShownEvent]]
        """
        if init is not None:
            try:
                ourselves = InterstitialShownEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['InterstitialShownEvent', dict]]]:
        """
        Safely create a new list InterstitialShownEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list InterstitialShownEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of InterstitialShownEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, InterstitialShownEvent]]]
        """
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

    __slots__ = ["result", "userInput"]

    def __init__(self, result: bool, userInput: str) -> None:
        """
        Create a new instance of JavascriptDialogClosedEvent

        :param result: Whether dialog was confirmed.
        :type result: bool
        :param userInput: User input in case of prompt.
        :type userInput: str
        """
        super().__init__()
        self.result = result
        self.userInput = userInput

    def __repr__(self) -> str:
        repr_args = []
        if self.result is not None:
            repr_args.append("result={!r}".format(self.result))
        if self.userInput is not None:
            repr_args.append("userInput={!r}".format(self.userInput))
        return "JavascriptDialogClosedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['JavascriptDialogClosedEvent', dict]]:
        """
        Safely create JavascriptDialogClosedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of JavascriptDialogClosedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of JavascriptDialogClosedEvent if creation did not fail
        :rtype: Optional[Union[dict, JavascriptDialogClosedEvent]]
        """
        if init is not None:
            try:
                ourselves = JavascriptDialogClosedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['JavascriptDialogClosedEvent', dict]]]:
        """
        Safely create a new list JavascriptDialogClosedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list JavascriptDialogClosedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of JavascriptDialogClosedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, JavascriptDialogClosedEvent]]]
        """
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

    __slots__ = ["url", "message", "type", "hasBrowserHandler", "defaultPrompt"]

    def __init__(self, url: str, message: str, type: str, hasBrowserHandler: bool, defaultPrompt: Optional[str] = None) -> None:
        """
        Create a new instance of JavascriptDialogOpeningEvent

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

    def __repr__(self) -> str:
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
    def safe_create(init: Optional[dict]) -> Optional[Union['JavascriptDialogOpeningEvent', dict]]:
        """
        Safely create JavascriptDialogOpeningEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of JavascriptDialogOpeningEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of JavascriptDialogOpeningEvent if creation did not fail
        :rtype: Optional[Union[dict, JavascriptDialogOpeningEvent]]
        """
        if init is not None:
            try:
                ourselves = JavascriptDialogOpeningEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['JavascriptDialogOpeningEvent', dict]]]:
        """
        Safely create a new list JavascriptDialogOpeningEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list JavascriptDialogOpeningEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of JavascriptDialogOpeningEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, JavascriptDialogOpeningEvent]]]
        """
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

    __slots__ = ["frameId", "loaderId", "name", "timestamp"]

    def __init__(self, frameId: str, loaderId: str, name: str, timestamp: float) -> None:
        """
        Create a new instance of LifecycleEventEvent

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

    def __repr__(self) -> str:
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
    def safe_create(init: Optional[dict]) -> Optional[Union['LifecycleEventEvent', dict]]:
        """
        Safely create LifecycleEventEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of LifecycleEventEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of LifecycleEventEvent if creation did not fail
        :rtype: Optional[Union[dict, LifecycleEventEvent]]
        """
        if init is not None:
            try:
                ourselves = LifecycleEventEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['LifecycleEventEvent', dict]]]:
        """
        Safely create a new list LifecycleEventEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list LifecycleEventEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of LifecycleEventEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, LifecycleEventEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LifecycleEventEvent.safe_create(it))
            return list_of_self
        else:
            return init


class LoadEventFiredEvent(object):

    event = "Page.loadEventFired"

    __slots__ = ["timestamp"]

    def __init__(self, timestamp: float) -> None:
        """
        Create a new instance of LoadEventFiredEvent

        :param timestamp: The timestamp
        :type timestamp: float
        """
        super().__init__()
        self.timestamp = timestamp

    def __repr__(self) -> str:
        repr_args = []
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        return "LoadEventFiredEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['LoadEventFiredEvent', dict]]:
        """
        Safely create LoadEventFiredEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of LoadEventFiredEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of LoadEventFiredEvent if creation did not fail
        :rtype: Optional[Union[dict, LoadEventFiredEvent]]
        """
        if init is not None:
            try:
                ourselves = LoadEventFiredEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['LoadEventFiredEvent', dict]]]:
        """
        Safely create a new list LoadEventFiredEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list LoadEventFiredEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of LoadEventFiredEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, LoadEventFiredEvent]]]
        """
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

    __slots__ = ["frameId", "url"]

    def __init__(self, frameId: str, url: str) -> None:
        """
        Create a new instance of NavigatedWithinDocumentEvent

        :param frameId: Id of the frame.
        :type frameId: str
        :param url: Frame's new url.
        :type url: str
        """
        super().__init__()
        self.frameId = frameId
        self.url = url

    def __repr__(self) -> str:
        repr_args = []
        if self.frameId is not None:
            repr_args.append("frameId={!r}".format(self.frameId))
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        return "NavigatedWithinDocumentEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['NavigatedWithinDocumentEvent', dict]]:
        """
        Safely create NavigatedWithinDocumentEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of NavigatedWithinDocumentEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of NavigatedWithinDocumentEvent if creation did not fail
        :rtype: Optional[Union[dict, NavigatedWithinDocumentEvent]]
        """
        if init is not None:
            try:
                ourselves = NavigatedWithinDocumentEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['NavigatedWithinDocumentEvent', dict]]]:
        """
        Safely create a new list NavigatedWithinDocumentEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list NavigatedWithinDocumentEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of NavigatedWithinDocumentEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, NavigatedWithinDocumentEvent]]]
        """
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

    __slots__ = ["data", "metadata", "sessionId"]

    def __init__(self, data: str, metadata: Union[ScreencastFrameMetadata, dict], sessionId: int) -> None:
        """
        Create a new instance of ScreencastFrameEvent

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

    def __repr__(self) -> str:
        repr_args = []
        if self.data is not None:
            repr_args.append("data={!r}".format(self.data))
        if self.metadata is not None:
            repr_args.append("metadata={!r}".format(self.metadata))
        if self.sessionId is not None:
            repr_args.append("sessionId={!r}".format(self.sessionId))
        return "ScreencastFrameEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ScreencastFrameEvent', dict]]:
        """
        Safely create ScreencastFrameEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ScreencastFrameEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ScreencastFrameEvent if creation did not fail
        :rtype: Optional[Union[dict, ScreencastFrameEvent]]
        """
        if init is not None:
            try:
                ourselves = ScreencastFrameEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ScreencastFrameEvent', dict]]]:
        """
        Safely create a new list ScreencastFrameEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ScreencastFrameEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ScreencastFrameEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, ScreencastFrameEvent]]]
        """
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

    __slots__ = ["visible"]

    def __init__(self, visible: bool) -> None:
        """
        Create a new instance of ScreencastVisibilityChangedEvent

        :param visible: True if the page is visible.
        :type visible: bool
        """
        super().__init__()
        self.visible = visible

    def __repr__(self) -> str:
        repr_args = []
        if self.visible is not None:
            repr_args.append("visible={!r}".format(self.visible))
        return "ScreencastVisibilityChangedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ScreencastVisibilityChangedEvent', dict]]:
        """
        Safely create ScreencastVisibilityChangedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ScreencastVisibilityChangedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ScreencastVisibilityChangedEvent if creation did not fail
        :rtype: Optional[Union[dict, ScreencastVisibilityChangedEvent]]
        """
        if init is not None:
            try:
                ourselves = ScreencastVisibilityChangedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ScreencastVisibilityChangedEvent', dict]]]:
        """
        Safely create a new list ScreencastVisibilityChangedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ScreencastVisibilityChangedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ScreencastVisibilityChangedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, ScreencastVisibilityChangedEvent]]]
        """
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

    __slots__ = ["url", "windowName", "windowFeatures", "userGesture"]

    def __init__(self, url: str, windowName: str, windowFeatures: List[str], userGesture: bool) -> None:
        """
        Create a new instance of WindowOpenEvent

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

    def __repr__(self) -> str:
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
    def safe_create(init: Optional[dict]) -> Optional[Union['WindowOpenEvent', dict]]:
        """
        Safely create WindowOpenEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of WindowOpenEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of WindowOpenEvent if creation did not fail
        :rtype: Optional[Union[dict, WindowOpenEvent]]
        """
        if init is not None:
            try:
                ourselves = WindowOpenEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['WindowOpenEvent', dict]]]:
        """
        Safely create a new list WindowOpenEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list WindowOpenEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of WindowOpenEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, WindowOpenEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(WindowOpenEvent.safe_create(it))
            return list_of_self
        else:
            return init


PAGE_EVENTS_TO_CLASS = {
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

PageNS = namedtuple("PageNS", ["DomContentEventFired", "FrameAttached", "FrameClearedScheduledNavigation", "FrameDetached", "FrameNavigated", "FrameResized", "FrameScheduledNavigation", "FrameStartedLoading", "FrameStoppedLoading", "InterstitialHidden", "InterstitialShown", "JavascriptDialogClosed", "JavascriptDialogOpening", "LifecycleEvent", "LoadEventFired", "NavigatedWithinDocument", "ScreencastFrame", "ScreencastVisibilityChanged", "WindowOpen"])

PAGE_EVENTS_NS = PageNS(
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
