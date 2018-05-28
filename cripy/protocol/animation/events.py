from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent
from cripy.protocol.animation.types import (
    Animation,
)


class AnimationCanceledEvent(BaseEvent):
    """Event for when an animation has been cancelled."""

    event: str = "Animation.animationCanceled"

    def __init__(self, id: str) -> None:
        """
        :param id: Id of the animation that was cancelled.
        :type id: str
        """
        super().__init__()
        self.id: str = id


class AnimationCreatedEvent(BaseEvent):
    """Event for each animation that has been created."""

    event: str = "Animation.animationCreated"

    def __init__(self, id: str) -> None:
        """
        :param id: Id of the animation that was created.
        :type id: str
        """
        super().__init__()
        self.id: str = id


class AnimationStartedEvent(BaseEvent):
    """Event for animation that has been started."""

    event: str = "Animation.animationStarted"

    def __init__(self, animation: Animation) -> None:
        """
        :param animation: Animation that was started.
        :type animation: Animation
        """
        super().__init__()
        self.animation: Animation = animation


EVENT_TO_CLASS = {
   "Animation.animationCanceled": AnimationCanceledEvent,
   "Animation.animationCreated": AnimationCreatedEvent,
   "Animation.animationStarted": AnimationStartedEvent,
}

