from typing import Any, List, Optional, Union
from cripy.async.protocol.page import types as Page

__all__ = [
    "FrameWithManifest",
    "ApplicationCacheResource",
    "ApplicationCacheT",
    "APPLICATIONCACHE_TYPES_TO_OBJECT"
]


class FrameWithManifest(object):
    """
    Frame identifier - manifest URL pair.
    """

    __slots__ = ["frameId", "manifestURL", "status"]

    def __init__(self, frameId: str, manifestURL: str, status: int) -> None:
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

    def __repr__(self) -> str:
        repr_args = []
        if self.frameId is not None:
            repr_args.append("frameId={!r}".format(self.frameId))
        if self.manifestURL is not None:
            repr_args.append("manifestURL={!r}".format(self.manifestURL))
        if self.status is not None:
            repr_args.append("status={!r}".format(self.status))
        return "FrameWithManifest(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['FrameWithManifest', dict]]:
        """
        Safely create FrameWithManifest from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of FrameWithManifest
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of FrameWithManifest if creation did not fail
        :rtype: Optional[Union[dict, FrameWithManifest]]
        """
        if init is not None:
            try:
                ourselves = FrameWithManifest(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['FrameWithManifest', dict]]]:
        """
        Safely create a new list FrameWithManifests from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list FrameWithManifest instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of FrameWithManifest instances if creation did not fail
        :rtype: Optional[List[Union[dict, FrameWithManifest]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FrameWithManifest.safe_create(it))
            return list_of_self
        else:
            return init


class ApplicationCacheResource(object):
    """
    Detailed application cache resource information.
    """

    __slots__ = ["url", "size", "type"]

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

    def __repr__(self) -> str:
        repr_args = []
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.size is not None:
            repr_args.append("size={!r}".format(self.size))
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        return "ApplicationCacheResource(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ApplicationCacheResource', dict]]:
        """
        Safely create ApplicationCacheResource from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ApplicationCacheResource
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ApplicationCacheResource if creation did not fail
        :rtype: Optional[Union[dict, ApplicationCacheResource]]
        """
        if init is not None:
            try:
                ourselves = ApplicationCacheResource(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ApplicationCacheResource', dict]]]:
        """
        Safely create a new list ApplicationCacheResources from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ApplicationCacheResource instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ApplicationCacheResource instances if creation did not fail
        :rtype: Optional[List[Union[dict, ApplicationCacheResource]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ApplicationCacheResource.safe_create(it))
            return list_of_self
        else:
            return init


class ApplicationCacheT(object):
    """
    Detailed application cache information.
    """

    __slots__ = ["manifestURL", "size", "creationTime", "updateTime", "resources"]

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

    def __repr__(self) -> str:
        repr_args = []
        if self.manifestURL is not None:
            repr_args.append("manifestURL={!r}".format(self.manifestURL))
        if self.size is not None:
            repr_args.append("size={!r}".format(self.size))
        if self.creationTime is not None:
            repr_args.append("creationTime={!r}".format(self.creationTime))
        if self.updateTime is not None:
            repr_args.append("updateTime={!r}".format(self.updateTime))
        if self.resources is not None:
            repr_args.append("resources={!r}".format(self.resources))
        return "ApplicationCacheT(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ApplicationCacheT', dict]]:
        """
        Safely create ApplicationCacheT from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ApplicationCacheT
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ApplicationCacheT if creation did not fail
        :rtype: Optional[Union[dict, ApplicationCacheT]]
        """
        if init is not None:
            try:
                ourselves = ApplicationCacheT(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ApplicationCacheT', dict]]]:
        """
        Safely create a new list ApplicationCacheTs from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ApplicationCacheT instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ApplicationCacheT instances if creation did not fail
        :rtype: Optional[List[Union[dict, ApplicationCacheT]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ApplicationCacheT.safe_create(it))
            return list_of_self
        else:
            return init


APPLICATIONCACHE_TYPES_TO_OBJECT = {
    "FrameWithManifest": FrameWithManifest,
    "ApplicationCacheResource": ApplicationCacheResource,
    "ApplicationCacheT": ApplicationCacheT,
}
