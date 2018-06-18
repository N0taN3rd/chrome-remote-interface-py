from cripy.gevent.protocol.dom import types as DOM

__all__ = ["KeyframesRule", "KeyframeStyle", "AnimationEffect", "Animation"]


class KeyframesRule(object):
    """
    Keyframes Rule
    """

    def __init__(self, keyframes, name=None):
        """
        :param name: CSS keyframed animation's name.
        :type name: Optional[str]
        :param keyframes: List of animation keyframes.
        :type keyframes: List[dict]
        """
        super().__init__()
        self.name = name
        self.keyframes = KeyframeStyle.safe_create_from_list(keyframes)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.keyframes is not None:
            repr_args.append("keyframes={!r}".format(self.keyframes))
        return "KeyframesRule(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
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

    def __init__(self, offset, easing):
        """
        :param offset: Keyframe's time offset.
        :type offset: str
        :param easing: `AnimationEffect`'s timing function.
        :type easing: str
        """
        super().__init__()
        self.offset = offset
        self.easing = easing

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.offset is not None:
            repr_args.append("offset={!r}".format(self.offset))
        if self.easing is not None:
            repr_args.append("easing={!r}".format(self.easing))
        return "KeyframeStyle(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
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

    def __init__(
        self,
        delay,
        endDelay,
        iterationStart,
        iterations,
        duration,
        direction,
        fill,
        easing,
        backendNodeId=None,
        keyframesRule=None,
    ):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

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
        return "AnimationEffect(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
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
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AnimationEffect.safe_create(it))
            return list_of_self
        else:
            return init


class Animation(object):
    """
    Animation instance.
    """

    def __init__(
        self,
        id,
        name,
        pausedState,
        playState,
        playbackRate,
        startTime,
        currentTime,
        type,
        source=None,
        cssId=None,
    ):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

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
        return "Animation(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = Animation(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
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
