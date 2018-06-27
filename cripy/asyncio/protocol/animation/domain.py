from typing import Any, List, Optional, Union
from cripy.asyncio.protocol.runtime import types as Runtime
from cripy.asyncio.protocol.animation import events as Events
from cripy.asyncio.protocol.animation import types as Types

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

    async def disable(self) -> Optional[dict]:
        """
        Disables animation domain notifications.
        """
        res = await self.chrome.send('Animation.disable')
        return res

    async def enable(self) -> Optional[dict]:
        """
        Enables animation domain notifications.
        """
        res = await self.chrome.send('Animation.enable')
        return res

    async def getCurrentTime(self, id: str) -> Optional[dict]:
        """
        Returns the current time of the an animation.

        :param id: Id of animation.
        :type id: str
        """
        msg_dict = dict()
        if id is not None:
            msg_dict['id'] = id
        res = await self.chrome.send('Animation.getCurrentTime', msg_dict)
        return res

    async def getPlaybackRate(self) -> Optional[dict]:
        """
        Gets the playback rate of the document timeline.
        """
        res = await self.chrome.send('Animation.getPlaybackRate')
        return res

    async def releaseAnimations(self, animations: List[str]) -> Optional[dict]:
        """
        Releases a set of animations to no longer be manipulated.

        :param animations: List of animation ids to seek.
        :type animations: List[str]
        """
        msg_dict = dict()
        if animations is not None:
            msg_dict['animations'] = animations
        res = await self.chrome.send('Animation.releaseAnimations', msg_dict)
        return res

    async def resolveAnimation(self, animationId: str) -> Optional[dict]:
        """
        Gets the remote object of the Animation.

        :param animationId: Animation id.
        :type animationId: str
        """
        msg_dict = dict()
        if animationId is not None:
            msg_dict['animationId'] = animationId
        res = await self.chrome.send('Animation.resolveAnimation', msg_dict)
        res['remoteObject'] = Runtime.RemoteObject.safe_create(res['remoteObject'])
        return res

    async def seekAnimations(self, animations: List[str], currentTime: float) -> Optional[dict]:
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
        res = await self.chrome.send('Animation.seekAnimations', msg_dict)
        return res

    async def setPaused(self, animations: List[str], paused: bool) -> Optional[dict]:
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
        res = await self.chrome.send('Animation.setPaused', msg_dict)
        return res

    async def setPlaybackRate(self, playbackRate: float) -> Optional[dict]:
        """
        Sets the playback rate of the document timeline.

        :param playbackRate: Playback rate for animations on page
        :type playbackRate: float
        """
        msg_dict = dict()
        if playbackRate is not None:
            msg_dict['playbackRate'] = playbackRate
        res = await self.chrome.send('Animation.setPlaybackRate', msg_dict)
        return res

    async def setTiming(self, animationId: str, duration: float, delay: float) -> Optional[dict]:
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
        res = await self.chrome.send('Animation.setTiming', msg_dict)
        return res

    def animationCanceled(self, fn, once=False):
        if once:
            self.chrome.once("Animation.animationCanceled", fn)
        else:
            self.chrome.on("Animation.animationCanceled", fn)

    def animationCreated(self, fn, once=False):
        if once:
            self.chrome.once("Animation.animationCreated", fn)
        else:
            self.chrome.on("Animation.animationCreated", fn)

    def animationStarted(self, fn, once=False):
        if once:
            self.chrome.once("Animation.animationStarted", fn)
        else:
            self.chrome.on("Animation.animationStarted", fn)

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return Events.ANIMATION_EVENTS_TO_CLASS

