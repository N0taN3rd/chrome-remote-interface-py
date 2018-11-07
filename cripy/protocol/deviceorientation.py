# -*- coding: utf-8 -*-
"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy.types import ConnectionType, SessionType

__all__ = ["DeviceOrientation"]


@attr.dataclass(slots=True)
class DeviceOrientation(object):
    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def clearDeviceOrientationOverride(self) -> Awaitable[Optional[dict]]:
        """
        Clears the overridden Device Orientation.
        """
        return self.client.send("DeviceOrientation.clearDeviceOrientationOverride")

    def setDeviceOrientationOverride(
        self, alpha: float, beta: float, gamma: float
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send(
            "DeviceOrientation.setDeviceOrientationOverride", msg_dict
        )
