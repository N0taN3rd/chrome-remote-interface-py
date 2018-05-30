from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
try:
    from cripy.protocol.css.types import *
except ImportError:
    pass


class FontsUpdatedEvent(BaseEvent):
    """
    Fires whenever a web font is updated.
	 A non-empty font parameter indicates a successfully loaded web font
    """

    event = "CSS.fontsUpdated"

    def __init__(self, font: Optional[Union[FontFace, dict]] = None) -> None:
        """
        :param font: The web font that has loaded.
        :type font: Optional[dict]
        """
        super().__init__()
        self.font = FontFace.safe_create(font)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['FontsUpdatedEvent', dict]]:
        if init is not None:
            try:
                ourselves = FontsUpdatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['FontsUpdatedEvent', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FontsUpdatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class MediaQueryResultChangedEvent(BaseEvent, dict):
    """
    Fires whenever a MediaQuery result changes (for example, after a browser window has been resized.) The current implementation considers only viewport-dependent media features.
    """

    event = "CSS.mediaQueryResultChanged"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['MediaQueryResultChangedEvent', dict]]:
        if init is not None:
            try:
                ourselves = MediaQueryResultChangedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['MediaQueryResultChangedEvent', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(MediaQueryResultChangedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class StyleSheetAddedEvent(BaseEvent):
    """
    Fired whenever an active document stylesheet is added.
    """

    event = "CSS.styleSheetAdded"

    def __init__(self, header: Union[CSSStyleSheetHeader, dict]) -> None:
        """
        :param header: Added stylesheet metainfo.
        :type header: dict
        """
        super().__init__()
        self.header = CSSStyleSheetHeader.safe_create(header)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['StyleSheetAddedEvent', dict]]:
        if init is not None:
            try:
                ourselves = StyleSheetAddedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['StyleSheetAddedEvent', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(StyleSheetAddedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class StyleSheetChangedEvent(BaseEvent):
    """
    Fired whenever a stylesheet is changed as a result of the client operation.
    """

    event = "CSS.styleSheetChanged"

    def __init__(self, styleSheetId: str) -> None:
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        """
        super().__init__()
        self.styleSheetId = styleSheetId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['StyleSheetChangedEvent', dict]]:
        if init is not None:
            try:
                ourselves = StyleSheetChangedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['StyleSheetChangedEvent', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(StyleSheetChangedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class StyleSheetRemovedEvent(BaseEvent):
    """
    Fired whenever an active document stylesheet is removed.
    """

    event = "CSS.styleSheetRemoved"

    def __init__(self, styleSheetId: str) -> None:
        """
        :param styleSheetId: Identifier of the removed stylesheet.
        :type styleSheetId: str
        """
        super().__init__()
        self.styleSheetId = styleSheetId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['StyleSheetRemovedEvent', dict]]:
        if init is not None:
            try:
                ourselves = StyleSheetRemovedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['StyleSheetRemovedEvent', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(StyleSheetRemovedEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "CSS.fontsUpdated": FontsUpdatedEvent,
   "CSS.mediaQueryResultChanged": MediaQueryResultChangedEvent,
   "CSS.styleSheetAdded": StyleSheetAddedEvent,
   "CSS.styleSheetChanged": StyleSheetChangedEvent,
   "CSS.styleSheetRemoved": StyleSheetRemovedEvent,
}

