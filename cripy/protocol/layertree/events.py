from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
from cripy.protocol.dom import types as DOM
from cripy.protocol.layertree.types import (
    LayerId,
)


class LayerPaintedEvent(BaseEvent):

    event = "LayerTree.layerPainted"

    def __init__(self, layerId: LayerId, clip: Union[DOM.Rect, dict]) -> None:
        """
        :param layerId: The id of the painted layer.
        :type layerId: str
        :param clip: Clip rectangle.
        :type clip: dict
        """
        super().__init__()
        self.layerId = layerId
        self.clip = DOM.Rect.safe_create(clip)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['LayerPaintedEvent']:
        if init is not None:
            return LayerPaintedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['LayerPaintedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LayerPaintedEvent(**it))
            return list_of_self
        else:
            return init


class LayerTreeDidChangeEvent(BaseEvent):

    event = "LayerTree.layerTreeDidChange"

    def __init__(self, layers: Optional[List[Union[Layer, dict]]] = None) -> None:
        """
        :param layers: Layer tree, absent if not in the comspositing mode.
        :type layers: Optional[List[dict]]
        """
        super().__init__()
        self.layers = Layer.safe_create_from_list(layers)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['LayerTreeDidChangeEvent']:
        if init is not None:
            return LayerTreeDidChangeEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['LayerTreeDidChangeEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(LayerTreeDidChangeEvent(**it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "LayerTree.layerPainted": LayerPaintedEvent,
   "LayerTree.layerTreeDidChange": LayerTreeDidChangeEvent,
}

