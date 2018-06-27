from collections import namedtuple
from cripy.gevent.protocol.dom import types as DOM
from cripy.gevent.protocol.layertree.types import *

__all__ = [
    "LayerPaintedEvent",
    "LayerTreeDidChangeEvent",
    "LAYERTREE_EVENTS_TO_CLASS",
    "LAYERTREE_EVENTS_NS"
]


class LayerPaintedEvent(object):
    __slots__ = ["layerId", "clip"]

    def __init__(self, layerId, clip):
        """
        Create a new instance of LayerPaintedEvent

        :param layerId: The id of the painted layer.
        :type layerId: str
        :param clip: Clip rectangle.
        :type clip: dict
        """
        super(LayerPaintedEvent, self).__init__()
        self.layerId = layerId
        self.clip = DOM.Rect.safe_create(clip)

    def __repr__(self):
        repr_args = []
        if self.layerId is not None:
            repr_args.append("layerId={!r}".format(self.layerId))
        if self.clip is not None:
            repr_args.append("clip={!r}".format(self.clip))
        return "LayerPaintedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create LayerPaintedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of LayerPaintedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of LayerPaintedEvent if creation did not fail
        :rtype: Optional[Union[dict, LayerPaintedEvent]]
        """
        if init is not None:
            try:
                ourselves = LayerPaintedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list LayerPaintedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list LayerPaintedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of LayerPaintedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, LayerPaintedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LayerPaintedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class LayerTreeDidChangeEvent(object):
    __slots__ = ["layers"]

    def __init__(self, layers=None):
        """
        Create a new instance of LayerTreeDidChangeEvent

        :param layers: Layer tree, absent if not in the comspositing mode.
        :type layers: Optional[List[dict]]
        """
        super(LayerTreeDidChangeEvent, self).__init__()
        self.layers = Layer.safe_create_from_list(layers)

    def __repr__(self):
        repr_args = []
        if self.layers is not None:
            repr_args.append("layers={!r}".format(self.layers))
        return "LayerTreeDidChangeEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create LayerTreeDidChangeEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of LayerTreeDidChangeEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of LayerTreeDidChangeEvent if creation did not fail
        :rtype: Optional[Union[dict, LayerTreeDidChangeEvent]]
        """
        if init is not None:
            try:
                ourselves = LayerTreeDidChangeEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        """
        Safely create a new list LayerTreeDidChangeEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list LayerTreeDidChangeEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of LayerTreeDidChangeEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, LayerTreeDidChangeEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LayerTreeDidChangeEvent.safe_create(it))
            return list_of_self
        else:
            return init


LAYERTREE_EVENTS_TO_CLASS = {
   "LayerTree.layerPainted": LayerPaintedEvent,
   "LayerTree.layerTreeDidChange": LayerTreeDidChangeEvent,
}

LayerTreeNS = namedtuple("LayerTreeNS", ["LayerPainted", "LayerTreeDidChange"])

LAYERTREE_EVENTS_NS = LayerTreeNS(
  LayerPainted="LayerTree.layerPainted",
  LayerTreeDidChange="LayerTree.layerTreeDidChange",
)
