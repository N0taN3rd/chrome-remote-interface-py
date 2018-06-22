from typing import Any, List, Optional, Union

__all__ = [
    "TargetInfo",
    "RemoteLocation",
    "TARGET_TYPES_TO_OBJECT"
]


class TargetInfo(object):
    __slots__ = ["targetId", "type", "title", "url", "attached", "openerId", "browserContextId"]

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

    def __repr__(self) -> str:
        repr_args = []
        if self.targetId is not None:
            repr_args.append("targetId={!r}".format(self.targetId))
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        if self.title is not None:
            repr_args.append("title={!r}".format(self.title))
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.attached is not None:
            repr_args.append("attached={!r}".format(self.attached))
        if self.openerId is not None:
            repr_args.append("openerId={!r}".format(self.openerId))
        if self.browserContextId is not None:
            repr_args.append("browserContextId={!r}".format(self.browserContextId))
        return "TargetInfo(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['TargetInfo', dict]]:
        """
        Safely create TargetInfo from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of TargetInfo
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of TargetInfo if creation did not fail
        :rtype: Optional[Union[dict, TargetInfo]]
        """
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
        """
        Safely create a new list TargetInfos from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list TargetInfo instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of TargetInfo instances if creation did not fail
        :rtype: Optional[List[Union[dict, TargetInfo]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(TargetInfo.safe_create(it))
            return list_of_self
        else:
            return init


class RemoteLocation(object):
    __slots__ = ["host", "port"]

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

    def __repr__(self) -> str:
        repr_args = []
        if self.host is not None:
            repr_args.append("host={!r}".format(self.host))
        if self.port is not None:
            repr_args.append("port={!r}".format(self.port))
        return "RemoteLocation(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['RemoteLocation', dict]]:
        """
        Safely create RemoteLocation from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of RemoteLocation
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of RemoteLocation if creation did not fail
        :rtype: Optional[Union[dict, RemoteLocation]]
        """
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
        """
        Safely create a new list RemoteLocations from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list RemoteLocation instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of RemoteLocation instances if creation did not fail
        :rtype: Optional[List[Union[dict, RemoteLocation]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(RemoteLocation.safe_create(it))
            return list_of_self
        else:
            return init


TARGET_TYPES_TO_OBJECT = {
    "TargetInfo": TargetInfo,
    "RemoteLocation": RemoteLocation,
}
