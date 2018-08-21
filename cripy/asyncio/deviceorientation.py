from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from .client import Client

__all__ = ["DeviceOrientation"]


@attr.dataclass(slots=True)
class DeviceOrientation(object):
    client: "Client" = attr.ib(repr=False)

    async def clearDeviceOrientationOverride(self) -> Optional[dict]:
        """
        Clears the overridden Device Orientation.
        """
        res = await self.client.send("DeviceOrientation.clearDeviceOrientationOverride")
        return res

    async def setDeviceOrientationOverride(
        self, alpha: float, beta: float, gamma: float
    ) -> Optional[dict]:
        """
        Overrides the Device Orientation.

        :param alpha: Mock alpha
        :type alpha: float
        :param beta: Mock beta
        :type beta: float
        :param gamma: Mock gamma
        :type gamma: float
        """
        msg_dict = dict()
        if alpha is not None:
            msg_dict["alpha"] = alpha
        if beta is not None:
            msg_dict["beta"] = beta
        if gamma is not None:
            msg_dict["gamma"] = gamma
        res = await self.client.send(
            "DeviceOrientation.setDeviceOrientationOverride", msg_dict
        )
        return res
