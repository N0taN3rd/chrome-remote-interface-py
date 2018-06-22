from typing import Any, List, Optional, Union

__all__ = ["DeviceOrientation"]


class DeviceOrientation(object):
    def __init__(self, chrome):
        """
        Construct a new DeviceOrientation object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def clearDeviceOrientationOverride(self) -> Optional[dict]:
        """
        Clears the overridden Device Orientation.
        """
        mayberes = await self.chrome.send('DeviceOrientation.clearDeviceOrientationOverride')
        return mayberes

    async def setDeviceOrientationOverride(self, alpha: float, beta: float, gamma: float) -> Optional[dict]:
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
            msg_dict['alpha'] = alpha
        if beta is not None:
            msg_dict['beta'] = beta
        if gamma is not None:
            msg_dict['gamma'] = gamma
        mayberes = await self.chrome.send('DeviceOrientation.setDeviceOrientationOverride', msg_dict)
        return mayberes

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return None

