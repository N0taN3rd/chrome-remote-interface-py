from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType


class GPUInfo(ProtocolType):
    """
    Provides information about the GPU(s) on the system.
    """

    def __init__(self, devices: List[Union['GPUDevice', dict]], driverBugWorkarounds: List[str], auxAttributes: Optional[dict] = None, featureStatus: Optional[dict] = None) -> None:
        """
        :param devices: The graphics devices on the system. Element 0 is the primary GPU.
        :type devices: List[dict]
        :param auxAttributes: An optional dictionary of additional GPU related attributes.
        :type auxAttributes: Optional[dict]
        :param featureStatus: An optional dictionary of graphics features and their status.
        :type featureStatus: Optional[dict]
        :param driverBugWorkarounds: An optional array of GPU driver bug workarounds.
        :type driverBugWorkarounds: List[str]
        """
        super().__init__()
        self.devices = GPUDevice.safe_create_from_list(devices)
        self.auxAttributes = auxAttributes
        self.featureStatus = featureStatus
        self.driverBugWorkarounds = driverBugWorkarounds

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['GPUInfo', dict]]:
        if init is not None:
            try:
                ourselves = GPUInfo(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['GPUInfo', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(GPUInfo.safe_create(it))
            return list_of_self
        else:
            return init


class GPUDevice(ProtocolType):
    """
    Describes a single graphics processor (GPU).
    """

    def __init__(self, vendorId: float, deviceId: float, vendorString: str, deviceString: str) -> None:
        """
        :param vendorId: PCI ID of the GPU vendor, if available; 0 otherwise.
        :type vendorId: float
        :param deviceId: PCI ID of the GPU device, if available; 0 otherwise.
        :type deviceId: float
        :param vendorString: String description of the GPU vendor, if the PCI ID is not available.
        :type vendorString: str
        :param deviceString: String description of the GPU device, if the PCI ID is not available.
        :type deviceString: str
        """
        super().__init__()
        self.vendorId = vendorId
        self.deviceId = deviceId
        self.vendorString = vendorString
        self.deviceString = deviceString

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['GPUDevice', dict]]:
        if init is not None:
            try:
                ourselves = GPUDevice(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['GPUDevice', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(GPUDevice.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "GPUInfo": GPUInfo,
    "GPUDevice": GPUDevice,
}
