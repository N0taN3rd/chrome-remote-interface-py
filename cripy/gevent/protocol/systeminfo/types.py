
__all__ = [
    "GPUInfo",
    "GPUDevice",
    "SYSTEMINFO_TYPE_TO_OBJECT"
]


class GPUInfo(object):
    """
    Provides information about the GPU(s) on the system.
    """

    __slots__ = ["devices", "auxAttributes", "featureStatus", "driverBugWorkarounds"]

    def __init__(self, devices, driverBugWorkarounds, auxAttributes=None, featureStatus=None):
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
        super(GPUInfo, self).__init__()
        self.devices = GPUDevice.safe_create_from_list(devices)
        self.auxAttributes = auxAttributes
        self.featureStatus = featureStatus
        self.driverBugWorkarounds = driverBugWorkarounds

    def __repr__(self):
        repr_args = []
        if self.devices is not None:
            repr_args.append("devices={!r}".format(self.devices))
        if self.auxAttributes is not None:
            repr_args.append("auxAttributes={!r}".format(self.auxAttributes))
        if self.featureStatus is not None:
            repr_args.append("featureStatus={!r}".format(self.featureStatus))
        if self.driverBugWorkarounds is not None:
            repr_args.append("driverBugWorkarounds={!r}".format(self.driverBugWorkarounds))
        return "GPUInfo(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create GPUInfo from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of GPUInfo
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of GPUInfo if creation did not fail
        :rtype: Optional[Union[dict, GPUInfo]]
        """
        if init is not None:
            try:
                ourselves = GPUInfo(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list GPUInfos from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list GPUInfo instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of GPUInfo instances if creation did not fail
        :rtype: Optional[List[Union[dict, GPUInfo]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(GPUInfo.safe_create(it))
            return list_of_self
        else:
            return init


class GPUDevice(object):
    """
    Describes a single graphics processor (GPU).
    """

    __slots__ = ["vendorId", "deviceId", "vendorString", "deviceString"]

    def __init__(self, vendorId, deviceId, vendorString, deviceString):
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
        super(GPUDevice, self).__init__()
        self.vendorId = vendorId
        self.deviceId = deviceId
        self.vendorString = vendorString
        self.deviceString = deviceString

    def __repr__(self):
        repr_args = []
        if self.vendorId is not None:
            repr_args.append("vendorId={!r}".format(self.vendorId))
        if self.deviceId is not None:
            repr_args.append("deviceId={!r}".format(self.deviceId))
        if self.vendorString is not None:
            repr_args.append("vendorString={!r}".format(self.vendorString))
        if self.deviceString is not None:
            repr_args.append("deviceString={!r}".format(self.deviceString))
        return "GPUDevice(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create GPUDevice from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of GPUDevice
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of GPUDevice if creation did not fail
        :rtype: Optional[Union[dict, GPUDevice]]
        """
        if init is not None:
            try:
                ourselves = GPUDevice(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list GPUDevices from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list GPUDevice instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of GPUDevice instances if creation did not fail
        :rtype: Optional[List[Union[dict, GPUDevice]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(GPUDevice.safe_create(it))
            return list_of_self
        else:
            return init


SYSTEMINFO_TYPE_TO_OBJECT = {
    "GPUInfo": GPUInfo,
    "GPUDevice": GPUDevice,
}
