from typing import Any, List, Optional, Set, Union, TypeVar
from cripy.helpers import ProtocolType


class GPUInfo(ProtocolType):
    """Provides information about the GPU(s) on the system."""

    def __init__(
        self,
        devices: List[Union["GPUDevice", dict]],
        driverBugWorkarounds: List[str],
        auxAttributes: Optional[dict] = None,
        featureStatus: Optional[dict] = None,
    ) -> None:
        """
        :param devices: The graphics devices on the system. Element 0 is the primary GPU.
        :type devices: array
        :param auxAttributes: An optional dictionary of additional GPU related attributes.
        :type auxAttributes: dict
        :param featureStatus: An optional dictionary of graphics features and their status.
        :type featureStatus: dict
        :param driverBugWorkarounds: An optional array of GPU driver bug workarounds.
        :type driverBugWorkarounds: array
        """
        super().__init__()
        self.devices: List[GPUDevice] = devices
        self.auxAttributes: Optional[dict] = auxAttributes
        self.featureStatus: Optional[dict] = featureStatus
        self.driverBugWorkarounds: List[str] = driverBugWorkarounds


class GPUDevice(ProtocolType):
    """Describes a single graphics processor (GPU)."""

    def __init__(
        self, vendorId: float, deviceId: float, vendorString: str, deviceString: str
    ) -> None:
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
        self.vendorId: float = vendorId
        self.deviceId: float = deviceId
        self.vendorString: str = vendorString
        self.deviceString: str = deviceString


OBJECT_LIST = {"GPUInfo": GPUInfo, "GPUDevice": GPUDevice}
