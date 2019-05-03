"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["HeadlessExperimental"]


class HeadlessExperimental:
    """
    This domain provides experimental commands only supported in headless mode.
     
    Domain Dependencies: 
      * Page
      * Runtime
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/HeadlessExperimental`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of HeadlessExperimental

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def beginFrame(
        self,
        frameTimeTicks: Optional[Union[int, float]] = None,
        interval: Optional[Union[int, float]] = None,
        noDisplayUpdates: Optional[bool] = None,
        screenshot: Optional[Dict[str, Any]] = None,
    ) -> Awaitable[Dict]:
        """
        Sends a BeginFrame to the target and returns when the frame was completed. Optionally captures a
        screenshot from the resulting frame. Requires that the target was created with enabled
        BeginFrameControl. Designed for use with --run-all-compositor-stages-before-draw, see also
        https://goo.gl/3zHXhB for more background.

        See `https://chromedevtools.github.io/devtools-protocol/tot/HeadlessExperimental#method-beginFrame`

        :param frameTimeTicks: Timestamp of this BeginFrame in Renderer TimeTicks (milliseconds of uptime). If not set,
         the current time will be used.
        :param interval: The interval between BeginFrames that is reported to the compositor, in milliseconds.
         Defaults to a 60 frames/second interval, i.e. about 16.666 milliseconds.
        :param noDisplayUpdates: Whether updates should not be committed and drawn onto the display. False by default. If
         true, only side effects of the BeginFrame will be run, such as layout and animations, but
         any visual updates may not be visible on the display or in screenshots.
        :param screenshot: If set, a screenshot of the frame will be captured and returned in the response. Otherwise,
         no screenshot will be captured. Note that capturing a screenshot can fail, for example,
         during renderer initialization. In such a case, no screenshot data will be returned.
        :return: The results of the command
        """
        msg = {}
        if frameTimeTicks is not None:
            msg["frameTimeTicks"] = frameTimeTicks
        if interval is not None:
            msg["interval"] = interval
        if noDisplayUpdates is not None:
            msg["noDisplayUpdates"] = noDisplayUpdates
        if screenshot is not None:
            msg["screenshot"] = screenshot
        return self.client.send("HeadlessExperimental.beginFrame", msg)

    def disable(self) -> Awaitable[Dict]:
        """
        Disables headless events for the target.

        See `https://chromedevtools.github.io/devtools-protocol/tot/HeadlessExperimental#method-disable`

        :return: The results of the command
        """
        return self.client.send("HeadlessExperimental.disable", {})

    def enable(self) -> Awaitable[Dict]:
        """
        Enables headless events for the target.

        See `https://chromedevtools.github.io/devtools-protocol/tot/HeadlessExperimental#method-enable`

        :return: The results of the command
        """
        return self.client.send("HeadlessExperimental.enable", {})

    def needsBeginFramesChanged(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        Issued when the target starts or stops needing BeginFrames.

        See `https://chromedevtools.github.io/devtools-protocol/tot/HeadlessExperimental#event-needsBeginFramesChanged`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "HeadlessExperimental.needsBeginFramesChanged"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
