from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent
from cripy.protocol.css.types import (
    CSSStyleSheetHeader,
    FontFace,
    StyleSheetId,
)


class FontsUpdatedEvent(BaseEvent):
    """Fires whenever a web font is updated.
	 A non-empty font parameter indicates a successfully loaded web font"""

    event: str = "CSS.fontsUpdated"

    def __init__(self, font: Optional[FontFace] = None) -> None:
        """
        :param font: The web font that has loaded.
        :type font: FontFace
        """
        super().__init__()
        self.font: Optional[FontFace] = font


class MediaQueryResultChangedEvent(BaseEvent):
    """Fires whenever a MediaQuery result changes (for example, after a browser window has been resized.) The current implementation considers only viewport-dependent media features."""

    event: str = "CSS.mediaQueryResultChanged"

    def __init__(self, ) -> None:
        super().__init__()


class StyleSheetAddedEvent(BaseEvent):
    """Fired whenever an active document stylesheet is added."""

    event: str = "CSS.styleSheetAdded"

    def __init__(self, header: CSSStyleSheetHeader) -> None:
        """
        :param header: Added stylesheet metainfo.
        :type header: CSSStyleSheetHeader
        """
        super().__init__()
        self.header: CSSStyleSheetHeader = header


class StyleSheetChangedEvent(BaseEvent):
    """Fired whenever a stylesheet is changed as a result of the client operation."""

    event: str = "CSS.styleSheetChanged"

    def __init__(self, styleSheetId: StyleSheetId) -> None:
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: StyleSheetId
        """
        super().__init__()
        self.styleSheetId: StyleSheetId = styleSheetId


class StyleSheetRemovedEvent(BaseEvent):
    """Fired whenever an active document stylesheet is removed."""

    event: str = "CSS.styleSheetRemoved"

    def __init__(self, styleSheetId: StyleSheetId) -> None:
        """
        :param styleSheetId: Identifier of the removed stylesheet.
        :type styleSheetId: StyleSheetId
        """
        super().__init__()
        self.styleSheetId: StyleSheetId = styleSheetId


EVENT_TO_CLASS = {
   "CSS.fontsUpdated": FontsUpdatedEvent,
   "CSS.mediaQueryResultChanged": MediaQueryResultChangedEvent,
   "CSS.styleSheetAdded": StyleSheetAddedEvent,
   "CSS.styleSheetChanged": StyleSheetChangedEvent,
   "CSS.styleSheetRemoved": StyleSheetRemovedEvent,
}

