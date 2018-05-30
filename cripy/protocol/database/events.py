from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
try:
    from cripy.protocol.database.types import *
except ImportError:
    pass


class AddDatabaseEvent(BaseEvent):

    event = "Database.addDatabase"

    def __init__(self, database: Union[Database, dict]) -> None:
        """
        :param database: The database
        :type database: dict
        """
        super().__init__()
        self.database = Database.safe_create(database)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['AddDatabaseEvent', dict]]:
        if init is not None:
            try:
                ourselves = AddDatabaseEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['AddDatabaseEvent', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AddDatabaseEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "Database.addDatabase": AddDatabaseEvent,
}

