from cripy.gevent.protocol.runtime import types as Runtime
from cripy.gevent.protocol.animation import events as Events
from cripy.gevent.protocol.animation import types as Types

__all__ = ["Animation"]


class Animation(object):
    dependencies = ['Runtime', 'DOM']

    events = Events.ANIMATION_EVENTS_NS

    def __init__(self, chrome):
        """
        Construct a new Animation object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def disable(self):
        """
        Disables animation domain notifications.
        """
        wres = self.chrome.send('Animation.disable')
        return wres.get()

    def enable(self):
        """
        Enables animation domain notifications.
        """
        wres = self.chrome.send('Animation.enable')
        return wres.get()

    def getCurrentTime(self, id):
        """
        Returns the current time of the an animation.

        :param id: Id of animation.
        :type id: str
        """
        msg_dict = dict()
        if id is not None:
            msg_dict['id'] = id
        wres = self.chrome.send('Animation.getCurrentTime', msg_dict)
        res = wres.get()
        return res

    def getPlaybackRate(self):
        """
        Gets the playback rate of the document timeline.
        """
        wres = self.chrome.send('Animation.getPlaybackRate')
        res = wres.get()
        return res

    def releaseAnimations(self, animations):
        """
        Releases a set of animations to no longer be manipulated.

        :param animations: List of animation ids to seek.
        :type animations: List[str]
        """
        msg_dict = dict()
        if animations is not None:
            msg_dict['animations'] = animations
        wres = self.chrome.send('Animation.releaseAnimations', msg_dict)
        return wres.get()

    def resolveAnimation(self, animationId):
        """
        Gets the remote object of the Animation.

        :param animationId: Animation id.
        :type animationId: str
        """
        msg_dict = dict()
        if animationId is not None:
            msg_dict['animationId'] = animationId
        wres = self.chrome.send('Animation.resolveAnimation', msg_dict)
        res = wres.get()
        res['remoteObject'] = Runtime.RemoteObject.safe_create(res['remoteObject'])
        return res

    def seekAnimations(self, animations, currentTime):
        """
        Seek a set of animations to a particular time within each animation.

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
        wres = self.chrome.send('Animation.seekAnimations', msg_dict)
        return wres.get()

    def setPaused(self, animations, paused):
        """
        Sets the paused state of a set of animations.

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
        wres = self.chrome.send('Animation.setPaused', msg_dict)
        return wres.get()

    def setPlaybackRate(self, playbackRate):
        """
        Sets the playback rate of the document timeline.

        :param playbackRate: Playback rate for animations on page
        :type playbackRate: float
        """
        msg_dict = dict()
        if playbackRate is not None:
            msg_dict['playbackRate'] = playbackRate
        wres = self.chrome.send('Animation.setPlaybackRate', msg_dict)
        return wres.get()

    def setTiming(self, animationId, duration, delay):
        """
        Sets the timing of an animation node.

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
        wres = self.chrome.send('Animation.setTiming', msg_dict)
        return wres.get()

    def animationCanceled(self, fn, once=False):
        self.chrome.on("Animation.animationCanceled", fn, once=once)

    def animationCreated(self, fn, once=False):
        self.chrome.on("Animation.animationCreated", fn, once=once)

    def animationStarted(self, fn, once=False):
        self.chrome.on("Animation.animationStarted", fn, once=once)

    @staticmethod
    def get_event_classes():
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return Events.ANIMATION_EVENTS_TO_CLASS

