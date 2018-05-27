from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.dom import types as DOM


class Animation(ChromeTypeBase):

    def __init__(
        self,
        id: str,
        name: str,
        pausedState: bool,
        playState: str,
        playbackRate: float,
        startTime: float,
        currentTime: float,
        type: str,
        source: Optional["AnimationEffect"] = None,
        cssId: Optional[str] = None,
    ) -> None:
        super().__init__()
        self.id: str = id
        self.name: str = name
        self.pausedState: bool = pausedState
        self.playState: str = playState
        self.playbackRate: float = playbackRate
        self.startTime: float = startTime
        self.currentTime: float = currentTime
        self.type: str = type
        self.source: Optional[AnimationEffect] = source
        self.cssId: Optional[str] = cssId


class AnimationEffect(ChromeTypeBase):

    def __init__(
        self,
        delay: float,
        endDelay: float,
        iterationStart: float,
        iterations: float,
        duration: float,
        direction: str,
        fill: str,
        easing: str,
        backendNodeId: Optional["DOM.BackendNodeId"] = None,
        keyframesRule: Optional["KeyframesRule"] = None,
    ) -> None:
        super().__init__()
        self.delay: float = delay
        self.endDelay: float = endDelay
        self.iterationStart: float = iterationStart
        self.iterations: float = iterations
        self.duration: float = duration
        self.direction: str = direction
        self.fill: str = fill
        self.backendNodeId: Optional[DOM.BackendNodeId] = backendNodeId
        self.keyframesRule: Optional[KeyframesRule] = keyframesRule
        self.easing: str = easing


class KeyframesRule(ChromeTypeBase):

    def __init__(
        self, keyframes: List["KeyframeStyle"], name: Optional[str] = None
    ) -> None:
        super().__init__()
        self.name: Optional[str] = name
        self.keyframes: List[KeyframeStyle] = keyframes


class KeyframeStyle(ChromeTypeBase):

    def __init__(self, offset: str, easing: str) -> None:
        super().__init__()
        self.offset: str = offset
        self.easing: str = easing
