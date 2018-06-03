from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.dom import types as DOM


class KeyframesRule(ProtocolType):
    """
    Keyframes Rule
    """

    def __init__(self, keyframes: List[Union['KeyframeStyle', dict]], name: Optional[str] = None) -> None:
        """
        :param name: CSS keyframed animation's name.
        :type name: Optional[str]
        :param keyframes: List of animation keyframes.
        :type keyframes: List[dict]
        """
        super().__init__()
        self.name = name
        self.keyframes = KeyframeStyle.safe_create_from_list(keyframes)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['KeyframesRule', dict]]:
        if init is not None:
            try:
                ourselves = KeyframesRule(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['KeyframesRule', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(KeyframesRule.safe_create(it))
            return list_of_self
        else:
            return init


class KeyframeStyle(ProtocolType):
    """
    Keyframe Style
    """

    def __init__(self, offset: str, easing: str) -> None:
        """
        :param offset: Keyframe's time offset.
        :type offset: str
        :param easing: `AnimationEffect`'s timing function.
        :type easing: str
        """
        super().__init__()
        self.offset = offset
        self.easing = easing

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['KeyframeStyle', dict]]:
        if init is not None:
            try:
                ourselves = KeyframeStyle(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['KeyframeStyle', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(KeyframeStyle.safe_create(it))
            return list_of_self
        else:
            return init


class AnimationEffect(ProtocolType):
    """
    AnimationEffect instance
    """

    def __init__(self, delay: float, endDelay: float, iterationStart: float, iterations: float, duration: float, direction: str, fill: str, easing: str, backendNodeId: Optional[int] = None, keyframesRule: Optional[Union['KeyframesRule', dict]] = None) -> None:
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
        :type backendNodeId: Optional[int]
        :param keyframesRule: `AnimationEffect`'s keyframes.
        :type keyframesRule: Optional[dict]
        :param easing: `AnimationEffect`'s timing function.
        :type easing: str
        """
        super().__init__()
        self.delay = delay
        self.endDelay = endDelay
        self.iterationStart = iterationStart
        self.iterations = iterations
        self.duration = duration
        self.direction = direction
        self.fill = fill
        self.backendNodeId = backendNodeId
        self.keyframesRule = KeyframesRule.safe_create(keyframesRule)
        self.easing = easing

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['AnimationEffect', dict]]:
        if init is not None:
            try:
                ourselves = AnimationEffect(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['AnimationEffect', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AnimationEffect.safe_create(it))
            return list_of_self
        else:
            return init


class Animation(ProtocolType):
    """
    Animation instance.
    """

    def __init__(self, id: str, name: str, pausedState: bool, playState: str, playbackRate: float, startTime: float, currentTime: float, type: str, source: Optional[Union['AnimationEffect', dict]] = None, cssId: Optional[str] = None) -> None:
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
        :type source: Optional[dict]
        :param cssId: A unique ID for `Animation` representing the sources that triggered this CSS animation/transition.
        :type cssId: Optional[str]
        """
        super().__init__()
        self.id = id
        self.name = name
        self.pausedState = pausedState
        self.playState = playState
        self.playbackRate = playbackRate
        self.startTime = startTime
        self.currentTime = currentTime
        self.type = type
        self.source = AnimationEffect.safe_create(source)
        self.cssId = cssId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['Animation', dict]]:
        if init is not None:
            try:
                ourselves = Animation(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['Animation', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Animation.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "KeyframesRule": KeyframesRule,
    "KeyframeStyle": KeyframeStyle,
    "AnimationEffect": AnimationEffect,
    "Animation": Animation,
}
