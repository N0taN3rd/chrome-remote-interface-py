from cripy.gevent.protocol.runtime import types as Runtime
from cripy.gevent.protocol.animation import events as Events
from cripy.gevent.protocol.animation import types as Types

__all__ = ["Animation"] + Events.__all__ + Types.__all__


class Animation(object):
    dependencies = ["Runtime", "DOM"]

    def __init__(self, chrome):
        self.chrome = chrome

    def disable(self):
        wres = self.chrome.send("Animation.disable")
        return wres.get()

    def enable(self):
        wres = self.chrome.send("Animation.enable")
        return wres.get()

    def getCurrentTime(self, id):
        """
        :param id: Id of animation.
        :type id: str
        """
        msg_dict = dict()
        if id is not None:
            msg_dict["id"] = id
        wres = self.chrome.send("Animation.getCurrentTime", msg_dict)
        res = wres.get()
        return res

    def getPlaybackRate(self):
        wres = self.chrome.send("Animation.getPlaybackRate")
        res = wres.get()
        return res

    def releaseAnimations(self, animations):
        """
        :param animations: List of animation ids to seek.
        :type animations: List[str]
        """
        msg_dict = dict()
        if animations is not None:
            msg_dict["animations"] = animations
        wres = self.chrome.send("Animation.releaseAnimations", msg_dict)
        return wres.get()

    def resolveAnimation(self, animationId):
        """
        :param animationId: Animation id.
        :type animationId: str
        """
        msg_dict = dict()
        if animationId is not None:
            msg_dict["animationId"] = animationId
        wres = self.chrome.send("Animation.resolveAnimation", msg_dict)
        res = wres.get()
        res["remoteObject"] = Runtime.RemoteObject.safe_create(res["remoteObject"])
        return res

    def seekAnimations(self, animations, currentTime):
        """
        :param animations: List of animation ids to seek.
        :type animations: List[str]
        :param currentTime: Set the current time of each animation.
        :type currentTime: float
        """
        msg_dict = dict()
        if animations is not None:
            msg_dict["animations"] = animations
        if currentTime is not None:
            msg_dict["currentTime"] = currentTime
        wres = self.chrome.send("Animation.seekAnimations", msg_dict)
        return wres.get()

    def setPaused(self, animations, paused):
        """
        :param animations: Animations to set the pause state of.
        :type animations: List[str]
        :param paused: Paused state to set to.
        :type paused: bool
        """
        msg_dict = dict()
        if animations is not None:
            msg_dict["animations"] = animations
        if paused is not None:
            msg_dict["paused"] = paused
        wres = self.chrome.send("Animation.setPaused", msg_dict)
        return wres.get()

    def setPlaybackRate(self, playbackRate):
        """
        :param playbackRate: Playback rate for animations on page
        :type playbackRate: float
        """
        msg_dict = dict()
        if playbackRate is not None:
            msg_dict["playbackRate"] = playbackRate
        wres = self.chrome.send("Animation.setPlaybackRate", msg_dict)
        return wres.get()

    def setTiming(self, animationId, duration, delay):
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
            msg_dict["animationId"] = animationId
        if duration is not None:
            msg_dict["duration"] = duration
        if delay is not None:
            msg_dict["delay"] = delay
        wres = self.chrome.send("Animation.setTiming", msg_dict)
        return wres.get()

    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS
