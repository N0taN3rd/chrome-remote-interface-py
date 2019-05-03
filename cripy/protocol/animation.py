"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Animation"]


class Animation:
    """
    Domain Dependencies: 
      * Runtime
      * DOM
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/Animation`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of Animation

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def disable(self) -> Awaitable[Dict]:
        """
        Disables animation domain notifications.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Animation#method-disable`

        :return: The results of the command
        """
        return self.client.send("Animation.disable", {})

    def enable(self) -> Awaitable[Dict]:
        """
        Enables animation domain notifications.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Animation#method-enable`

        :return: The results of the command
        """
        return self.client.send("Animation.enable", {})

    def getCurrentTime(self, id: str) -> Awaitable[Dict]:
        """
        Returns the current time of the an animation.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Animation#method-getCurrentTime`

        :param id: Id of animation.
        :return: The results of the command
        """
        return self.client.send("Animation.getCurrentTime", {"id": id})

    def getPlaybackRate(self) -> Awaitable[Dict]:
        """
        Gets the playback rate of the document timeline.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Animation#method-getPlaybackRate`

        :return: The results of the command
        """
        return self.client.send("Animation.getPlaybackRate", {})

    def releaseAnimations(self, animations: List[str]) -> Awaitable[Dict]:
        """
        Releases a set of animations to no longer be manipulated.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Animation#method-releaseAnimations`

        :param animations: List of animation ids to seek.
        :return: The results of the command
        """
        return self.client.send(
            "Animation.releaseAnimations", {"animations": animations}
        )

    def resolveAnimation(self, animationId: str) -> Awaitable[Dict]:
        """
        Gets the remote object of the Animation.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Animation#method-resolveAnimation`

        :param animationId: Animation id.
        :return: The results of the command
        """
        return self.client.send(
            "Animation.resolveAnimation", {"animationId": animationId}
        )

    def seekAnimations(
        self, animations: List[str], currentTime: Union[int, float]
    ) -> Awaitable[Dict]:
        """
        Seek a set of animations to a particular time within each animation.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Animation#method-seekAnimations`

        :param animations: List of animation ids to seek.
        :param currentTime: Set the current time of each animation.
        :return: The results of the command
        """
        return self.client.send(
            "Animation.seekAnimations",
            {"animations": animations, "currentTime": currentTime},
        )

    def setPaused(self, animations: List[str], paused: bool) -> Awaitable[Dict]:
        """
        Sets the paused state of a set of animations.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Animation#method-setPaused`

        :param animations: Animations to set the pause state of.
        :param paused: Paused state to set to.
        :return: The results of the command
        """
        return self.client.send(
            "Animation.setPaused", {"animations": animations, "paused": paused}
        )

    def setPlaybackRate(self, playbackRate: Union[int, float]) -> Awaitable[Dict]:
        """
        Sets the playback rate of the document timeline.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Animation#method-setPlaybackRate`

        :param playbackRate: Playback rate for animations on page
        :return: The results of the command
        """
        return self.client.send(
            "Animation.setPlaybackRate", {"playbackRate": playbackRate}
        )

    def setTiming(
        self, animationId: str, duration: Union[int, float], delay: Union[int, float]
    ) -> Awaitable[Dict]:
        """
        Sets the timing of an animation node.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Animation#method-setTiming`

        :param animationId: Animation id.
        :param duration: Duration of the animation.
        :param delay: Delay of the animation.
        :return: The results of the command
        """
        return self.client.send(
            "Animation.setTiming",
            {"animationId": animationId, "duration": duration, "delay": delay},
        )

    def animationCanceled(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Event for when an animation has been cancelled.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Animation#event-animationCanceled`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Animation.animationCanceled"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def animationCreated(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Event for each animation that has been created.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Animation#event-animationCreated`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Animation.animationCreated"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)

    def animationStarted(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Event for animation that has been started.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Animation#event-animationStarted`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Animation.animationStarted"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
