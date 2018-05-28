from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.dom import types as DOM


class Animation(ChromeTypeBase):
    """Animation instance."""
    def __init__(self, id: str, name: str, pausedState: bool, playState: str, playbackRate: float, startTime: float, currentTime: float, type: str, source: Optional['AnimationEffect'] = None, cssId: Optional[str] = None) -> None:
        """
        :param str id: `Animation`'s id.
        :param str name: `Animation`'s name.
        :param bool pausedState: `Animation`'s internal paused state.
        :param str playState: `Animation`'s play state.
        :param float playbackRate: `Animation`'s playback rate.
        :param float startTime: `Animation`'s start time.
        :param float currentTime: `Animation`'s current time.
        :param str type: Animation type of `Animation`.
        :param AnimationEffect source: `Animation`'s source animation node.
        :param str cssId: A unique ID for `Animation` representing the sources that triggered this CSS animation/transition.
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
    def __init__(self, delay: float, endDelay: float, iterationStart: float, iterations: float, duration: float, direction: str, fill: str, easing: str, backendNodeId: Optional['DOM.BackendNodeId'] = None, keyframesRule: Optional['KeyframesRule'] = None) -> None:
        """
        :param float delay: `AnimationEffect`'s delay.
        :param float endDelay: `AnimationEffect`'s end delay.
        :param float iterationStart: `AnimationEffect`'s iteration start.
        :param float iterations: `AnimationEffect`'s iterations.
        :param float duration: `AnimationEffect`'s iteration duration.
        :param str direction: `AnimationEffect`'s playback direction.
        :param str fill: `AnimationEffect`'s fill mode.
        :param DOM.BackendNodeId backendNodeId: `AnimationEffect`'s target node.
        :param KeyframesRule keyframesRule: `AnimationEffect`'s keyframes.
        :param str easing: `AnimationEffect`'s timing function.
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
    def __init__(self, keyframes: List['KeyframeStyle'], name: Optional[str] = None) -> None:
        """
        :param str name: CSS keyframed animation's name.
        :param array keyframes: List of animation keyframes.
        """
        super().__init__()
        self.name: Optional[str] = name
        self.keyframes: List[KeyframeStyle] = keyframes


class KeyframeStyle(ChromeTypeBase):
    """Keyframe Style"""
    def __init__(self, offset: str, easing: str) -> None:
        """
        :param str offset: Keyframe's time offset.
        :param str easing: `AnimationEffect`'s timing function.
        """
        super().__init__()
        self.offset: str = offset
        self.easing: str = easing


