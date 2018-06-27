from cripy.gevent.protocol.network import types as Network

__all__ = [
    "VisualViewport",
    "Viewport",
    "ScreencastFrameMetadata",
    "NavigationEntry",
    "LayoutViewport",
    "FrameTree",
    "FrameResourceTree",
    "FrameResource",
    "Frame",
    "AppManifestError",
    "PAGE_TYPE_TO_OBJECT"
]


class VisualViewport(object):
    """
    Visual viewport position, dimensions, and scale.
    """

    __slots__ = ["offsetX", "offsetY", "pageX", "pageY", "clientWidth", "clientHeight", "scale"]

    def __init__(self, offsetX, offsetY, pageX, pageY, clientWidth, clientHeight, scale):
        """
        :param offsetX: Horizontal offset relative to the layout viewport (CSS pixels).
        :type offsetX: float
        :param offsetY: Vertical offset relative to the layout viewport (CSS pixels).
        :type offsetY: float
        :param pageX: Horizontal offset relative to the document (CSS pixels).
        :type pageX: float
        :param pageY: Vertical offset relative to the document (CSS pixels).
        :type pageY: float
        :param clientWidth: Width (CSS pixels), excludes scrollbar if present.
        :type clientWidth: float
        :param clientHeight: Height (CSS pixels), excludes scrollbar if present.
        :type clientHeight: float
        :param scale: Scale relative to the ideal viewport (size at width=device-width).
        :type scale: float
        """
        super(VisualViewport, self).__init__()
        self.offsetX = offsetX
        self.offsetY = offsetY
        self.pageX = pageX
        self.pageY = pageY
        self.clientWidth = clientWidth
        self.clientHeight = clientHeight
        self.scale = scale

    def __repr__(self):
        repr_args = []
        if self.offsetX is not None:
            repr_args.append("offsetX={!r}".format(self.offsetX))
        if self.offsetY is not None:
            repr_args.append("offsetY={!r}".format(self.offsetY))
        if self.pageX is not None:
            repr_args.append("pageX={!r}".format(self.pageX))
        if self.pageY is not None:
            repr_args.append("pageY={!r}".format(self.pageY))
        if self.clientWidth is not None:
            repr_args.append("clientWidth={!r}".format(self.clientWidth))
        if self.clientHeight is not None:
            repr_args.append("clientHeight={!r}".format(self.clientHeight))
        if self.scale is not None:
            repr_args.append("scale={!r}".format(self.scale))
        return "VisualViewport(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create VisualViewport from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of VisualViewport
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of VisualViewport if creation did not fail
        :rtype: Optional[Union[dict, VisualViewport]]
        """
        if init is not None:
            try:
                ourselves = VisualViewport(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list VisualViewports from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list VisualViewport instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of VisualViewport instances if creation did not fail
        :rtype: Optional[List[Union[dict, VisualViewport]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(VisualViewport.safe_create(it))
            return list_of_self
        else:
            return init


class Viewport(object):
    """
    Viewport for capturing screenshot.
    """

    __slots__ = ["x", "y", "width", "height", "scale"]

    def __init__(self, x, y, width, height, scale):
        """
        :param x: X offset in CSS pixels.
        :type x: float
        :param y: Y offset in CSS pixels
        :type y: float
        :param width: Rectangle width in CSS pixels
        :type width: float
        :param height: Rectangle height in CSS pixels
        :type height: float
        :param scale: Page scale factor.
        :type scale: float
        """
        super(Viewport, self).__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scale = scale

    def __repr__(self):
        repr_args = []
        if self.x is not None:
            repr_args.append("x={!r}".format(self.x))
        if self.y is not None:
            repr_args.append("y={!r}".format(self.y))
        if self.width is not None:
            repr_args.append("width={!r}".format(self.width))
        if self.height is not None:
            repr_args.append("height={!r}".format(self.height))
        if self.scale is not None:
            repr_args.append("scale={!r}".format(self.scale))
        return "Viewport(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create Viewport from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of Viewport
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of Viewport if creation did not fail
        :rtype: Optional[Union[dict, Viewport]]
        """
        if init is not None:
            try:
                ourselves = Viewport(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list Viewports from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list Viewport instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of Viewport instances if creation did not fail
        :rtype: Optional[List[Union[dict, Viewport]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Viewport.safe_create(it))
            return list_of_self
        else:
            return init


class ScreencastFrameMetadata(object):
    """
    Screencast frame metadata.
    """

    __slots__ = ["offsetTop", "pageScaleFactor", "deviceWidth", "deviceHeight", "scrollOffsetX", "scrollOffsetY", "timestamp"]

    def __init__(self, offsetTop, pageScaleFactor, deviceWidth, deviceHeight, scrollOffsetX, scrollOffsetY, timestamp=None):
        """
        :param offsetTop: Top offset in DIP.
        :type offsetTop: float
        :param pageScaleFactor: Page scale factor.
        :type pageScaleFactor: float
        :param deviceWidth: Device screen width in DIP.
        :type deviceWidth: float
        :param deviceHeight: Device screen height in DIP.
        :type deviceHeight: float
        :param scrollOffsetX: Position of horizontal scroll in CSS pixels.
        :type scrollOffsetX: float
        :param scrollOffsetY: Position of vertical scroll in CSS pixels.
        :type scrollOffsetY: float
        :param timestamp: Frame swap timestamp.
        :type timestamp: Optional[float]
        """
        super(ScreencastFrameMetadata, self).__init__()
        self.offsetTop = offsetTop
        self.pageScaleFactor = pageScaleFactor
        self.deviceWidth = deviceWidth
        self.deviceHeight = deviceHeight
        self.scrollOffsetX = scrollOffsetX
        self.scrollOffsetY = scrollOffsetY
        self.timestamp = timestamp

    def __repr__(self):
        repr_args = []
        if self.offsetTop is not None:
            repr_args.append("offsetTop={!r}".format(self.offsetTop))
        if self.pageScaleFactor is not None:
            repr_args.append("pageScaleFactor={!r}".format(self.pageScaleFactor))
        if self.deviceWidth is not None:
            repr_args.append("deviceWidth={!r}".format(self.deviceWidth))
        if self.deviceHeight is not None:
            repr_args.append("deviceHeight={!r}".format(self.deviceHeight))
        if self.scrollOffsetX is not None:
            repr_args.append("scrollOffsetX={!r}".format(self.scrollOffsetX))
        if self.scrollOffsetY is not None:
            repr_args.append("scrollOffsetY={!r}".format(self.scrollOffsetY))
        if self.timestamp is not None:
            repr_args.append("timestamp={!r}".format(self.timestamp))
        return "ScreencastFrameMetadata(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create ScreencastFrameMetadata from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ScreencastFrameMetadata
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ScreencastFrameMetadata if creation did not fail
        :rtype: Optional[Union[dict, ScreencastFrameMetadata]]
        """
        if init is not None:
            try:
                ourselves = ScreencastFrameMetadata(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list ScreencastFrameMetadatas from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ScreencastFrameMetadata instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ScreencastFrameMetadata instances if creation did not fail
        :rtype: Optional[List[Union[dict, ScreencastFrameMetadata]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ScreencastFrameMetadata.safe_create(it))
            return list_of_self
        else:
            return init


class NavigationEntry(object):
    """
    Navigation history entry.
    """

    __slots__ = ["id", "url", "userTypedURL", "title", "transitionType"]

    def __init__(self, id, url, userTypedURL, title, transitionType):
        """
        :param id: Unique id of the navigation history entry.
        :type id: int
        :param url: URL of the navigation history entry.
        :type url: str
        :param userTypedURL: URL that the user typed in the url bar.
        :type userTypedURL: str
        :param title: Title of the navigation history entry.
        :type title: str
        :param transitionType: Transition type.
        :type transitionType: str
        """
        super(NavigationEntry, self).__init__()
        self.id = id
        self.url = url
        self.userTypedURL = userTypedURL
        self.title = title
        self.transitionType = transitionType

    def __repr__(self):
        repr_args = []
        if self.id is not None:
            repr_args.append("id={!r}".format(self.id))
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.userTypedURL is not None:
            repr_args.append("userTypedURL={!r}".format(self.userTypedURL))
        if self.title is not None:
            repr_args.append("title={!r}".format(self.title))
        if self.transitionType is not None:
            repr_args.append("transitionType={!r}".format(self.transitionType))
        return "NavigationEntry(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create NavigationEntry from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of NavigationEntry
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of NavigationEntry if creation did not fail
        :rtype: Optional[Union[dict, NavigationEntry]]
        """
        if init is not None:
            try:
                ourselves = NavigationEntry(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list NavigationEntrys from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list NavigationEntry instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of NavigationEntry instances if creation did not fail
        :rtype: Optional[List[Union[dict, NavigationEntry]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(NavigationEntry.safe_create(it))
            return list_of_self
        else:
            return init


class LayoutViewport(object):
    """
    Layout viewport position and dimensions.
    """

    __slots__ = ["pageX", "pageY", "clientWidth", "clientHeight"]

    def __init__(self, pageX, pageY, clientWidth, clientHeight):
        """
        :param pageX: Horizontal offset relative to the document (CSS pixels).
        :type pageX: int
        :param pageY: Vertical offset relative to the document (CSS pixels).
        :type pageY: int
        :param clientWidth: Width (CSS pixels), excludes scrollbar if present.
        :type clientWidth: int
        :param clientHeight: Height (CSS pixels), excludes scrollbar if present.
        :type clientHeight: int
        """
        super(LayoutViewport, self).__init__()
        self.pageX = pageX
        self.pageY = pageY
        self.clientWidth = clientWidth
        self.clientHeight = clientHeight

    def __repr__(self):
        repr_args = []
        if self.pageX is not None:
            repr_args.append("pageX={!r}".format(self.pageX))
        if self.pageY is not None:
            repr_args.append("pageY={!r}".format(self.pageY))
        if self.clientWidth is not None:
            repr_args.append("clientWidth={!r}".format(self.clientWidth))
        if self.clientHeight is not None:
            repr_args.append("clientHeight={!r}".format(self.clientHeight))
        return "LayoutViewport(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create LayoutViewport from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of LayoutViewport
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of LayoutViewport if creation did not fail
        :rtype: Optional[Union[dict, LayoutViewport]]
        """
        if init is not None:
            try:
                ourselves = LayoutViewport(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list LayoutViewports from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list LayoutViewport instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of LayoutViewport instances if creation did not fail
        :rtype: Optional[List[Union[dict, LayoutViewport]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LayoutViewport.safe_create(it))
            return list_of_self
        else:
            return init


class FrameTree(object):
    """
    Information about the Frame hierarchy.
    """

    __slots__ = ["frame", "childFrames"]

    def __init__(self, frame, childFrames=None):
        """
        :param frame: Frame information for this tree item.
        :type frame: dict
        :param childFrames: Child frames.
        :type childFrames: Optional[List[dict]]
        """
        super(FrameTree, self).__init__()
        self.frame = Frame.safe_create(frame)
        self.childFrames = FrameTree.safe_create_from_list(childFrames)

    def __repr__(self):
        repr_args = []
        if self.frame is not None:
            repr_args.append("frame={!r}".format(self.frame))
        if self.childFrames is not None:
            repr_args.append("childFrames={!r}".format(self.childFrames))
        return "FrameTree(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create FrameTree from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of FrameTree
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of FrameTree if creation did not fail
        :rtype: Optional[Union[dict, FrameTree]]
        """
        if init is not None:
            try:
                ourselves = FrameTree(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list FrameTrees from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list FrameTree instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of FrameTree instances if creation did not fail
        :rtype: Optional[List[Union[dict, FrameTree]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FrameTree.safe_create(it))
            return list_of_self
        else:
            return init


class FrameResourceTree(object):
    """
    Information about the Frame hierarchy along with their cached resources.
    """

    __slots__ = ["frame", "childFrames", "resources"]

    def __init__(self, frame, resources, childFrames=None):
        """
        :param frame: Frame information for this tree item.
        :type frame: dict
        :param childFrames: Child frames.
        :type childFrames: Optional[List[dict]]
        :param resources: Information about frame resources.
        :type resources: List[dict]
        """
        super(FrameResourceTree, self).__init__()
        self.frame = Frame.safe_create(frame)
        self.childFrames = FrameResourceTree.safe_create_from_list(childFrames)
        self.resources = FrameResource.safe_create_from_list(resources)

    def __repr__(self):
        repr_args = []
        if self.frame is not None:
            repr_args.append("frame={!r}".format(self.frame))
        if self.childFrames is not None:
            repr_args.append("childFrames={!r}".format(self.childFrames))
        if self.resources is not None:
            repr_args.append("resources={!r}".format(self.resources))
        return "FrameResourceTree(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create FrameResourceTree from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of FrameResourceTree
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of FrameResourceTree if creation did not fail
        :rtype: Optional[Union[dict, FrameResourceTree]]
        """
        if init is not None:
            try:
                ourselves = FrameResourceTree(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list FrameResourceTrees from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list FrameResourceTree instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of FrameResourceTree instances if creation did not fail
        :rtype: Optional[List[Union[dict, FrameResourceTree]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FrameResourceTree.safe_create(it))
            return list_of_self
        else:
            return init


class FrameResource(object):
    """
    Information about the Resource on the page.
    """

    __slots__ = ["url", "type", "mimeType", "lastModified", "contentSize", "failed", "canceled"]

    def __init__(self, url, type, mimeType, lastModified=None, contentSize=None, failed=None, canceled=None):
        """
        :param url: Resource URL.
        :type url: str
        :param type: Type of this resource.
        :type type: str
        :param mimeType: Resource mimeType as determined by the browser.
        :type mimeType: str
        :param lastModified: last-modified timestamp as reported by server.
        :type lastModified: Optional[float]
        :param contentSize: Resource content size.
        :type contentSize: Optional[float]
        :param failed: True if the resource failed to load.
        :type failed: Optional[bool]
        :param canceled: True if the resource was canceled during loading.
        :type canceled: Optional[bool]
        """
        super(FrameResource, self).__init__()
        self.url = url
        self.type = type
        self.mimeType = mimeType
        self.lastModified = lastModified
        self.contentSize = contentSize
        self.failed = failed
        self.canceled = canceled

    def __repr__(self):
        repr_args = []
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        if self.mimeType is not None:
            repr_args.append("mimeType={!r}".format(self.mimeType))
        if self.lastModified is not None:
            repr_args.append("lastModified={!r}".format(self.lastModified))
        if self.contentSize is not None:
            repr_args.append("contentSize={!r}".format(self.contentSize))
        if self.failed is not None:
            repr_args.append("failed={!r}".format(self.failed))
        if self.canceled is not None:
            repr_args.append("canceled={!r}".format(self.canceled))
        return "FrameResource(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create FrameResource from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of FrameResource
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of FrameResource if creation did not fail
        :rtype: Optional[Union[dict, FrameResource]]
        """
        if init is not None:
            try:
                ourselves = FrameResource(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list FrameResources from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list FrameResource instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of FrameResource instances if creation did not fail
        :rtype: Optional[List[Union[dict, FrameResource]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FrameResource.safe_create(it))
            return list_of_self
        else:
            return init


class Frame(object):
    """
    Information about the Frame on the page.
    """

    __slots__ = ["id", "parentId", "loaderId", "name", "url", "securityOrigin", "mimeType", "unreachableUrl"]

    def __init__(self, id, loaderId, url, securityOrigin, mimeType, parentId=None, name=None, unreachableUrl=None):
        """
        :param id: Frame unique identifier.
        :type id: str
        :param parentId: Parent frame identifier.
        :type parentId: Optional[str]
        :param loaderId: Identifier of the loader associated with this frame.
        :type loaderId: str
        :param name: Frame's name as specified in the tag.
        :type name: Optional[str]
        :param url: Frame document's URL.
        :type url: str
        :param securityOrigin: Frame document's security origin.
        :type securityOrigin: str
        :param mimeType: Frame document's mimeType as determined by the browser.
        :type mimeType: str
        :param unreachableUrl: If the frame failed to load, this contains the URL that could not be loaded.
        :type unreachableUrl: Optional[str]
        """
        super(Frame, self).__init__()
        self.id = id
        self.parentId = parentId
        self.loaderId = loaderId
        self.name = name
        self.url = url
        self.securityOrigin = securityOrigin
        self.mimeType = mimeType
        self.unreachableUrl = unreachableUrl

    def __repr__(self):
        repr_args = []
        if self.id is not None:
            repr_args.append("id={!r}".format(self.id))
        if self.parentId is not None:
            repr_args.append("parentId={!r}".format(self.parentId))
        if self.loaderId is not None:
            repr_args.append("loaderId={!r}".format(self.loaderId))
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.securityOrigin is not None:
            repr_args.append("securityOrigin={!r}".format(self.securityOrigin))
        if self.mimeType is not None:
            repr_args.append("mimeType={!r}".format(self.mimeType))
        if self.unreachableUrl is not None:
            repr_args.append("unreachableUrl={!r}".format(self.unreachableUrl))
        return "Frame(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create Frame from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of Frame
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of Frame if creation did not fail
        :rtype: Optional[Union[dict, Frame]]
        """
        if init is not None:
            try:
                ourselves = Frame(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list Frames from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list Frame instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of Frame instances if creation did not fail
        :rtype: Optional[List[Union[dict, Frame]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Frame.safe_create(it))
            return list_of_self
        else:
            return init


class AppManifestError(object):
    """
    Error while paring app manifest.
    """

    __slots__ = ["message", "critical", "line", "column"]

    def __init__(self, message, critical, line, column):
        """
        :param message: Error message.
        :type message: str
        :param critical: If criticial, this is a non-recoverable parse error.
        :type critical: int
        :param line: Error line.
        :type line: int
        :param column: Error column.
        :type column: int
        """
        super(AppManifestError, self).__init__()
        self.message = message
        self.critical = critical
        self.line = line
        self.column = column

    def __repr__(self):
        repr_args = []
        if self.message is not None:
            repr_args.append("message={!r}".format(self.message))
        if self.critical is not None:
            repr_args.append("critical={!r}".format(self.critical))
        if self.line is not None:
            repr_args.append("line={!r}".format(self.line))
        if self.column is not None:
            repr_args.append("column={!r}".format(self.column))
        return "AppManifestError(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create AppManifestError from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of AppManifestError
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of AppManifestError if creation did not fail
        :rtype: Optional[Union[dict, AppManifestError]]
        """
        if init is not None:
            try:
                ourselves = AppManifestError(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list AppManifestErrors from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list AppManifestError instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of AppManifestError instances if creation did not fail
        :rtype: Optional[List[Union[dict, AppManifestError]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AppManifestError.safe_create(it))
            return list_of_self
        else:
            return init


PAGE_TYPE_TO_OBJECT = {
    "VisualViewport": VisualViewport,
    "Viewport": Viewport,
    "ScreencastFrameMetadata": ScreencastFrameMetadata,
    "NavigationEntry": NavigationEntry,
    "LayoutViewport": LayoutViewport,
    "FrameTree": FrameTree,
    "FrameResourceTree": FrameResourceTree,
    "FrameResource": FrameResource,
    "Frame": Frame,
    "AppManifestError": AppManifestError,
}
