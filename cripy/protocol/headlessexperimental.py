"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["HeadlessExperimental"]


@attr.dataclass(slots=True, cmp=False)
class HeadlessExperimental(object):
    """
    This domain provides experimental commands only supported in headless mode.
    """

    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def beginFrame(
        self,
        frameTimeTicks: Optional[float] = None,
        interval: Optional[float] = None,
        noDisplayUpdates: Optional[bool] = None,
        screenshot: Optional[dict] = None,
    ) -> Awaitable[Dict]:
        """
        Sends a BeginFrame to the target and returns when the frame was completed. Optionally captures a
screenshot from the resulting frame. Requires that the target was created with enabled
BeginFrameControl. Designed for use with --run-all-compositor-stages-before-draw, see also
https://goo.gl/3zHXhB for more background.

        :param frameTimeTicks: Timestamp of this BeginFrame in Renderer TimeTicks (milliseconds of uptime). If not set, the current time will be used.
        :type frameTimeTicks: Optional[float]
        :param interval: The interval between BeginFrames that is reported to the compositor, in milliseconds. Defaults to a 60 frames/second interval, i.e. about 16.666 milliseconds.
        :type interval: Optional[float]
        :param noDisplayUpdates: Whether updates should not be committed and drawn onto the display. False by default. If true, only side effects of the BeginFrame will be run, such as layout and animations, but any visual updates may not be visible on the display or in screenshots.
        :type noDisplayUpdates: Optional[bool]
        :param screenshot: If set, a screenshot of the frame will be captured and returned in the response. Otherwise, no screenshot will be captured. Note that capturing a screenshot can fail, for example, during renderer initialization. In such a case, no screenshot data will be returned.
        :type screenshot: Optional[dict]
        """
        msg_dict = dict()
        if frameTimeTicks is not None:
            msg_dict["frameTimeTicks"] = frameTimeTicks
        if interval is not None:
            msg_dict["interval"] = interval
        if noDisplayUpdates is not None:
            msg_dict["noDisplayUpdates"] = noDisplayUpdates
        if screenshot is not None:
            msg_dict["screenshot"] = screenshot
        return self.client.send("HeadlessExperimental.beginFrame", msg_dict)

    def disable(self) -> Awaitable[Dict]:
        """
        Disables headless events for the target.
        """
        return self.client.send("HeadlessExperimental.disable")

    def enable(self) -> Awaitable[Dict]:
        """
        Enables headless events for the target.
        """
        return self.client.send("HeadlessExperimental.enable")

    def needsBeginFramesChanged(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        Issued when the target starts or stops needing BeginFrames.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("HeadlessExperimental.needsBeginFramesChanged", _cb)

            return future

        self.client.on("HeadlessExperimental.needsBeginFramesChanged", cb)
        return lambda: self.client.remove_listener(
            "HeadlessExperimental.needsBeginFramesChanged", cb
        )
