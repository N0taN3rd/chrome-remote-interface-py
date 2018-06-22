from cripy.gevent.protocol.dom import types as DOM
from cripy.gevent.protocol.runtime import types as Runtime

__all__ = [
    "EventListener",
    "DOMDEBUGGER_TYPE_TO_OBJECT"
]


class EventListener(object):
    """
    Object event listener.
    """

    __slots__ = ["type", "useCapture", "passive", "once", "scriptId", "lineNumber", "columnNumber", "handler", "originalHandler", "backendNodeId"]

    def __init__(self, type, useCapture, passive, once, scriptId, lineNumber, columnNumber, handler=None, originalHandler=None, backendNodeId=None):
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
        super(EventListener, self).__init__()
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
        return "EventListener(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create EventListener from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of EventListener
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of EventListener if creation did not fail
        :rtype: Optional[Union[dict, EventListener]]
        """
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
        """
        Safely create a new list EventListeners from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list EventListener instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of EventListener instances if creation did not fail
        :rtype: Optional[List[Union[dict, EventListener]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(EventListener.safe_create(it))
            return list_of_self
        else:
            return init


DOMDEBUGGER_TYPE_TO_OBJECT = {
    "EventListener": EventListener,
}
