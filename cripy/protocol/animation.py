# -*- coding: utf-8 -*-
"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Animation"]


@attr.dataclass(slots=True, cmp=False)
class Animation(object):
    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def disable(self) -> Awaitable[Optional[dict]]:
        """
        Disables animation domain notifications.
        """
        return self.client.send("Animation.disable")

    def enable(self) -> Awaitable[Optional[dict]]:
        """
        Enables animation domain notifications.
        """
        return self.client.send("Animation.enable")

    def getCurrentTime(self, id: str) -> Awaitable[Optional[dict]]:
        """
        Returns the current time of the an animation.

        :param id: Id of animation.
        :type id: str
        """
        msg_dict = dict()
        if id is not None:
            msg_dict["id"] = id
        return self.client.send("Animation.getCurrentTime", msg_dict)

    def getPlaybackRate(self) -> Awaitable[Optional[dict]]:
        """
        Gets the playback rate of the document timeline.
        """
        return self.client.send("Animation.getPlaybackRate")

    def releaseAnimations(self, animations: List[str]) -> Awaitable[Optional[dict]]:
        """
        Releases a set of animations to no longer be manipulated.

        :param animations: List of animation ids to seek.
        :type animations: List[str]
        """
        msg_dict = dict()
        if animations is not None:
            msg_dict["animations"] = animations
        return self.client.send("Animation.releaseAnimations", msg_dict)

    def resolveAnimation(self, animationId: str) -> Awaitable[Optional[dict]]:
        """
        Gets the remote object of the Animation.

        :param animationId: Animation id.
        :type animationId: str
        """
        msg_dict = dict()
        if animationId is not None:
            msg_dict["animationId"] = animationId
        return self.client.send("Animation.resolveAnimation", msg_dict)

    def seekAnimations(
        self, animations: List[str], currentTime: float
    ) -> Awaitable[Optional[dict]]:
        """
        Seek a set of animations to a particular time within each animation.

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
        return self.client.send("Animation.seekAnimations", msg_dict)

    def setPaused(
        self, animations: List[str], paused: bool
    ) -> Awaitable[Optional[dict]]:
        """
        Sets the paused state of a set of animations.

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
        return self.client.send("Animation.setPaused", msg_dict)

    def setPlaybackRate(self, playbackRate: float) -> Awaitable[Optional[dict]]:
        """
        Sets the playback rate of the document timeline.

        :param playbackRate: Playback rate for animations on page
        :type playbackRate: float
        """
        msg_dict = dict()
        if playbackRate is not None:
            msg_dict["playbackRate"] = playbackRate
        return self.client.send("Animation.setPlaybackRate", msg_dict)

    def setTiming(
        self, animationId: str, duration: float, delay: float
    ) -> Awaitable[Optional[dict]]:
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
            msg_dict["animationId"] = animationId
        if duration is not None:
            msg_dict["duration"] = duration
        if delay is not None:
            msg_dict["delay"] = delay
        return self.client.send("Animation.setTiming", msg_dict)

    def animationCanceled(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Event for when an animation has been cancelled.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Animation.animationCanceled", _cb)

            return future

        self.client.on("Animation.animationCanceled", cb)

    def animationCreated(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Event for each animation that has been created.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Animation.animationCreated", _cb)

            return future

        self.client.on("Animation.animationCreated", cb)

    def animationStarted(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Event for animation that has been started.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Any) -> None:
                future.set_result(msg)

            self.client.once("Animation.animationStarted", _cb)

            return future

        self.client.on("Animation.animationStarted", cb)
