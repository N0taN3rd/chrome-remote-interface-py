from typing import Any, List, Optional, Union
from types import SimpleNamespace

try:
    from cripy.protocol.animation.types import *
except ImportError:
    pass


class AnimationCanceledEvent(object):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.id is not None:
            repr_args.append("id={!r}".format(self.id))
        return "AnimationCanceledEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["AnimationCanceledEvent", dict]]:
        if init is not None:
            try:
                ourselves = AnimationCanceledEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["AnimationCanceledEvent", dict]]]:
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

    event = "Animation.animationCreated"

    def __init__(self, id: str) -> None:
        """
        :param id: Id of the animation that was created.
        :type id: str
        """
        super().__init__()
        self.id = id

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.id is not None:
            repr_args.append("id={!r}".format(self.id))
        return "AnimationCreatedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["AnimationCreatedEvent", dict]]:
        if init is not None:
            try:
                ourselves = AnimationCreatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["AnimationCreatedEvent", dict]]]:
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

    event = "Animation.animationStarted"

    def __init__(self, animation: Union[Animation, dict]) -> None:
        """
        :param animation: Animation that was started.
        :type animation: dict
        """
        super().__init__()
        self.animation = Animation.safe_create(animation)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.animation is not None:
            repr_args.append("animation={!r}".format(self.animation))
        return "AnimationStartedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["AnimationStartedEvent", dict]]:
        if init is not None:
            try:
                ourselves = AnimationStartedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["AnimationStartedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AnimationStartedEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
    "Animation.animationCanceled": AnimationCanceledEvent,
    "Animation.animationCreated": AnimationCreatedEvent,
    "Animation.animationStarted": AnimationStartedEvent,
}

EVENT_NS = SimpleNamespace(
    AnimationCanceled="Animation.animationCanceled",
    AnimationCreated="Animation.animationCreated",
    AnimationStarted="Animation.animationStarted",
)
