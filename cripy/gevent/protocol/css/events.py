from types import SimpleNamespace

try:
    from cripy.gevent.protocol.css.types import *
except ImportError:
    pass

__all__ = [
    "FontsUpdatedEvent",
    "MediaQueryResultChangedEvent",
    "StyleSheetAddedEvent",
    "StyleSheetChangedEvent",
    "StyleSheetRemovedEvent",
]


class FontsUpdatedEvent(object):
    """
    Fires whenever a web font is updated.
	 A non-empty font parameter indicates a successfully loaded web font
    """

    event = "CSS.fontsUpdated"

    def __init__(self, font=None):
        """
        :param font: The web font that has loaded.
        :type font: Optional[dict]
        """
        super().__init__()
        self.font = FontFace.safe_create(font)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.font is not None:
            repr_args.append("font={!r}".format(self.font))
        return "FontsUpdatedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = FontsUpdatedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(FontsUpdatedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class MediaQueryResultChangedEvent(dict):
    """
    Fires whenever a MediaQuery result changes (for example, after a browser window has been resized.) The current implementation considers only viewport-dependent media features.
    """

    event = "CSS.mediaQueryResultChanged"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return "MediaQueryResultChangedEvent(dict)"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = MediaQueryResultChangedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(MediaQueryResultChangedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class StyleSheetAddedEvent(object):
    """
    Fired whenever an active document stylesheet is added.
    """

    event = "CSS.styleSheetAdded"

    def __init__(self, header):
        """
        :param header: Added stylesheet metainfo.
        :type header: dict
        """
        super().__init__()
        self.header = CSSStyleSheetHeader.safe_create(header)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.header is not None:
            repr_args.append("header={!r}".format(self.header))
        return "StyleSheetAddedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = StyleSheetAddedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(StyleSheetAddedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class StyleSheetChangedEvent(object):
    """
    Fired whenever a stylesheet is changed as a result of the client operation.
    """

    event = "CSS.styleSheetChanged"

    def __init__(self, styleSheetId):
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        """
        super().__init__()
        self.styleSheetId = styleSheetId

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.styleSheetId is not None:
            repr_args.append("styleSheetId={!r}".format(self.styleSheetId))
        return "StyleSheetChangedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = StyleSheetChangedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(StyleSheetChangedEvent.safe_create(it))
            return list_of_self
        else:
            return init


class StyleSheetRemovedEvent(object):
    """
    Fired whenever an active document stylesheet is removed.
    """

    event = "CSS.styleSheetRemoved"

    def __init__(self, styleSheetId):
        """
        :param styleSheetId: Identifier of the removed stylesheet.
        :type styleSheetId: str
        """
        super().__init__()
        self.styleSheetId = styleSheetId

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.styleSheetId is not None:
            repr_args.append("styleSheetId={!r}".format(self.styleSheetId))
        return "StyleSheetRemovedEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = StyleSheetRemovedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
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

EVENT_NS = SimpleNamespace(
    FontsUpdated="CSS.fontsUpdated",
    MediaQueryResultChanged="CSS.mediaQueryResultChanged",
    StyleSheetAdded="CSS.styleSheetAdded",
    StyleSheetChanged="CSS.styleSheetChanged",
    StyleSheetRemoved="CSS.styleSheetRemoved",
)
