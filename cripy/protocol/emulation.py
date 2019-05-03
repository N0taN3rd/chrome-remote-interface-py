"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Emulation"]


class Emulation:
    """
    This domain emulates different environments for the page.
     
    Domain Dependencies: 
      * DOM
      * Page
      * Runtime
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/Emulation`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of Emulation

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def canEmulate(self) -> Awaitable[Dict]:
        """
        Tells whether emulation is supported.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-canEmulate`

        :return: The results of the command
        """
        return self.client.send("Emulation.canEmulate", {})

    def clearDeviceMetricsOverride(self) -> Awaitable[Dict]:
        """
        Clears the overriden device metrics.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-clearDeviceMetricsOverride`

        :return: The results of the command
        """
        return self.client.send("Emulation.clearDeviceMetricsOverride", {})

    def clearGeolocationOverride(self) -> Awaitable[Dict]:
        """
        Clears the overriden Geolocation Position and Error.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-clearGeolocationOverride`

        :return: The results of the command
        """
        return self.client.send("Emulation.clearGeolocationOverride", {})

    def resetPageScaleFactor(self) -> Awaitable[Dict]:
        """
        Requests that page scale factor is reset to initial values.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-resetPageScaleFactor`

        :return: The results of the command
        """
        return self.client.send("Emulation.resetPageScaleFactor", {})

    def setFocusEmulationEnabled(self, enabled: bool) -> Awaitable[Dict]:
        """
        Enables or disables simulating a focused and active page.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setFocusEmulationEnabled`

        :param enabled: Whether to enable to disable focus emulation.
        :return: The results of the command
        """
        return self.client.send(
            "Emulation.setFocusEmulationEnabled", {"enabled": enabled}
        )

    def setCPUThrottlingRate(self, rate: Union[int, float]) -> Awaitable[Dict]:
        """
        Enables CPU throttling to emulate slow CPUs.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setCPUThrottlingRate`

        :param rate: Throttling rate as a slowdown factor (1 is no throttle, 2 is 2x slowdown, etc).
        :return: The results of the command
        """
        return self.client.send("Emulation.setCPUThrottlingRate", {"rate": rate})

    def setDefaultBackgroundColorOverride(
        self, color: Optional[Dict[str, Any]] = None
    ) -> Awaitable[Dict]:
        """
        Sets or clears an override of the default background color of the frame. This override is used
        if the content does not specify one.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setDefaultBackgroundColorOverride`

        :param color: RGBA of the default background color. If not specified, any existing override will be
         cleared.
        :return: The results of the command
        """
        msg = {}
        if color is not None:
            msg["color"] = color
        return self.client.send("Emulation.setDefaultBackgroundColorOverride", msg)

    def setDeviceMetricsOverride(
        self,
        width: int,
        height: int,
        deviceScaleFactor: Union[int, float],
        mobile: bool,
        scale: Optional[Union[int, float]] = None,
        screenWidth: Optional[int] = None,
        screenHeight: Optional[int] = None,
        positionX: Optional[int] = None,
        positionY: Optional[int] = None,
        dontSetVisibleSize: Optional[bool] = None,
        screenOrientation: Optional[Dict[str, Any]] = None,
        viewport: Optional[Dict[str, Any]] = None,
    ) -> Awaitable[Dict]:
        """
        Overrides the values of device screen dimensions (window.screen.width, window.screen.height,
        window.innerWidth, window.innerHeight, and "device-width"/"device-height"-related CSS media
        query results).

        See `https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setDeviceMetricsOverride`

        :param width: Overriding width value in pixels (minimum 0, maximum 10000000). 0 disables the override.
        :param height: Overriding height value in pixels (minimum 0, maximum 10000000). 0 disables the override.
        :param deviceScaleFactor: Overriding device scale factor value. 0 disables the override.
        :param mobile: Whether to emulate mobile device. This includes viewport meta tag, overlay scrollbars, text
         autosizing and more.
        :param scale: Scale to apply to resulting view image.
        :param screenWidth: Overriding screen width value in pixels (minimum 0, maximum 10000000).
        :param screenHeight: Overriding screen height value in pixels (minimum 0, maximum 10000000).
        :param positionX: Overriding view X position on screen in pixels (minimum 0, maximum 10000000).
        :param positionY: Overriding view Y position on screen in pixels (minimum 0, maximum 10000000).
        :param dontSetVisibleSize: Do not set visible view size, rely upon explicit setVisibleSize call.
        :param screenOrientation: Screen orientation override.
        :param viewport: If set, the visible area of the page will be overridden to this viewport. This viewport
         change is not observed by the page, e.g. viewport-relative elements do not change positions.
        :return: The results of the command
        """
        msg = {
            "width": width,
            "height": height,
            "deviceScaleFactor": deviceScaleFactor,
            "mobile": mobile,
        }
        if scale is not None:
            msg["scale"] = scale
        if screenWidth is not None:
            msg["screenWidth"] = screenWidth
        if screenHeight is not None:
            msg["screenHeight"] = screenHeight
        if positionX is not None:
            msg["positionX"] = positionX
        if positionY is not None:
            msg["positionY"] = positionY
        if dontSetVisibleSize is not None:
            msg["dontSetVisibleSize"] = dontSetVisibleSize
        if screenOrientation is not None:
            msg["screenOrientation"] = screenOrientation
        if viewport is not None:
            msg["viewport"] = viewport
        return self.client.send("Emulation.setDeviceMetricsOverride", msg)

    def setScrollbarsHidden(self, hidden: bool) -> Awaitable[Dict]:
        """
        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setScrollbarsHidden`

        :param hidden: Whether scrollbars should be always hidden.
        :return: The results of the command
        """
        return self.client.send("Emulation.setScrollbarsHidden", {"hidden": hidden})

    def setDocumentCookieDisabled(self, disabled: bool) -> Awaitable[Dict]:
        """
        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setDocumentCookieDisabled`

        :param disabled: Whether document.coookie API should be disabled.
        :return: The results of the command
        """
        return self.client.send(
            "Emulation.setDocumentCookieDisabled", {"disabled": disabled}
        )

    def setEmitTouchEventsForMouse(
        self, enabled: bool, configuration: Optional[str] = None
    ) -> Awaitable[Dict]:
        """
        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setEmitTouchEventsForMouse`

        :param enabled: Whether touch emulation based on mouse input should be enabled.
        :param configuration: Touch/gesture events configuration. Default: current platform.
        :return: The results of the command
        """
        msg = {"enabled": enabled}
        if configuration is not None:
            msg["configuration"] = configuration
        return self.client.send("Emulation.setEmitTouchEventsForMouse", msg)

    def setEmulatedMedia(self, media: str) -> Awaitable[Dict]:
        """
        Emulates the given media for CSS media queries.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setEmulatedMedia`

        :param media: Media type to emulate. Empty string disables the override.
        :return: The results of the command
        """
        return self.client.send("Emulation.setEmulatedMedia", {"media": media})

    def setGeolocationOverride(
        self,
        latitude: Optional[Union[int, float]] = None,
        longitude: Optional[Union[int, float]] = None,
        accuracy: Optional[Union[int, float]] = None,
    ) -> Awaitable[Dict]:
        """
        Overrides the Geolocation Position or Error. Omitting any of the parameters emulates position
        unavailable.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setGeolocationOverride`

        :param latitude: Mock latitude
        :param longitude: Mock longitude
        :param accuracy: Mock accuracy
        :return: The results of the command
        """
        msg = {}
        if latitude is not None:
            msg["latitude"] = latitude
        if longitude is not None:
            msg["longitude"] = longitude
        if accuracy is not None:
            msg["accuracy"] = accuracy
        return self.client.send("Emulation.setGeolocationOverride", msg)

    def setNavigatorOverrides(self, platform: str) -> Awaitable[Dict]:
        """
        Overrides value returned by the javascript navigator object.

        Status: Deprecated and Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setNavigatorOverrides`

        :param platform: The platform navigator.platform should return.
        :return: The results of the command
        """
        return self.client.send(
            "Emulation.setNavigatorOverrides", {"platform": platform}
        )

    def setPageScaleFactor(self, pageScaleFactor: Union[int, float]) -> Awaitable[Dict]:
        """
        Sets a specified page scale factor.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setPageScaleFactor`

        :param pageScaleFactor: Page scale factor.
        :return: The results of the command
        """
        return self.client.send(
            "Emulation.setPageScaleFactor", {"pageScaleFactor": pageScaleFactor}
        )

    def setScriptExecutionDisabled(self, value: bool) -> Awaitable[Dict]:
        """
        Switches script execution in the page.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setScriptExecutionDisabled`

        :param value: Whether script execution should be disabled in the page.
        :return: The results of the command
        """
        return self.client.send(
            "Emulation.setScriptExecutionDisabled", {"value": value}
        )

    def setTouchEmulationEnabled(
        self, enabled: bool, maxTouchPoints: Optional[int] = None
    ) -> Awaitable[Dict]:
        """
        Enables touch on platforms which do not support them.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setTouchEmulationEnabled`

        :param enabled: Whether the touch event emulation should be enabled.
        :param maxTouchPoints: Maximum touch points supported. Defaults to one.
        :return: The results of the command
        """
        msg = {"enabled": enabled}
        if maxTouchPoints is not None:
            msg["maxTouchPoints"] = maxTouchPoints
        return self.client.send("Emulation.setTouchEmulationEnabled", msg)

    def setVirtualTimePolicy(
        self,
        policy: str,
        budget: Optional[Union[int, float]] = None,
        maxVirtualTimeTaskStarvationCount: Optional[int] = None,
        waitForNavigation: Optional[bool] = None,
        initialVirtualTime: Optional[Union[int, float]] = None,
    ) -> Awaitable[Dict]:
        """
        Turns on virtual time for all frames (replacing real-time with a synthetic time source) and sets
        the current virtual time policy.  Note this supersedes any previous time budget.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setVirtualTimePolicy`

        :param policy: The policy
        :param budget: If set, after this many virtual milliseconds have elapsed virtual time will be paused and a
         virtualTimeBudgetExpired event is sent.
        :param maxVirtualTimeTaskStarvationCount: If set this specifies the maximum number of tasks that can be run before virtual is forced
         forwards to prevent deadlock.
        :param waitForNavigation: If set the virtual time policy change should be deferred until any frame starts navigating.
         Note any previous deferred policy change is superseded.
        :param initialVirtualTime: If set, base::Time::Now will be overriden to initially return this value.
        :return: The results of the command
        """
        msg = {"policy": policy}
        if budget is not None:
            msg["budget"] = budget
        if maxVirtualTimeTaskStarvationCount is not None:
            msg["maxVirtualTimeTaskStarvationCount"] = maxVirtualTimeTaskStarvationCount
        if waitForNavigation is not None:
            msg["waitForNavigation"] = waitForNavigation
        if initialVirtualTime is not None:
            msg["initialVirtualTime"] = initialVirtualTime
        return self.client.send("Emulation.setVirtualTimePolicy", msg)

    def setVisibleSize(self, width: int, height: int) -> Awaitable[Dict]:
        """
        Resizes the frame/viewport of the page. Note that this does not affect the frame's container
        (e.g. browser window). Can be used to produce screenshots of the specified size. Not supported
        on Android.

        Status: Deprecated and Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setVisibleSize`

        :param width: Frame width (DIP).
        :param height: Frame height (DIP).
        :return: The results of the command
        """
        return self.client.send(
            "Emulation.setVisibleSize", {"width": width, "height": height}
        )

    def setUserAgentOverride(
        self,
        userAgent: str,
        acceptLanguage: Optional[str] = None,
        platform: Optional[str] = None,
    ) -> Awaitable[Dict]:
        """
        Allows overriding user agent with the given string.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setUserAgentOverride`

        :param userAgent: User agent to use.
        :param acceptLanguage: Browser langugage to emulate.
        :param platform: The platform navigator.platform should return.
        :return: The results of the command
        """
        msg = {"userAgent": userAgent}
        if acceptLanguage is not None:
            msg["acceptLanguage"] = acceptLanguage
        if platform is not None:
            msg["platform"] = platform
        return self.client.send("Emulation.setUserAgentOverride", msg)

    def virtualTimeBudgetExpired(
        self, listener: Optional[Callable[[Any], Any]] = None
    ) -> Any:
        """
        Notification sent after the virtual time budget for the current VirtualTimePolicy has run out.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Emulation#event-virtualTimeBudgetExpired`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Emulation.virtualTimeBudgetExpired"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
