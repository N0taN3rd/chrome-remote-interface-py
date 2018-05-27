from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase


class GPUDevice(ChromeTypeBase):

    def __init__(
        self, vendorId: float, deviceId: float, vendorString: str, deviceString: str
    ) -> None:
        super().__init__()
        self.vendorId: float = vendorId
        self.deviceId: float = deviceId
        self.vendorString: str = vendorString
        self.deviceString: str = deviceString


class GPUInfo(ChromeTypeBase):

    def __init__(
        self,
        devices: List["GPUDevice"],
        driverBugWorkarounds: List["str"],
        auxAttributes: Optional[dict] = None,
        featureStatus: Optional[dict] = None,
    ) -> None:
        super().__init__()
        self.devices: List[GPUDevice] = devices
        self.auxAttributes: Optional[dict] = auxAttributes
        self.featureStatus: Optional[dict] = featureStatus
        self.driverBugWorkarounds: List[str] = driverBugWorkarounds
