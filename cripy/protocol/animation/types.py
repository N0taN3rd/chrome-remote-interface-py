from typing import Any, List, Optional, Set, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.dom import types as DOM


class KeyframesRule(ProtocolType):
    """Keyframes Rule"""

    def __init__(
        self, keyframes: List[Union["KeyframeStyle", dict]], name: Optional[str] = None
    ) -> None:
        """
        :param name: CSS keyframed animation's name.
        :type name: str
        :param keyframes: List of animation keyframes.
        :type keyframes: array
        """
        super().__init__()
        self.name: Optional[str] = name
        self.keyframes: List[KeyframeStyle] = keyframes


class KeyframeStyle(ProtocolType):
    """Keyframe Style"""

    def __init__(self, offset: str, easing: str) -> None:
        """
        :param offset: Keyframe's time offset.
        :type offset: str
        :param easing: `AnimationEffect`'s timing function.
        :type easing: str
        """
        super().__init__()
        self.offset: str = offset
        self.easing: str = easing


class AnimationEffect(ProtocolType):
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
        :type delay: float
        :param endDelay: `AnimationEffect`'s end delay.
        :type endDelay: float
        :param iterationStart: `AnimationEffect`'s iteration start.
        :type iterationStart: float
        :param iterations: `AnimationEffect`'s iterations.
        :type iterations: float
        :param duration: `AnimationEffect`'s iteration duration.
        :type duration: float
        :param direction: `AnimationEffect`'s playback direction.
        :type direction: str
        :param fill: `AnimationEffect`'s fill mode.
        :type fill: str
        :param backendNodeId: `AnimationEffect`'s target node.
        :type backendNodeId: DOM.BackendNodeId
        :param keyframesRule: `AnimationEffect`'s keyframes.
        :type keyframesRule: KeyframesRule
        :param easing: `AnimationEffect`'s timing function.
        :type easing: str
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


class Animation(ProtocolType):
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
        :type id: str
        :param name: `Animation`'s name.
        :type name: str
        :param pausedState: `Animation`'s internal paused state.
        :type pausedState: bool
        :param playState: `Animation`'s play state.
        :type playState: str
        :param playbackRate: `Animation`'s playback rate.
        :type playbackRate: float
        :param startTime: `Animation`'s start time.
        :type startTime: float
        :param currentTime: `Animation`'s current time.
        :type currentTime: float
        :param type: Animation type of `Animation`.
        :type type: str
        :param source: `Animation`'s source animation node.
        :type source: AnimationEffect
        :param cssId: A unique ID for `Animation` representing the sources that triggered this CSS animation/transition.
        :type cssId: str
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


OBJECT_LIST = {
    "KeyframesRule": KeyframesRule,
    "KeyframeStyle": KeyframeStyle,
    "AnimationEffect": AnimationEffect,
    "Animation": Animation,
}
