from cripy.sync.protocol.page import types as Page

__all__ = [
    "FrameWithManifest",
    "ApplicationCacheResource",
    "ApplicationCache",
]


class FrameWithManifest(object):
    """
    Frame identifier - manifest URL pair.
    """

    def __init__(self, frameId, manifestURL, status):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.frameId is not None:
            repr_args.append("frameId={!r}".format(self.frameId))
        if self.manifestURL is not None:
            repr_args.append("manifestURL={!r}".format(self.manifestURL))
        if self.status is not None:
            repr_args.append("status={!r}".format(self.status))
        return "FrameWithManifest(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = FrameWithManifest(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
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

    def __init__(self, url, size, type):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.size is not None:
            repr_args.append("size={!r}".format(self.size))
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        return "ApplicationCacheResource(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = ApplicationCacheResource(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ApplicationCacheResource.safe_create(it))
            return list_of_self
        else:
            return init


class ApplicationCache(object):
    """
    Detailed application cache information.
    """

    def __init__(self, manifestURL, size, creationTime, updateTime, resources):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
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
        return "ApplicationCache(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = ApplicationCache(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ApplicationCache.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "FrameWithManifest": FrameWithManifest,
    "ApplicationCacheResource": ApplicationCacheResource,
    "ApplicationCache": ApplicationCache,
}
