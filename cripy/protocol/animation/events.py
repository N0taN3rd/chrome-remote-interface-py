from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class AnimationCanceledEvent(BaseEvent):
    """Event for when an animation has been cancelled."""

    event: str = "Animation.animationCanceled"

    def __init__(self) -> None:
        """
        :param id: Id of the animation that was cancelled.
        :type str:
        """
        super().__init__()


class AnimationCreatedEvent(BaseEvent):
    """Event for each animation that has been created."""

    event: str = "Animation.animationCreated"

    def __init__(self) -> None:
        """
        :param id: Id of the animation that was created.
        :type str:
        """
        super().__init__()


class AnimationStartedEvent(BaseEvent):
    """Event for animation that has been started."""

    event: str = "Animation.animationStarted"

    def __init__(self) -> None:
        """
        :param animation: Animation that was started.
        :type Animation:
        """
        super().__init__()


EVENT_TO_CLASS = {
   "Animation.animationCanceled": AnimationCanceledEvent,
   "Animation.animationCreated": AnimationCreatedEvent,
   "Animation.animationStarted": AnimationStartedEvent,
}

