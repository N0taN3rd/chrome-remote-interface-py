from cripy.sync.protocol.runtime import types as Runtime
from cripy.sync.protocol.animation import events as Events
from cripy.sync.protocol.animation import types as Types

__all__ = ["Animation"] + Events.__all__ + Types.__all__ 


class Animation(object):
    dependencies = ['Runtime', 'DOM']

    def __init__(self, chrome):
        self.chrome = chrome

    def disable(self, cb=None):
        self.chrome.send('Animation.disable')


    def enable(self, cb=None):
        self.chrome.send('Animation.enable')


    def getCurrentTime(self, id, cb=None):
        """
        :param id: Id of animation.
        :type id: str
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if id is not None:
            msg_dict['id'] = id
        self.chrome.send('Animation.getCurrentTime', params=msg_dict, cb=cb_wrapper)


    def getPlaybackRate(self, cb=None):
        def cb_wrapper(res):
            cb(res)
        self.chrome.send('Animation.getPlaybackRate', cb=cb_wrapper)


    def releaseAnimations(self, animations, cb=None):
        """
        :param animations: List of animation ids to seek.
        :type animations: List[str]
        """
        msg_dict = dict()
        if animations is not None:
            msg_dict['animations'] = animations
        self.chrome.send('Animation.releaseAnimations', params=msg_dict)


    def resolveAnimation(self, animationId, cb=None):
        """
        :param animationId: Animation id.
        :type animationId: str
        """
        def cb_wrapper(res):
            res['remoteObject'] = Runtime.RemoteObject.safe_create(res['remoteObject'])
            cb(res)
        msg_dict = dict()
        if animationId is not None:
            msg_dict['animationId'] = animationId
        self.chrome.send('Animation.resolveAnimation', params=msg_dict, cb=cb_wrapper)


    def seekAnimations(self, animations, currentTime, cb=None):
        """
        :param animations: List of animation ids to seek.
        :type animations: List[str]
        :param currentTime: Set the current time of each animation.
        :type currentTime: float
        """
        msg_dict = dict()
        if animations is not None:
            msg_dict['animations'] = animations
        if currentTime is not None:
            msg_dict['currentTime'] = currentTime
        self.chrome.send('Animation.seekAnimations', params=msg_dict)


    def setPaused(self, animations, paused, cb=None):
        """
        :param animations: Animations to set the pause state of.
        :type animations: List[str]
        :param paused: Paused state to set to.
        :type paused: bool
        """
        msg_dict = dict()
        if animations is not None:
            msg_dict['animations'] = animations
        if paused is not None:
            msg_dict['paused'] = paused
        self.chrome.send('Animation.setPaused', params=msg_dict)


    def setPlaybackRate(self, playbackRate, cb=None):
        """
        :param playbackRate: Playback rate for animations on page
        :type playbackRate: float
        """
        msg_dict = dict()
        if playbackRate is not None:
            msg_dict['playbackRate'] = playbackRate
        self.chrome.send('Animation.setPlaybackRate', params=msg_dict)


    def setTiming(self, animationId, duration, delay, cb=None):
        """
        :param animationId: Animation id.
        :type animationId: str
        :param duration: Duration of the animation.
        :type duration: float
        :param delay: Delay of the animation.
        :type delay: float
        """
        msg_dict = dict()
        if animationId is not None:
            msg_dict['animationId'] = animationId
        if duration is not None:
            msg_dict['duration'] = duration
        if delay is not None:
            msg_dict['delay'] = delay
        self.chrome.send('Animation.setTiming', params=msg_dict)


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

