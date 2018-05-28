from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent
from cripy.protocol.dom import types as DOM
from cripy.protocol.layertree.types import (
    LayerId,
)


class LayerPaintedEvent(BaseEvent):

    event: str = "LayerTree.layerPainted"

    def __init__(self, layerId: LayerId, clip: DOM.Rect) -> None:
        """
        :param layerId: The id of the painted layer.
        :type layerId: LayerId
        :param clip: Clip rectangle.
        :type clip: DOM.Rect
        """
        super().__init__()
        self.layerId: LayerId = layerId
        self.clip: DOM.Rect = clip


class LayerTreeDidChangeEvent(BaseEvent):

    event: str = "LayerTree.layerTreeDidChange"

    def __init__(self, layers: Optional[List[Layer]] = None) -> None:
        """
        :param layers: Layer tree, absent if not in the comspositing mode.
        :type layers: array
        """
        super().__init__()
        self.layers: Optional[List[Layer]] = layers


EVENT_TO_CLASS = {
   "LayerTree.layerPainted": LayerPaintedEvent,
   "LayerTree.layerTreeDidChange": LayerTreeDidChangeEvent,
}

