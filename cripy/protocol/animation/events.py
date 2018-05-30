from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
from cripy.protocol.animation.types import (
    Animation,
)


class AnimationCanceledEvent(BaseEvent):
    """
    Event for when an animation has been cancelled.
    """

    event = "Animation.animationCanceled"

    def __init__(self, id: str) -> None:
        """
        :param id: Id of the animation that was cancelled.
        :type id: str
        """
        super().__init__()
        self.id = id

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['AnimationCanceledEvent']:
        if init is not None:
            return AnimationCanceledEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['AnimationCanceledEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AnimationCanceledEvent(**it))
            return list_of_self
        else:
            return init


class AnimationCreatedEvent(BaseEvent):
    """
    Event for each animation that has been created.
    """

    event = "Animation.animationCreated"

    def __init__(self, id: str) -> None:
        """
        :param id: Id of the animation that was created.
        :type id: str
        """
        super().__init__()
        self.id = id

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['AnimationCreatedEvent']:
        if init is not None:
            return AnimationCreatedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['AnimationCreatedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AnimationCreatedEvent(**it))
            return list_of_self
        else:
            return init


class AnimationStartedEvent(BaseEvent):
    """
    Event for animation that has been started.
    """

    event = "Animation.animationStarted"

    def __init__(self, animation: Union[Animation, dict]) -> None:
        """
        :param animation: Animation that was started.
        :type animation: dict
        """
        super().__init__()
        self.animation = Animation.safe_create(animation)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['AnimationStartedEvent']:
        if init is not None:
            return AnimationStartedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['AnimationStartedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AnimationStartedEvent(**it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "Animation.animationCanceled": AnimationCanceledEvent,
   "Animation.animationCreated": AnimationCreatedEvent,
   "Animation.animationStarted": AnimationStartedEvent,
}

