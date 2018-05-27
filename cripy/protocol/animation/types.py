from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.dom import types as DOM


class Animation(ChromeTypeBase):
    """Animation instance."""

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
        """
        :param id: `Animation`'s id.
        :param name: `Animation`'s name.
        :param pausedState: `Animation`'s internal paused state.
        :param playState: `Animation`'s play state.
        :param playbackRate: `Animation`'s playback rate.
        :param startTime: `Animation`'s start time.
        :param currentTime: `Animation`'s current time.
        :param type: Animation type of `Animation`.
        :param source: `Animation`'s source animation node.
        :param cssId: A unique ID for `Animation` representing the sources that triggered this CSS
animation/transition.
        """
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
    """AnimationEffect instance"""

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
        """
        :param delay: `AnimationEffect`'s delay.
        :param endDelay: `AnimationEffect`'s end delay.
        :param iterationStart: `AnimationEffect`'s iteration start.
        :param iterations: `AnimationEffect`'s iterations.
        :param duration: `AnimationEffect`'s iteration duration.
        :param direction: `AnimationEffect`'s playback direction.
        :param fill: `AnimationEffect`'s fill mode.
        :param backendNodeId: `AnimationEffect`'s target node.
        :param keyframesRule: `AnimationEffect`'s keyframes.
        :param easing: `AnimationEffect`'s timing function.
        """
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
    """Keyframes Rule"""

    def __init__(
        self, keyframes: List["KeyframeStyle"], name: Optional[str] = None
    ) -> None:
        """
        :param name: CSS keyframed animation's name.
        :param keyframes: List of animation keyframes.
        """
        super().__init__()
        self.name: Optional[str] = name
        self.keyframes: List[KeyframeStyle] = keyframes


class KeyframeStyle(ChromeTypeBase):
    """Keyframe Style"""

    def __init__(self, offset: str, easing: str) -> None:
        """
        :param offset: Keyframe's time offset.
        :param easing: `AnimationEffect`'s timing function.
        """
        super().__init__()
        self.offset: str = offset
        self.easing: str = easing
