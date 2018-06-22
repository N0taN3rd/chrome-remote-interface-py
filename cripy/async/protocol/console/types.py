from typing import Any, List, Optional, Union

__all__ = [
    "ConsoleMessage",
    "CONSOLE_TYPES_TO_OBJECT"
]


class ConsoleMessage(object):
    """
    Console message.
    """

    __slots__ = ["source", "level", "text", "url", "line", "column"]

    def __init__(self, source: str, level: str, text: str, url: Optional[str] = None, line: Optional[int] = None, column: Optional[int] = None) -> None:
        """
        :param source: Message source.
        :type source: str
        :param level: Message severity.
        :type level: str
        :param text: Message text.
        :type text: str
        :param url: URL of the message origin.
        :type url: Optional[str]
        :param line: Line number in the resource that generated this message (1-based).
        :type line: Optional[int]
        :param column: Column number in the resource that generated this message (1-based).
        :type column: Optional[int]
        """
        super().__init__()
        self.source = source
        self.level = level
        self.text = text
        self.url = url
        self.line = line
        self.column = column

    def __repr__(self) -> str:
        repr_args = []
        if self.source is not None:
            repr_args.append("source={!r}".format(self.source))
        if self.level is not None:
            repr_args.append("level={!r}".format(self.level))
        if self.text is not None:
            repr_args.append("text={!r}".format(self.text))
        if self.url is not None:
            repr_args.append("url={!r}".format(self.url))
        if self.line is not None:
            repr_args.append("line={!r}".format(self.line))
        if self.column is not None:
            repr_args.append("column={!r}".format(self.column))
        return "ConsoleMessage(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ConsoleMessage', dict]]:
        """
        Safely create ConsoleMessage from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ConsoleMessage
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ConsoleMessage if creation did not fail
        :rtype: Optional[Union[dict, ConsoleMessage]]
        """
        if init is not None:
            try:
                ourselves = ConsoleMessage(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ConsoleMessage', dict]]]:
        """
        Safely create a new list ConsoleMessages from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ConsoleMessage instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ConsoleMessage instances if creation did not fail
        :rtype: Optional[List[Union[dict, ConsoleMessage]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ConsoleMessage.safe_create(it))
            return list_of_self
        else:
            return init


CONSOLE_TYPES_TO_OBJECT = {
    "ConsoleMessage": ConsoleMessage,
}
