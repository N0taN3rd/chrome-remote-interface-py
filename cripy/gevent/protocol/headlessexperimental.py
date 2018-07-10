__all__ = ["HeadlessExperimental"]


class HeadlessExperimental(object):
    """
    This domain provides experimental commands only supported in headless mode.
    """

    dependencies = ['Page', 'Runtime']

    def __init__(self, chrome):
        """
        Construct a new HeadlessExperimental object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def beginFrame(self, frameTimeTicks=None, interval=None, noDisplayUpdates=None, screenshot=None):
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
            msg_dict['frameTimeTicks'] = frameTimeTicks
        if interval is not None:
            msg_dict['interval'] = interval
        if noDisplayUpdates is not None:
            msg_dict['noDisplayUpdates'] = noDisplayUpdates
        if screenshot is not None:
            msg_dict['screenshot'] = screenshot
        wres = self.chrome.send('HeadlessExperimental.beginFrame', msg_dict)
        return wres.get()

    def disable(self):
        """
        Disables headless events for the target.
        """
        wres = self.chrome.send('HeadlessExperimental.disable')
        return wres.get()

    def enable(self):
        """
        Enables headless events for the target.
        """
        wres = self.chrome.send('HeadlessExperimental.enable')
        return wres.get()

    def needsBeginFramesChanged(self, fn, once=False):
        """
        Issued when the target starts or stops needing BeginFrames.
        """
        self.chrome.on("HeadlessExperimental.needsBeginFramesChanged", fn, once=once)


