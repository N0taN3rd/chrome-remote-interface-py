from cripy.gevent.protocol.dom import types as DOM

__all__ = [
    "KeyframesRule",
    "KeyframeStyle",
    "AnimationEffect",
    "AnimationT",
    "ANIMATION_TYPE_TO_OBJECT"
]


class KeyframesRule(object):
    """
    Keyframes Rule
    """

    __slots__ = ["name", "keyframes"]

    def __init__(self, keyframes, name=None):
        """
        :param name: CSS keyframed animation's name.
        :type name: Optional[str]
        :param keyframes: List of animation keyframes.
        :type keyframes: List[dict]
        """
        super(KeyframesRule, self).__init__()
        self.name = name
        self.keyframes = KeyframeStyle.safe_create_from_list(keyframes)

    def __repr__(self):
        repr_args = []
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.keyframes is not None:
            repr_args.append("keyframes={!r}".format(self.keyframes))
        return "KeyframesRule(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create KeyframesRule from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of KeyframesRule
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of KeyframesRule if creation did not fail
        :rtype: Optional[Union[dict, KeyframesRule]]
        """
        if init is not None:
            try:
                ourselves = KeyframesRule(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list KeyframesRules from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list KeyframesRule instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of KeyframesRule instances if creation did not fail
        :rtype: Optional[List[Union[dict, KeyframesRule]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(KeyframesRule.safe_create(it))
            return list_of_self
        else:
            return init


class KeyframeStyle(object):
    """
    Keyframe Style
    """

    __slots__ = ["offset", "easing"]

    def __init__(self, offset, easing):
        """
        :param offset: Keyframe's time offset.
        :type offset: str
        :param easing: `AnimationEffect`'s timing function.
        :type easing: str
        """
        super(KeyframeStyle, self).__init__()
        self.offset = offset
        self.easing = easing

    def __repr__(self):
        repr_args = []
        if self.offset is not None:
            repr_args.append("offset={!r}".format(self.offset))
        if self.easing is not None:
            repr_args.append("easing={!r}".format(self.easing))
        return "KeyframeStyle(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create KeyframeStyle from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of KeyframeStyle
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of KeyframeStyle if creation did not fail
        :rtype: Optional[Union[dict, KeyframeStyle]]
        """
        if init is not None:
            try:
                ourselves = KeyframeStyle(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list KeyframeStyles from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list KeyframeStyle instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of KeyframeStyle instances if creation did not fail
        :rtype: Optional[List[Union[dict, KeyframeStyle]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(KeyframeStyle.safe_create(it))
            return list_of_self
        else:
            return init


class AnimationEffect(object):
    """
    AnimationEffect instance
    """

    __slots__ = ["delay", "endDelay", "iterationStart", "iterations", "duration", "direction", "fill", "backendNodeId", "keyframesRule", "easing"]

    def __init__(self, delay, endDelay, iterationStart, iterations, duration, direction, fill, easing, backendNodeId=None, keyframesRule=None):
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
        super(AnimationEffect, self).__init__()
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

    def __repr__(self):
        repr_args = []
        if self.delay is not None:
            repr_args.append("delay={!r}".format(self.delay))
        if self.endDelay is not None:
            repr_args.append("endDelay={!r}".format(self.endDelay))
        if self.iterationStart is not None:
            repr_args.append("iterationStart={!r}".format(self.iterationStart))
        if self.iterations is not None:
            repr_args.append("iterations={!r}".format(self.iterations))
        if self.duration is not None:
            repr_args.append("duration={!r}".format(self.duration))
        if self.direction is not None:
            repr_args.append("direction={!r}".format(self.direction))
        if self.fill is not None:
            repr_args.append("fill={!r}".format(self.fill))
        if self.backendNodeId is not None:
            repr_args.append("backendNodeId={!r}".format(self.backendNodeId))
        if self.keyframesRule is not None:
            repr_args.append("keyframesRule={!r}".format(self.keyframesRule))
        if self.easing is not None:
            repr_args.append("easing={!r}".format(self.easing))
        return "AnimationEffect(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create AnimationEffect from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of AnimationEffect
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of AnimationEffect if creation did not fail
        :rtype: Optional[Union[dict, AnimationEffect]]
        """
        if init is not None:
            try:
                ourselves = AnimationEffect(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list AnimationEffects from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list AnimationEffect instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of AnimationEffect instances if creation did not fail
        :rtype: Optional[List[Union[dict, AnimationEffect]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AnimationEffect.safe_create(it))
            return list_of_self
        else:
            return init


class AnimationT(object):
    """
    Animation instance.
    """

    __slots__ = ["id", "name", "pausedState", "playState", "playbackRate", "startTime", "currentTime", "type", "source", "cssId"]

    def __init__(self, id, name, pausedState, playState, playbackRate, startTime, currentTime, type, source=None, cssId=None):
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
        super(AnimationT, self).__init__()
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

    def __repr__(self):
        repr_args = []
        if self.id is not None:
            repr_args.append("id={!r}".format(self.id))
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.pausedState is not None:
            repr_args.append("pausedState={!r}".format(self.pausedState))
        if self.playState is not None:
            repr_args.append("playState={!r}".format(self.playState))
        if self.playbackRate is not None:
            repr_args.append("playbackRate={!r}".format(self.playbackRate))
        if self.startTime is not None:
            repr_args.append("startTime={!r}".format(self.startTime))
        if self.currentTime is not None:
            repr_args.append("currentTime={!r}".format(self.currentTime))
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        if self.source is not None:
            repr_args.append("source={!r}".format(self.source))
        if self.cssId is not None:
            repr_args.append("cssId={!r}".format(self.cssId))
        return "AnimationT(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create AnimationT from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of AnimationT
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of AnimationT if creation did not fail
        :rtype: Optional[Union[dict, AnimationT]]
        """
        if init is not None:
            try:
                ourselves = AnimationT(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list AnimationTs from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list AnimationT instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of AnimationT instances if creation did not fail
        :rtype: Optional[List[Union[dict, AnimationT]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AnimationT.safe_create(it))
            return list_of_self
        else:
            return init


ANIMATION_TYPE_TO_OBJECT = {
    "KeyframesRule": KeyframesRule,
    "KeyframeStyle": KeyframeStyle,
    "AnimationEffect": AnimationEffect,
    "AnimationT": AnimationT,
}
