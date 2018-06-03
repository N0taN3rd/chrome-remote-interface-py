from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType


class TargetInfo(ProtocolType):
    def __init__(self, targetId: str, type: str, title: str, url: str, attached: bool, openerId: Optional[str] = None, browserContextId: Optional[str] = None) -> None:
        """
        :param targetId: The targetId
        :type targetId: str
        :param type: The type
        :type type: str
        :param title: The title
        :type title: str
        :param url: The url
        :type url: str
        :param attached: Whether the target has an attached client.
        :type attached: bool
        :param openerId: Opener target Id
        :type openerId: Optional[str]
        :param browserContextId: The browserContextId
        :type browserContextId: Optional[str]
        """
        super().__init__()
        self.targetId = targetId
        self.type = type
        self.title = title
        self.url = url
        self.attached = attached
        self.openerId = openerId
        self.browserContextId = browserContextId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['TargetInfo', dict]]:
        if init is not None:
            try:
                ourselves = TargetInfo(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['TargetInfo', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TargetInfo.safe_create(it))
            return list_of_self
        else:
            return init


class RemoteLocation(ProtocolType):
    def __init__(self, host: str, port: int) -> None:
        """
        :param host: The host
        :type host: str
        :param port: The port
        :type port: int
        """
        super().__init__()
        self.host = host
        self.port = port

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['RemoteLocation', dict]]:
        if init is not None:
            try:
                ourselves = RemoteLocation(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['RemoteLocation', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(RemoteLocation.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "TargetInfo": TargetInfo,
    "RemoteLocation": RemoteLocation,
}
