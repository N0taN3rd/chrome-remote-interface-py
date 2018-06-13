from cripy.sync.protocol.network import types as Network
from cripy.sync.protocol.dom import types as DOM
from cripy.sync.protocol.page import types as Page
from cripy.sync.protocol.emulation import events as Events
from cripy.sync.protocol.emulation import types as Types

__all__ = ["Emulation"] + Events.__all__ + Types.__all__ 


class Emulation(object):
    """
    This domain emulates different environments for the page.
    """

    dependencies = ['DOM', 'Page', 'Runtime']

    def __init__(self, chrome):
        self.chrome = chrome

    def canEmulate(self):
        def cb(res):
            self.chrome.emit('Emulation.canEmulate', res)
        self.chrome.send('Emulation.canEmulate', cb=cb)


    def clearDeviceMetricsOverride(self):
        self.chrome.send('Emulation.clearDeviceMetricsOverride')


    def clearGeolocationOverride(self):
        self.chrome.send('Emulation.clearGeolocationOverride')


    def resetPageScaleFactor(self):
        self.chrome.send('Emulation.resetPageScaleFactor')


    def setCPUThrottlingRate(self, rate):
        """
        :param rate: Throttling rate as a slowdown factor (1 is no throttle, 2 is 2x slowdown, etc).
        :type rate: float
        """
        msg_dict = dict()
        if rate is not None:
            msg_dict['rate'] = rate
        self.chrome.send('Emulation.setCPUThrottlingRate', params=msg_dict)


    def setDefaultBackgroundColorOverride(self, color):
        """
        :param color: RGBA of the default background color. If not specified, any existing override will be cleared.
        :type color: Optional[dict]
        """
        msg_dict = dict()
        if color is not None:
            msg_dict['color'] = color
        self.chrome.send('Emulation.setDefaultBackgroundColorOverride', params=msg_dict)


    def setDeviceMetricsOverride(self, width, height, deviceScaleFactor, mobile, scale, screenWidth, screenHeight, positionX, positionY, dontSetVisibleSize, screenOrientation, viewport):
        """
        :param width: Overriding width value in pixels (minimum 0, maximum 10000000). 0 disables the override.
        :type width: int
        :param height: Overriding height value in pixels (minimum 0, maximum 10000000). 0 disables the override.
        :type height: int
        :param deviceScaleFactor: Overriding device scale factor value. 0 disables the override.
        :type deviceScaleFactor: float
        :param mobile: Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text autosizing and more.
        :type mobile: bool
        :param scale: Scale to apply to resulting view image.
        :type scale: Optional[float]
        :param screenWidth: Overriding screen width value in pixels (minimum 0, maximum 10000000).
        :type screenWidth: Optional[int]
        :param screenHeight: Overriding screen height value in pixels (minimum 0, maximum 10000000).
        :type screenHeight: Optional[int]
        :param positionX: Overriding view X position on screen in pixels (minimum 0, maximum 10000000).
        :type positionX: Optional[int]
        :param positionY: Overriding view Y position on screen in pixels (minimum 0, maximum 10000000).
        :type positionY: Optional[int]
        :param dontSetVisibleSize: Do not set visible view size, rely upon explicit setVisibleSize call.
        :type dontSetVisibleSize: Optional[bool]
        :param screenOrientation: Screen orientation override.
        :type screenOrientation: Optional[dict]
        :param viewport: If set, the visible area of the page will be overridden to this viewport. This viewport change is not observed by the page, e.g. viewport-relative elements do not change positions.
        :type viewport: Optional[dict]
        """
        msg_dict = dict()
        if width is not None:
            msg_dict['width'] = width
        if height is not None:
            msg_dict['height'] = height
        if deviceScaleFactor is not None:
            msg_dict['deviceScaleFactor'] = deviceScaleFactor
        if mobile is not None:
            msg_dict['mobile'] = mobile
        if scale is not None:
            msg_dict['scale'] = scale
        if screenWidth is not None:
            msg_dict['screenWidth'] = screenWidth
        if screenHeight is not None:
            msg_dict['screenHeight'] = screenHeight
        if positionX is not None:
            msg_dict['positionX'] = positionX
        if positionY is not None:
            msg_dict['positionY'] = positionY
        if dontSetVisibleSize is not None:
            msg_dict['dontSetVisibleSize'] = dontSetVisibleSize
        if screenOrientation is not None:
            msg_dict['screenOrientation'] = screenOrientation
        if viewport is not None:
            msg_dict['viewport'] = viewport
        self.chrome.send('Emulation.setDeviceMetricsOverride', params=msg_dict)


    def setScrollbarsHidden(self, hidden):
        """
        :param hidden: Whether scrollbars should be always hidden.
        :type hidden: bool
        """
        msg_dict = dict()
        if hidden is not None:
            msg_dict['hidden'] = hidden
        self.chrome.send('Emulation.setScrollbarsHidden', params=msg_dict)


    def setDocumentCookieDisabled(self, disabled):
        """
        :param disabled: Whether document.coookie API should be disabled.
        :type disabled: bool
        """
        msg_dict = dict()
        if disabled is not None:
            msg_dict['disabled'] = disabled
        self.chrome.send('Emulation.setDocumentCookieDisabled', params=msg_dict)


    def setEmitTouchEventsForMouse(self, enabled, configuration):
        """
        :param enabled: Whether touch emulation based on mouse input should be enabled.
        :type enabled: bool
        :param configuration: Touch/gesture events configuration. Default: current platform.
        :type configuration: Optional[str]
        """
        msg_dict = dict()
        if enabled is not None:
            msg_dict['enabled'] = enabled
        if configuration is not None:
            msg_dict['configuration'] = configuration
        self.chrome.send('Emulation.setEmitTouchEventsForMouse', params=msg_dict)


    def setEmulatedMedia(self, media):
        """
        :param media: Media type to emulate. Empty string disables the override.
        :type media: str
        """
        msg_dict = dict()
        if media is not None:
            msg_dict['media'] = media
        self.chrome.send('Emulation.setEmulatedMedia', params=msg_dict)


    def setGeolocationOverride(self, latitude, longitude, accuracy):
        """
        :param latitude: Mock latitude
        :type latitude: Optional[float]
        :param longitude: Mock longitude
        :type longitude: Optional[float]
        :param accuracy: Mock accuracy
        :type accuracy: Optional[float]
        """
        msg_dict = dict()
        if latitude is not None:
            msg_dict['latitude'] = latitude
        if longitude is not None:
            msg_dict['longitude'] = longitude
        if accuracy is not None:
            msg_dict['accuracy'] = accuracy
        self.chrome.send('Emulation.setGeolocationOverride', params=msg_dict)


    def setNavigatorOverrides(self, platform):
        """
        :param platform: The platform navigator.platform should return.
        :type platform: str
        """
        msg_dict = dict()
        if platform is not None:
            msg_dict['platform'] = platform
        self.chrome.send('Emulation.setNavigatorOverrides', params=msg_dict)


    def setPageScaleFactor(self, pageScaleFactor):
        """
        :param pageScaleFactor: Page scale factor.
        :type pageScaleFactor: float
        """
        msg_dict = dict()
        if pageScaleFactor is not None:
            msg_dict['pageScaleFactor'] = pageScaleFactor
        self.chrome.send('Emulation.setPageScaleFactor', params=msg_dict)


    def setScriptExecutionDisabled(self, value):
        """
        :param value: Whether script execution should be disabled in the page.
        :type value: bool
        """
        msg_dict = dict()
        if value is not None:
            msg_dict['value'] = value
        self.chrome.send('Emulation.setScriptExecutionDisabled', params=msg_dict)


    def setTouchEmulationEnabled(self, enabled, maxTouchPoints):
        """
        :param enabled: Whether the touch event emulation should be enabled.
        :type enabled: bool
        :param maxTouchPoints: Maximum touch points supported. Defaults to one.
        :type maxTouchPoints: Optional[int]
        """
        msg_dict = dict()
        if enabled is not None:
            msg_dict['enabled'] = enabled
        if maxTouchPoints is not None:
            msg_dict['maxTouchPoints'] = maxTouchPoints
        self.chrome.send('Emulation.setTouchEmulationEnabled', params=msg_dict)


    def setVirtualTimePolicy(self, policy, budget, maxVirtualTimeTaskStarvationCount, waitForNavigation, initialVirtualTime):
        """
        :param policy: The policy
        :type policy: str
        :param budget: If set, after this many virtual milliseconds have elapsed virtual time will be paused and a virtualTimeBudgetExpired event is sent.
        :type budget: Optional[float]
        :param maxVirtualTimeTaskStarvationCount: If set this specifies the maximum number of tasks that can be run before virtual is forced forwards to prevent deadlock.
        :type maxVirtualTimeTaskStarvationCount: Optional[int]
        :param waitForNavigation: If set the virtual time policy change should be deferred until any frame starts navigating. Note any previous deferred policy change is superseded.
        :type waitForNavigation: Optional[bool]
        :param initialVirtualTime: If set, base::Time::Now will be overriden to initially return this value.
        :type initialVirtualTime: Optional[float]
        """
        def cb(res):
            self.chrome.emit('Emulation.setVirtualTimePolicy', res)
        msg_dict = dict()
        if policy is not None:
            msg_dict['policy'] = policy
        if budget is not None:
            msg_dict['budget'] = budget
        if maxVirtualTimeTaskStarvationCount is not None:
            msg_dict['maxVirtualTimeTaskStarvationCount'] = maxVirtualTimeTaskStarvationCount
        if waitForNavigation is not None:
            msg_dict['waitForNavigation'] = waitForNavigation
        if initialVirtualTime is not None:
            msg_dict['initialVirtualTime'] = initialVirtualTime
        self.chrome.send('Emulation.setVirtualTimePolicy', params=msg_dict, cb=cb)


    def setVisibleSize(self, width, height):
        """
        :param width: Frame width (DIP).
        :type width: int
        :param height: Frame height (DIP).
        :type height: int
        """
        msg_dict = dict()
        if width is not None:
            msg_dict['width'] = width
        if height is not None:
            msg_dict['height'] = height
        self.chrome.send('Emulation.setVisibleSize', params=msg_dict)


    def setUserAgentOverride(self, userAgent, acceptLanguage, platform):
        """
        :param userAgent: User agent to use.
        :type userAgent: str
        :param acceptLanguage: Browser langugage to emulate.
        :type acceptLanguage: Optional[str]
        :param platform: The platform navigator.platform should return.
        :type platform: Optional[str]
        """
        msg_dict = dict()
        if userAgent is not None:
            msg_dict['userAgent'] = userAgent
        if acceptLanguage is not None:
            msg_dict['acceptLanguage'] = acceptLanguage
        if platform is not None:
            msg_dict['platform'] = platform
        self.chrome.send('Emulation.setUserAgentOverride', params=msg_dict)


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

