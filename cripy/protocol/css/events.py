from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
from cripy.protocol.css.types import (
    CSSStyleSheetHeader,
    StyleSheetId,
    FontFace,
)


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
    def safe_create(init: Optional[dict]) -> Optional['FontsUpdatedEvent']:
        if init is not None:
            return FontsUpdatedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['FontsUpdatedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FontsUpdatedEvent(**it))
            return list_of_self
        else:
            return init


class MediaQueryResultChangedEvent(BaseEvent):
    """
    Fires whenever a MediaQuery result changes (for example, after a browser window has been resized.) The current implementation considers only viewport-dependent media features.
    """

    event = "CSS.mediaQueryResultChanged"

    def __init__(self, ) -> None:
        super().__init__()

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['MediaQueryResultChangedEvent']:
        if init is not None:
            return MediaQueryResultChangedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['MediaQueryResultChangedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(MediaQueryResultChangedEvent(**it))
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
    def safe_create(init: Optional[dict]) -> Optional['StyleSheetAddedEvent']:
        if init is not None:
            return StyleSheetAddedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['StyleSheetAddedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(StyleSheetAddedEvent(**it))
            return list_of_self
        else:
            return init


class StyleSheetChangedEvent(BaseEvent):
    """
    Fired whenever a stylesheet is changed as a result of the client operation.
    """

    event = "CSS.styleSheetChanged"

    def __init__(self, styleSheetId: StyleSheetId) -> None:
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        """
        super().__init__()
        self.styleSheetId = styleSheetId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['StyleSheetChangedEvent']:
        if init is not None:
            return StyleSheetChangedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['StyleSheetChangedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(StyleSheetChangedEvent(**it))
            return list_of_self
        else:
            return init


class StyleSheetRemovedEvent(BaseEvent):
    """
    Fired whenever an active document stylesheet is removed.
    """

    event = "CSS.styleSheetRemoved"

    def __init__(self, styleSheetId: StyleSheetId) -> None:
        """
        :param styleSheetId: Identifier of the removed stylesheet.
        :type styleSheetId: str
        """
        super().__init__()
        self.styleSheetId = styleSheetId

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional['StyleSheetRemovedEvent']:
        if init is not None:
            return StyleSheetRemovedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['StyleSheetRemovedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(StyleSheetRemovedEvent(**it))
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

