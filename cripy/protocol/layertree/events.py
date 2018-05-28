from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class LayerPaintedEvent(BaseEvent):

    event: str = "LayerTree.layerPainted"

    def __init__(self) -> None:
        """
        :param LayerId layerId: The id of the painted layer.
        :param DOM.Rect clip: Clip rectangle.
        """
        super().__init__()


class LayerTreeDidChangeEvent(BaseEvent):

    event: str = "LayerTree.layerTreeDidChange"

    def __init__(self) -> None:
        """
        :param array layers: Layer tree, absent if not in the comspositing mode.
        """
        super().__init__()


EVENT_TO_CLASS = {
   "LayerTree.layerPainted": LayerPaintedEvent,
   "LayerTree.layerTreeDidChange": LayerTreeDidChangeEvent,
}

