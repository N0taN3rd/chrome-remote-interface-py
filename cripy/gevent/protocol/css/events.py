from collections import namedtuple
from cripy.gevent.protocol.css.types import *

__all__ = [
    "FontsUpdatedEvent",
    "MediaQueryResultChangedEvent",
    "StyleSheetAddedEvent",
    "StyleSheetChangedEvent",
    "StyleSheetRemovedEvent",
    "CSS_EVENTS_TO_CLASS",
    "CSS_EVENTS_NS"
]


class FontsUpdatedEvent(object):
    """
    Fires whenever a web font is updated.
	 A non-empty font parameter indicates a successfully loaded web font
    """

    __slots__ = ["font"]

    def __init__(self, font=None):
        """
        Create a new instance of FontsUpdatedEvent

        :param font: The web font that has loaded.
        :type font: Optional[dict]
        """
        super(FontsUpdatedEvent, self).__init__()
        self.font = FontFace.safe_create(font)

    def __repr__(self):
        repr_args = []
        if self.font is not None:
            repr_args.append("font={!r}".format(self.font))
        return "FontsUpdatedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create FontsUpdatedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of FontsUpdatedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of FontsUpdatedEvent if creation did not fail
        :rtype: Optional[Union[dict, FontsUpdatedEvent]]
        """
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
        """
        Safely create a new list FontsUpdatedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list FontsUpdatedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of FontsUpdatedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, FontsUpdatedEvent]]]
        """
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

    def __repr__(self):
        return "MediaQueryResultChangedEvent(dict)"

    @staticmethod
    def safe_create(init):
        """
        Safely create MediaQueryResultChangedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of MediaQueryResultChangedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of MediaQueryResultChangedEvent if creation did not fail
        :rtype: Optional[Union[dict, MediaQueryResultChangedEvent]]
        """
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
        """
        Safely create a new list MediaQueryResultChangedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list MediaQueryResultChangedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of MediaQueryResultChangedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, MediaQueryResultChangedEvent]]]
        """
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

    __slots__ = ["header"]

    def __init__(self, header):
        """
        Create a new instance of StyleSheetAddedEvent

        :param header: Added stylesheet metainfo.
        :type header: dict
        """
        super(StyleSheetAddedEvent, self).__init__()
        self.header = CSSStyleSheetHeader.safe_create(header)

    def __repr__(self):
        repr_args = []
        if self.header is not None:
            repr_args.append("header={!r}".format(self.header))
        return "StyleSheetAddedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create StyleSheetAddedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of StyleSheetAddedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of StyleSheetAddedEvent if creation did not fail
        :rtype: Optional[Union[dict, StyleSheetAddedEvent]]
        """
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
        """
        Safely create a new list StyleSheetAddedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list StyleSheetAddedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of StyleSheetAddedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, StyleSheetAddedEvent]]]
        """
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

    __slots__ = ["styleSheetId"]

    def __init__(self, styleSheetId):
        """
        Create a new instance of StyleSheetChangedEvent

        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        """
        super(StyleSheetChangedEvent, self).__init__()
        self.styleSheetId = styleSheetId

    def __repr__(self):
        repr_args = []
        if self.styleSheetId is not None:
            repr_args.append("styleSheetId={!r}".format(self.styleSheetId))
        return "StyleSheetChangedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create StyleSheetChangedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of StyleSheetChangedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of StyleSheetChangedEvent if creation did not fail
        :rtype: Optional[Union[dict, StyleSheetChangedEvent]]
        """
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
        """
        Safely create a new list StyleSheetChangedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list StyleSheetChangedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of StyleSheetChangedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, StyleSheetChangedEvent]]]
        """
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

    __slots__ = ["styleSheetId"]

    def __init__(self, styleSheetId):
        """
        Create a new instance of StyleSheetRemovedEvent

        :param styleSheetId: Identifier of the removed stylesheet.
        :type styleSheetId: str
        """
        super(StyleSheetRemovedEvent, self).__init__()
        self.styleSheetId = styleSheetId

    def __repr__(self):
        repr_args = []
        if self.styleSheetId is not None:
            repr_args.append("styleSheetId={!r}".format(self.styleSheetId))
        return "StyleSheetRemovedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        """
        Safely create StyleSheetRemovedEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of StyleSheetRemovedEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of StyleSheetRemovedEvent if creation did not fail
        :rtype: Optional[Union[dict, StyleSheetRemovedEvent]]
        """
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
        """
        Safely create a new list StyleSheetRemovedEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list StyleSheetRemovedEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of StyleSheetRemovedEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, StyleSheetRemovedEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(StyleSheetRemovedEvent.safe_create(it))
            return list_of_self
        else:
            return init


CSS_EVENTS_TO_CLASS = {
   "CSS.fontsUpdated": FontsUpdatedEvent,
   "CSS.mediaQueryResultChanged": MediaQueryResultChangedEvent,
   "CSS.styleSheetAdded": StyleSheetAddedEvent,
   "CSS.styleSheetChanged": StyleSheetChangedEvent,
   "CSS.styleSheetRemoved": StyleSheetRemovedEvent,
}

CSSNS = namedtuple("CSSNS", ["FontsUpdated", "MediaQueryResultChanged", "StyleSheetAdded", "StyleSheetChanged", "StyleSheetRemoved"])

CSS_EVENTS_NS = CSSNS(
  FontsUpdated="CSS.fontsUpdated",
  MediaQueryResultChanged="CSS.mediaQueryResultChanged",
  StyleSheetAdded="CSS.styleSheetAdded",
  StyleSheetChanged="CSS.styleSheetChanged",
  StyleSheetRemoved="CSS.styleSheetRemoved",
)
