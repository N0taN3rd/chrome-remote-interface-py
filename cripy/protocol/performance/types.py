from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType


class Metric(ProtocolType):
    """
    Run-time execution metric.
    """

    def __init__(self, name: str, value: float) -> None:
        """
        :param name: Metric name.
        :type name: str
        :param value: Metric value.
        :type value: float
        """
        super().__init__()
        self.name = name
        self.value = value

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['Metric', dict]]:
        if init is not None:
            try:
                ourselves = Metric(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['Metric', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Metric.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "Metric": Metric,
}
