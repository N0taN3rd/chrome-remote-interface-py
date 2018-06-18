from cripy.gevent.protocol.dom import types as DOM
from cripy.gevent.protocol.runtime import types as Runtime

__all__ = ["EventListener"]


class EventListener(object):
    """
    Object event listener.
    """

    def __init__(
        self,
        type,
        useCapture,
        passive,
        once,
        scriptId,
        lineNumber,
        columnNumber,
        handler=None,
        originalHandler=None,
        backendNodeId=None,
    ):
        """
        :param type: `EventListener`'s type.
        :type type: str
        :param useCapture: `EventListener`'s useCapture.
        :type useCapture: bool
        :param passive: `EventListener`'s passive flag.
        :type passive: bool
        :param once: `EventListener`'s once flag.
        :type once: bool
        :param scriptId: Script id of the handler code.
        :type scriptId: str
        :param lineNumber: Line number in the script (0-based).
        :type lineNumber: int
        :param columnNumber: Column number in the script (0-based).
        :type columnNumber: int
        :param handler: Event handler function value.
        :type handler: Optional[dict]
        :param originalHandler: Event original handler function value.
        :type originalHandler: Optional[dict]
        :param backendNodeId: Node the listener is added to (if any).
        :type backendNodeId: Optional[int]
        """
        super().__init__()
        self.type = type
        self.useCapture = useCapture
        self.passive = passive
        self.once = once
        self.scriptId = scriptId
        self.lineNumber = lineNumber
        self.columnNumber = columnNumber
        self.handler = Runtime.RemoteObject.safe_create(handler)
        self.originalHandler = Runtime.RemoteObject.safe_create(originalHandler)
        self.backendNodeId = backendNodeId

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        if self.useCapture is not None:
            repr_args.append("useCapture={!r}".format(self.useCapture))
        if self.passive is not None:
            repr_args.append("passive={!r}".format(self.passive))
        if self.once is not None:
            repr_args.append("once={!r}".format(self.once))
        if self.scriptId is not None:
            repr_args.append("scriptId={!r}".format(self.scriptId))
        if self.lineNumber is not None:
            repr_args.append("lineNumber={!r}".format(self.lineNumber))
        if self.columnNumber is not None:
            repr_args.append("columnNumber={!r}".format(self.columnNumber))
        if self.handler is not None:
            repr_args.append("handler={!r}".format(self.handler))
        if self.originalHandler is not None:
            repr_args.append("originalHandler={!r}".format(self.originalHandler))
        if self.backendNodeId is not None:
            repr_args.append("backendNodeId={!r}".format(self.backendNodeId))
        return "EventListener(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = EventListener(**init)
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
                list_of_self.append(EventListener.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {"EventListener": EventListener}
