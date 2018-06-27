from typing import Any, List, Optional, Union
from collections import namedtuple
from cripy.asyncio.protocol.animation.types import *

__all__ = [
    "AnimationCanceledEvent",
    "AnimationCreatedEvent",
    "AnimationStartedEvent",
    "ANIMATION_EVENTS_TO_CLASS",
    "ANIMATION_EVENTS_NS"
]


class AnimationCanceledEvent(object):
    """
    Event for when an animation has been cancelled.
    """


    __slots__ = ["id"]

    def __init__(self, id: str) -> None:
        """
        Create a new instance of AnimationCanceledEvent

        :param id: Id of the animation that was cancelled.
        :type id: str
        """
        super().__init__()
        self.id = id

    def __repr__(self) -> str:
        repr_args = []
        if self.id is not None:
            repr_args.append("id={!r}".format(self.id))
        return "AnimationCanceledEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['AnimationCanceledEvent', dict]]:
        """
        Safely create AnimationCanceledEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of AnimationCanceledEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of AnimationCanceledEvent if creation did not fail
        :rtype: Optional[Union[dict, AnimationCanceledEvent]]
        """
        if init is not None:
            try:
                ourselves = AnimationCanceledEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['AnimationCanceledEvent', dict]]]:
        """
        Safely create a new list AnimationCanceledEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list AnimationCanceledEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of AnimationCanceledEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, AnimationCanceledEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AnimationCanceledEvent.safe_create(it))
            return list_of_self
        else:
            return init


class AnimationCreatedEvent(object):
    """
    Event for each animation that has been created.
    """


    __slots__ = ["id"]

    def __init__(self, id: str) -> None:
        """
        Create a new instance of AnimationCreatedEvent

        :param id: Id of the animation that was created.
        :type id: str
        """
        super().__init__()
        self.id = id

    def __repr__(self) -> str:
        repr_args = []
        if self.id is not None:
            repr_args.append("id={!r}".format(self.id))
        return "AnimationCreatedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['AnimationCreatedEvent', dict]]:
        """
        Safely create AnimationCreatedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of AnimationCreatedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of AnimationCreatedEvent if creation did not fail
        :rtype: Optional[Union[dict, AnimationCreatedEvent]]
        """
        if init is not None:
            try:
                ourselves = AnimationCreatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['AnimationCreatedEvent', dict]]]:
        """
        Safely create a new list AnimationCreatedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list AnimationCreatedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of AnimationCreatedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, AnimationCreatedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AnimationCreatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class AnimationStartedEvent(object):
    """
    Event for animation that has been started.
    """


    __slots__ = ["animation"]

    def __init__(self, animation: Union[AnimationT, dict]) -> None:
        """
        Create a new instance of AnimationStartedEvent

        :param animation: Animation that was started.
        :type animation: dict
        """
        super().__init__()
        self.animation = AnimationT.safe_create(animation)

    def __repr__(self) -> str:
        repr_args = []
        if self.animation is not None:
            repr_args.append("animation={!r}".format(self.animation))
        return "AnimationStartedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['AnimationStartedEvent', dict]]:
        """
        Safely create AnimationStartedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of AnimationStartedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of AnimationStartedEvent if creation did not fail
        :rtype: Optional[Union[dict, AnimationStartedEvent]]
        """
        if init is not None:
            try:
                ourselves = AnimationStartedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['AnimationStartedEvent', dict]]]:
        """
        Safely create a new list AnimationStartedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list AnimationStartedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of AnimationStartedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, AnimationStartedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AnimationStartedEvent.safe_create(it))
            return list_of_self
        else:
            return init


ANIMATION_EVENTS_TO_CLASS = {
   "Animation.animationCanceled": AnimationCanceledEvent,
   "Animation.animationCreated": AnimationCreatedEvent,
   "Animation.animationStarted": AnimationStartedEvent,
}

AnimationNS = namedtuple("AnimationNS", ["AnimationCanceled", "AnimationCreated", "AnimationStarted"])

ANIMATION_EVENTS_NS = AnimationNS(
  AnimationCanceled="Animation.animationCanceled",
  AnimationCreated="Animation.animationCreated",
  AnimationStarted="Animation.animationStarted",
)
