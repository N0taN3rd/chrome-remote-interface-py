from typing import Any, List, Optional, Union
from types import SimpleNamespace
from cripy.async.protocol.dom import types as DOM

try:
    from cripy.async.protocol.layertree.types import *
except ImportError:
    pass


class LayerPaintedEvent(object):

    event = "LayerTree.layerPainted"

    def __init__(self, layerId: str, clip: Union[DOM.Rect, dict]) -> None:
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

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.layerId is not None:
            repr_args.append("layerId={!r}".format(self.layerId))
        if self.clip is not None:
            repr_args.append("clip={!r}".format(self.clip))
        return "LayerPaintedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["LayerPaintedEvent", dict]]:
        if init is not None:
            try:
                ourselves = LayerPaintedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["LayerPaintedEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LayerPaintedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class LayerTreeDidChangeEvent(object):

    event = "LayerTree.layerTreeDidChange"

    def __init__(self, layers: Optional[List[Union[Layer, dict]]] = None) -> None:
        """
        :param layers: Layer tree, absent if not in the comspositing mode.
        :type layers: Optional[List[dict]]
        """
        super().__init__()
        self.layers = Layer.safe_create_from_list(layers)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.layers is not None:
            repr_args.append("layers={!r}".format(self.layers))
        return "LayerTreeDidChangeEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(
        init: Optional[dict]
    ) -> Optional[Union["LayerTreeDidChangeEvent", dict]]:
        if init is not None:
            try:
                ourselves = LayerTreeDidChangeEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["LayerTreeDidChangeEvent", dict]]]:
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
