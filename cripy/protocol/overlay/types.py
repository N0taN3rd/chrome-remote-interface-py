from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.dom import types as DOM


class HighlightConfig(object):
    """
    Configuration data for the highlighting of page elements.
    """

    def __init__(
        self,
        showInfo: Optional[bool] = None,
        showRulers: Optional[bool] = None,
        showExtensionLines: Optional[bool] = None,
        displayAsMaterial: Optional[bool] = None,
        contentColor: Optional[Union["DOM.RGBA", dict]] = None,
        paddingColor: Optional[Union["DOM.RGBA", dict]] = None,
        borderColor: Optional[Union["DOM.RGBA", dict]] = None,
        marginColor: Optional[Union["DOM.RGBA", dict]] = None,
        eventTargetColor: Optional[Union["DOM.RGBA", dict]] = None,
        shapeColor: Optional[Union["DOM.RGBA", dict]] = None,
        shapeMarginColor: Optional[Union["DOM.RGBA", dict]] = None,
        selectorList: Optional[str] = None,
        cssGridColor: Optional[Union["DOM.RGBA", dict]] = None,
    ) -> None:
        """
        :param showInfo: Whether the node info tooltip should be shown (default: false).
        :type showInfo: Optional[bool]
        :param showRulers: Whether the rulers should be shown (default: false).
        :type showRulers: Optional[bool]
        :param showExtensionLines: Whether the extension lines from node to the rulers should be shown (default: false).
        :type showExtensionLines: Optional[bool]
        :param displayAsMaterial: The displayAsMaterial
        :type displayAsMaterial: Optional[bool]
        :param contentColor: The content box highlight fill color (default: transparent).
        :type contentColor: Optional[dict]
        :param paddingColor: The padding highlight fill color (default: transparent).
        :type paddingColor: Optional[dict]
        :param borderColor: The border highlight fill color (default: transparent).
        :type borderColor: Optional[dict]
        :param marginColor: The margin highlight fill color (default: transparent).
        :type marginColor: Optional[dict]
        :param eventTargetColor: The event target element highlight fill color (default: transparent).
        :type eventTargetColor: Optional[dict]
        :param shapeColor: The shape outside fill color (default: transparent).
        :type shapeColor: Optional[dict]
        :param shapeMarginColor: The shape margin fill color (default: transparent).
        :type shapeMarginColor: Optional[dict]
        :param selectorList: Selectors to highlight relevant nodes.
        :type selectorList: Optional[str]
        :param cssGridColor: The grid layout color (default: transparent).
        :type cssGridColor: Optional[dict]
        """
        super().__init__()
        self.showInfo = showInfo
        self.showRulers = showRulers
        self.showExtensionLines = showExtensionLines
        self.displayAsMaterial = displayAsMaterial
        self.contentColor = DOM.RGBA.safe_create(contentColor)
        self.paddingColor = DOM.RGBA.safe_create(paddingColor)
        self.borderColor = DOM.RGBA.safe_create(borderColor)
        self.marginColor = DOM.RGBA.safe_create(marginColor)
        self.eventTargetColor = DOM.RGBA.safe_create(eventTargetColor)
        self.shapeColor = DOM.RGBA.safe_create(shapeColor)
        self.shapeMarginColor = DOM.RGBA.safe_create(shapeMarginColor)
        self.selectorList = selectorList
        self.cssGridColor = DOM.RGBA.safe_create(cssGridColor)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.showInfo is not None:
            repr_args.append("showInfo={!r}".format(self.showInfo))
        if self.showRulers is not None:
            repr_args.append("showRulers={!r}".format(self.showRulers))
        if self.showExtensionLines is not None:
            repr_args.append("showExtensionLines={!r}".format(self.showExtensionLines))
        if self.displayAsMaterial is not None:
            repr_args.append("displayAsMaterial={!r}".format(self.displayAsMaterial))
        if self.contentColor is not None:
            repr_args.append("contentColor={!r}".format(self.contentColor))
        if self.paddingColor is not None:
            repr_args.append("paddingColor={!r}".format(self.paddingColor))
        if self.borderColor is not None:
            repr_args.append("borderColor={!r}".format(self.borderColor))
        if self.marginColor is not None:
            repr_args.append("marginColor={!r}".format(self.marginColor))
        if self.eventTargetColor is not None:
            repr_args.append("eventTargetColor={!r}".format(self.eventTargetColor))
        if self.shapeColor is not None:
            repr_args.append("shapeColor={!r}".format(self.shapeColor))
        if self.shapeMarginColor is not None:
            repr_args.append("shapeMarginColor={!r}".format(self.shapeMarginColor))
        if self.selectorList is not None:
            repr_args.append("selectorList={!r}".format(self.selectorList))
        if self.cssGridColor is not None:
            repr_args.append("cssGridColor={!r}".format(self.cssGridColor))
        return "HighlightConfig(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["HighlightConfig", dict]]:
        if init is not None:
            try:
                ourselves = HighlightConfig(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["HighlightConfig", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(HighlightConfig.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {"HighlightConfig": HighlightConfig}
