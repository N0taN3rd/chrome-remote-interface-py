from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.page import types as Page


class FrameWithManifest(ProtocolType):
    """
    Frame identifier - manifest URL pair.
    """

    def __init__(self, frameId: Page.FrameId, manifestURL: str, status: int) -> None:
        """
        :param frameId: Frame identifier.
        :type frameId: str
        :param manifestURL: Manifest URL.
        :type manifestURL: str
        :param status: Application cache status.
        :type status: int
        """
        super().__init__()
        self.frameId = frameId
        self.manifestURL = manifestURL
        self.status = status

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['FrameWithManifest']:
        if init is not None:
            return FrameWithManifest(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['FrameWithManifest']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FrameWithManifest(**it))
            return list_of_self
        else:
            return init


class ApplicationCacheResource(ProtocolType):
    """
    Detailed application cache resource information.
    """

    def __init__(self, url: str, size: int, type: str) -> None:
        """
        :param url: Resource url.
        :type url: str
        :param size: Resource size.
        :type size: int
        :param type: Resource type.
        :type type: str
        """
        super().__init__()
        self.url = url
        self.size = size
        self.type = type

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ApplicationCacheResource']:
        if init is not None:
            return ApplicationCacheResource(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ApplicationCacheResource']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ApplicationCacheResource(**it))
            return list_of_self
        else:
            return init


class ApplicationCache(ProtocolType):
    """
    Detailed application cache information.
    """

    def __init__(self, manifestURL: str, size: float, creationTime: float, updateTime: float, resources: List[Union['ApplicationCacheResource', dict]]) -> None:
        """
        :param manifestURL: Manifest URL.
        :type manifestURL: str
        :param size: Application cache size.
        :type size: float
        :param creationTime: Application cache creation time.
        :type creationTime: float
        :param updateTime: Application cache update time.
        :type updateTime: float
        :param resources: Application cache resources.
        :type resources: List[dict]
        """
        super().__init__()
        self.manifestURL = manifestURL
        self.size = size
        self.creationTime = creationTime
        self.updateTime = updateTime
        self.resources = ApplicationCacheResource.safe_create_from_list(resources)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['ApplicationCache']:
        if init is not None:
            return ApplicationCache(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ApplicationCache']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ApplicationCache(**it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "FrameWithManifest": FrameWithManifest,
    "ApplicationCacheResource": ApplicationCacheResource,
    "ApplicationCache": ApplicationCache,
}
