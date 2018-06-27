from typing import Any, List, Optional, Union
from cripy.asyncio.protocol.page import types as Page
from cripy.asyncio.protocol.network import types as Network
from cripy.asyncio.protocol.dom import types as DOM
from cripy.asyncio.protocol.emulation import events as Events
from cripy.asyncio.protocol.emulation import types as Types

__all__ = ["Emulation"]


class Emulation(object):
    """
    This domain emulates different environments for the page.
    """

    dependencies = ['DOM', 'Page', 'Runtime']

    events = Events.EMULATION_EVENTS_NS

    def __init__(self, chrome):
        """
        Construct a new Emulation object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def canEmulate(self) -> Optional[dict]:
        """
        Tells whether emulation is supported.
        """
        res = await self.chrome.send('Emulation.canEmulate')
        return res

    async def clearDeviceMetricsOverride(self) -> Optional[dict]:
        """
        Clears the overriden device metrics.
        """
        res = await self.chrome.send('Emulation.clearDeviceMetricsOverride')
        return res

    async def clearGeolocationOverride(self) -> Optional[dict]:
        """
        Clears the overriden Geolocation Position and Error.
        """
        res = await self.chrome.send('Emulation.clearGeolocationOverride')
        return res

    async def resetPageScaleFactor(self) -> Optional[dict]:
        """
        Requests that page scale factor is reset to initial values.
        """
        res = await self.chrome.send('Emulation.resetPageScaleFactor')
        return res

    async def setCPUThrottlingRate(self, rate: float) -> Optional[dict]:
        """
        Enables CPU throttling to emulate slow CPUs.

        :param rate: Throttling rate as a slowdown factor (1 is no throttle, 2 is 2x slowdown, etc).
        :type rate: float
        """
        msg_dict = dict()
        if rate is not None:
            msg_dict['rate'] = rate
        res = await self.chrome.send('Emulation.setCPUThrottlingRate', msg_dict)
        return res

    async def setDefaultBackgroundColorOverride(self, color: Optional[dict] = None) -> Optional[dict]:
        """
        Sets or clears an override of the default background color of the frame. This override is used
if the content does not specify one.

        :param color: RGBA of the default background color. If not specified, any existing override will be cleared.
        :type color: Optional[dict]
        """
        msg_dict = dict()
        if color is not None:
            msg_dict['color'] = color
        res = await self.chrome.send('Emulation.setDefaultBackgroundColorOverride', msg_dict)
        return res

    async def setDeviceMetricsOverride(self, width: int, height: int, deviceScaleFactor: float, mobile: bool, scale: Optional[float] = None, screenWidth: Optional[int] = None, screenHeight: Optional[int] = None, positionX: Optional[int] = None, positionY: Optional[int] = None, dontSetVisibleSize: Optional[bool] = None, screenOrientation: Optional[dict] = None, viewport: Optional[dict] = None) -> Optional[dict]:
        """
        Overrides the values of device screen dimensions (window.screen.width, window.screen.height,
window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media
query results).

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
        res = await self.chrome.send('Emulation.setDeviceMetricsOverride', msg_dict)
        return res

    async def setScrollbarsHidden(self, hidden: bool) -> Optional[dict]:
        """
        :param hidden: Whether scrollbars should be always hidden.
        :type hidden: bool
        """
        msg_dict = dict()
        if hidden is not None:
            msg_dict['hidden'] = hidden
        res = await self.chrome.send('Emulation.setScrollbarsHidden', msg_dict)
        return res

    async def setDocumentCookieDisabled(self, disabled: bool) -> Optional[dict]:
        """
        :param disabled: Whether document.coookie API should be disabled.
        :type disabled: bool
        """
        msg_dict = dict()
        if disabled is not None:
            msg_dict['disabled'] = disabled
        res = await self.chrome.send('Emulation.setDocumentCookieDisabled', msg_dict)
        return res

    async def setEmitTouchEventsForMouse(self, enabled: bool, configuration: Optional[str] = None) -> Optional[dict]:
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
        res = await self.chrome.send('Emulation.setEmitTouchEventsForMouse', msg_dict)
        return res

    async def setEmulatedMedia(self, media: str) -> Optional[dict]:
        """
        Emulates the given media for CSS media queries.

        :param media: Media type to emulate. Empty string disables the override.
        :type media: str
        """
        msg_dict = dict()
        if media is not None:
            msg_dict['media'] = media
        res = await self.chrome.send('Emulation.setEmulatedMedia', msg_dict)
        return res

    async def setGeolocationOverride(self, latitude: Optional[float] = None, longitude: Optional[float] = None, accuracy: Optional[float] = None) -> Optional[dict]:
        """
        Overrides the Geolocation Position or Error. Omitting any of the parameters emulates position
unavailable.

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
        res = await self.chrome.send('Emulation.setGeolocationOverride', msg_dict)
        return res

    async def setNavigatorOverrides(self, platform: str) -> Optional[dict]:
        """
        Overrides value returned by the javascript navigator object.

        :param platform: The platform navigator.platform should return.
        :type platform: str
        """
        msg_dict = dict()
        if platform is not None:
            msg_dict['platform'] = platform
        res = await self.chrome.send('Emulation.setNavigatorOverrides', msg_dict)
        return res

    async def setPageScaleFactor(self, pageScaleFactor: float) -> Optional[dict]:
        """
        Sets a specified page scale factor.

        :param pageScaleFactor: Page scale factor.
        :type pageScaleFactor: float
        """
        msg_dict = dict()
        if pageScaleFactor is not None:
            msg_dict['pageScaleFactor'] = pageScaleFactor
        res = await self.chrome.send('Emulation.setPageScaleFactor', msg_dict)
        return res

    async def setScriptExecutionDisabled(self, value: bool) -> Optional[dict]:
        """
        Switches script execution in the page.

        :param value: Whether script execution should be disabled in the page.
        :type value: bool
        """
        msg_dict = dict()
        if value is not None:
            msg_dict['value'] = value
        res = await self.chrome.send('Emulation.setScriptExecutionDisabled', msg_dict)
        return res

    async def setTouchEmulationEnabled(self, enabled: bool, maxTouchPoints: Optional[int] = None) -> Optional[dict]:
        """
        Enables touch on platforms which do not support them.

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
        res = await self.chrome.send('Emulation.setTouchEmulationEnabled', msg_dict)
        return res

    async def setVirtualTimePolicy(self, policy: str, budget: Optional[float] = None, maxVirtualTimeTaskStarvationCount: Optional[int] = None, waitForNavigation: Optional[bool] = None, initialVirtualTime: Optional[float] = None) -> Optional[dict]:
        """
        Turns on virtual time for all frames (replacing real-time with a synthetic time source) and sets
the current virtual time policy.  Note this supersedes any previous time budget.

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
        res = await self.chrome.send('Emulation.setVirtualTimePolicy', msg_dict)
        return res

    async def setVisibleSize(self, width: int, height: int) -> Optional[dict]:
        """
        Resizes the frame/viewport of the page. Note that this does not affect the frame's container
(e.g. browser window). Can be used to produce screenshots of the specified size. Not supported
on Android.

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
        res = await self.chrome.send('Emulation.setVisibleSize', msg_dict)
        return res

    async def setUserAgentOverride(self, userAgent: str, acceptLanguage: Optional[str] = None, platform: Optional[str] = None) -> Optional[dict]:
        """
        Allows overriding user agent with the given string.

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
        res = await self.chrome.send('Emulation.setUserAgentOverride', msg_dict)
        return res

    def virtualTimeAdvanced(self, fn, once=False):
        if once:
            self.chrome.once("Emulation.virtualTimeAdvanced", fn)
        else:
            self.chrome.on("Emulation.virtualTimeAdvanced", fn)

    def virtualTimeBudgetExpired(self, fn, once=False):
        if once:
            self.chrome.once("Emulation.virtualTimeBudgetExpired", fn)
        else:
            self.chrome.on("Emulation.virtualTimeBudgetExpired", fn)

    def virtualTimePaused(self, fn, once=False):
        if once:
            self.chrome.once("Emulation.virtualTimePaused", fn)
        else:
            self.chrome.on("Emulation.virtualTimePaused", fn)

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return Events.EMULATION_EVENTS_TO_CLASS

