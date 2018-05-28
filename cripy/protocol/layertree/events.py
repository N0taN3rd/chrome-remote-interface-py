from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class LayerPaintedEvent(BaseEvent):

    event: str = "LayerTree.layerPainted"

    def __init__(self) -> None:
        """
        :param layerId: The id of the painted layer.
        :type LayerId:
        :param clip: Clip rectangle.
        :type DOM.Rect:
        """
        super().__init__()


class LayerTreeDidChangeEvent(BaseEvent):

    event: str = "LayerTree.layerTreeDidChange"

    def __init__(self) -> None:
        """
        :param layers: Layer tree, absent if not in the comspositing mode.
        :type array:
        """
        super().__init__()


EVENT_TO_CLASS = {
   "LayerTree.layerPainted": LayerPaintedEvent,
   "LayerTree.layerTreeDidChange": LayerTreeDidChangeEvent,
}

