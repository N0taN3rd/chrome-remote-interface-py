from typing import Any, List, Optional, Union

__all__ = [
    "ScreenOrientation",
    "EMULATION_TYPES_TO_OBJECT"
]


class ScreenOrientation(object):
    """
    Screen orientation.
    """

    __slots__ = ["type", "angle"]

    def __init__(self, type: str, angle: int) -> None:
        """
        :param type: Orientation type.
        :type type: str
        :param angle: Orientation angle.
        :type angle: int
        """
        super().__init__()
        self.type = type
        self.angle = angle

    def __repr__(self) -> str:
        repr_args = []
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        if self.angle is not None:
            repr_args.append("angle={!r}".format(self.angle))
        return "ScreenOrientation(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ScreenOrientation', dict]]:
        """
        Safely create ScreenOrientation from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of ScreenOrientation
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of ScreenOrientation if creation did not fail
        :rtype: Optional[Union[dict, ScreenOrientation]]
        """
        if init is not None:
            try:
                ourselves = ScreenOrientation(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ScreenOrientation', dict]]]:
        """
        Safely create a new list ScreenOrientations from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list ScreenOrientation instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of ScreenOrientation instances if creation did not fail
        :rtype: Optional[List[Union[dict, ScreenOrientation]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ScreenOrientation.safe_create(it))
            return list_of_self
        else:
            return init


EMULATION_TYPES_TO_OBJECT = {
    "ScreenOrientation": ScreenOrientation,
}
