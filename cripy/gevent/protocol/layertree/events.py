from types import SimpleNamespace
from cripy.gevent.protocol.dom import types as DOM

try:
    from cripy.gevent.protocol.layertree.types import *
except ImportError:
    pass

__all__ = ["LayerPaintedEvent", "LayerTreeDidChangeEvent"]


class LayerPaintedEvent(object):

    event = "LayerTree.layerPainted"

    def __init__(self, layerId, clip):
        """
        :param layerId: The id of the painted layer.
        :type layerId: str
        :param clip: Clip rectangle.
        :type clip: dict
        """
        super().__init__()
        self.layerId = layerId
        self.clip = DOM.Rect.safe_create(clip)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.layerId is not None:
            repr_args.append("layerId={!r}".format(self.layerId))
        if self.clip is not None:
            repr_args.append("clip={!r}".format(self.clip))
        return "LayerPaintedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
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
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LayerPaintedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class LayerTreeDidChangeEvent(object):

    event = "LayerTree.layerTreeDidChange"

    def __init__(self, layers=None):
        """
        :param layers: Layer tree, absent if not in the comspositing mode.
        :type layers: Optional[List[dict]]
        """
        super().__init__()
        self.layers = layers

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.layers is not None:
            repr_args.append("layers={!r}".format(self.layers))
        return "LayerTreeDidChangeEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
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
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LayerTreeDidChangeEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
    "LayerTree.layerPainted": LayerPaintedEvent,
    "LayerTree.layerTreeDidChange": LayerTreeDidChangeEvent,
}

EVENT_NS = SimpleNamespace(
    LayerPainted="LayerTree.layerPainted",
    LayerTreeDidChange="LayerTree.layerTreeDidChange",
)
