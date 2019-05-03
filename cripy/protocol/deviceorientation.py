"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["DeviceOrientation"]


class DeviceOrientation:
    """
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/DeviceOrientation`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of DeviceOrientation

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def clearDeviceOrientationOverride(self) -> Awaitable[Dict]:
        """
        Clears the overridden Device Orientation.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DeviceOrientation#method-clearDeviceOrientationOverride`

        :return: The results of the command
        """
        return self.client.send("DeviceOrientation.clearDeviceOrientationOverride", {})

    def setDeviceOrientationOverride(
        self,
        alpha: Union[int, float],
        beta: Union[int, float],
        gamma: Union[int, float],
    ) -> Awaitable[Dict]:
        """
        Overrides the Device Orientation.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DeviceOrientation#method-setDeviceOrientationOverride`

        :param alpha: Mock alpha
        :param beta: Mock beta
        :param gamma: Mock gamma
        :return: The results of the command
        """
        return self.client.send(
            "DeviceOrientation.setDeviceOrientationOverride",
            {"alpha": alpha, "beta": beta, "gamma": gamma},
        )
