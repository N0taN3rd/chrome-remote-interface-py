from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType

TargetID = TypeVar("TargetID", str, str) # 

SessionID = TypeVar("SessionID", str, str) # Unique identifier of attached debugging session.

BrowserContextID = TypeVar("BrowserContextID", str, str) # 


class TargetInfo(ProtocolType):
    def __init__(self, targetId: TargetID, type: str, title: str, url: str, attached: bool, openerId: Optional[TargetID] = None, browserContextId: Optional[BrowserContextID] = None) -> None:
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
    def safe_create(init: Optional[dict]) -> Optional['TargetInfo']:
        if init is not None:
            return TargetInfo(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['TargetInfo']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TargetInfo(**it))
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
    def safe_create(init: Optional[dict]) -> Optional['RemoteLocation']:
        if init is not None:
            return RemoteLocation(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['RemoteLocation']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(RemoteLocation(**it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "TargetInfo": TargetInfo,
    "RemoteLocation": RemoteLocation,
}
