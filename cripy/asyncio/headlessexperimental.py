from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from .client import Client

__all__ = ["HeadlessExperimental"]


@attr.dataclass(slots=True)
class HeadlessExperimental(object):
    """
    This domain provides experimental commands only supported in headless mode.
    """

    client: "Client" = attr.ib(repr=False)
    dependencies: ClassVar[List[str]] = ["Page", "Runtime"]

    async def beginFrame(
        self,
        frameTimeTicks: Optional[float] = None,
        interval: Optional[float] = None,
        noDisplayUpdates: Optional[bool] = None,
        screenshot: Optional[dict] = None,
    ) -> Optional[dict]:
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
        res = await self.client.send("HeadlessExperimental.beginFrame", msg_dict)
        return res

    async def disable(self) -> Optional[dict]:
        """
        Disables headless events for the target.
        """
        res = await self.client.send("HeadlessExperimental.disable")
        return res

    async def enable(self) -> Optional[dict]:
        """
        Enables headless events for the target.
        """
        res = await self.client.send("HeadlessExperimental.enable")
        return res

    def needsBeginFramesChanged(
        self, fn: Callable[..., Any], once: bool = False
    ) -> None:
        """
        Issued when the target starts or stops needing BeginFrames.
        """
        if once:
            self.client.once("HeadlessExperimental.needsBeginFramesChanged", fn)
        else:
            self.client.on("HeadlessExperimental.needsBeginFramesChanged", fn)
