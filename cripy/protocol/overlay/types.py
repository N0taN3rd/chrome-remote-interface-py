from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.dom import types as DOM

# 
InspectMode = str


class HighlightConfig(ChromeTypeBase):
    """Configuration data for the highlighting of page elements."""

    def __init__(self, showInfo: Optional[bool] = None, showRulers: Optional[bool] = None, showExtensionLines: Optional[bool] = None, displayAsMaterial: Optional[bool] = None, contentColor: Optional['DOM.RGBA'] = None, paddingColor: Optional['DOM.RGBA'] = None, borderColor: Optional['DOM.RGBA'] = None, marginColor: Optional['DOM.RGBA'] = None, eventTargetColor: Optional['DOM.RGBA'] = None, shapeColor: Optional['DOM.RGBA'] = None, shapeMarginColor: Optional['DOM.RGBA'] = None, selectorList: Optional[str] = None, cssGridColor: Optional['DOM.RGBA'] = None) -> None:
        """
        :param showInfo: Whether the node info tooltip should be shown (default: false).
        :type bool:
        :param showRulers: Whether the rulers should be shown (default: false).
        :type bool:
        :param showExtensionLines: Whether the extension lines from node to the rulers should be shown (default: false).
        :type bool:
        :param displayAsMaterial: The displayAsMaterial
        :type bool:
        :param contentColor: The content box highlight fill color (default: transparent).
        :type DOM.RGBA:
        :param paddingColor: The padding highlight fill color (default: transparent).
        :type DOM.RGBA:
        :param borderColor: The border highlight fill color (default: transparent).
        :type DOM.RGBA:
        :param marginColor: The margin highlight fill color (default: transparent).
        :type DOM.RGBA:
        :param eventTargetColor: The event target element highlight fill color (default: transparent).
        :type DOM.RGBA:
        :param shapeColor: The shape outside fill color (default: transparent).
        :type DOM.RGBA:
        :param shapeMarginColor: The shape margin fill color (default: transparent).
        :type DOM.RGBA:
        :param selectorList: Selectors to highlight relevant nodes.
        :type str:
        :param cssGridColor: The grid layout color (default: transparent).
        :type DOM.RGBA:
        """
        super().__init__()
        self.showInfo: Optional[bool] = showInfo
        self.showRulers: Optional[bool] = showRulers
        self.showExtensionLines: Optional[bool] = showExtensionLines
        self.displayAsMaterial: Optional[bool] = displayAsMaterial
        self.contentColor: Optional[DOM.RGBA] = contentColor
        self.paddingColor: Optional[DOM.RGBA] = paddingColor
        self.borderColor: Optional[DOM.RGBA] = borderColor
        self.marginColor: Optional[DOM.RGBA] = marginColor
        self.eventTargetColor: Optional[DOM.RGBA] = eventTargetColor
        self.shapeColor: Optional[DOM.RGBA] = shapeColor
        self.shapeMarginColor: Optional[DOM.RGBA] = shapeMarginColor
        self.selectorList: Optional[str] = selectorList
        self.cssGridColor: Optional[DOM.RGBA] = cssGridColor


