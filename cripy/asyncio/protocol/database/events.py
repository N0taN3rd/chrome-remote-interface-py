from typing import Any, List, Optional, Union
from collections import namedtuple
from cripy.asyncio.protocol.database.types import *

__all__ = [
    "AddDatabaseEvent",
    "DATABASE_EVENTS_TO_CLASS",
    "DATABASE_EVENTS_NS"
]

class AddDatabaseEvent(object):

    event = "Database.addDatabase"

    __slots__ = ["database"]

    def __init__(self, database: Union[DatabaseT, dict]) -> None:
        """
        Create a new instance of AddDatabaseEvent

        :param database: The database
        :type database: dict
        """
        super().__init__()
        self.database = Database.safe_create(database)

    def __repr__(self) -> str:
        repr_args = []
        if self.database is not None:
            repr_args.append("database={!r}".format(self.database))
        return "AddDatabaseEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['AddDatabaseEvent', dict]]:
        """
        Safely create AddDatabaseEvent from the supplied init dictionary.

        This method will not throw an Exception and will return a new instance of AddDatabaseEvent
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new instance of AddDatabaseEvent if creation did not fail
        :rtype: Optional[Union[dict, AddDatabaseEvent]]
        """
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
        """
        Safely create a new list AddDatabaseEvents from the supplied list of dictionaries.

        This method will not throw an Exception and will return a new list AddDatabaseEvent instances
        if init is not None otherwise returns init or None if init was None.

        :param init: The init dictionary
        :type init: dict
        :return: A new list of AddDatabaseEvent instances if creation did not fail
        :rtype: Optional[List[Union[dict, AddDatabaseEvent]]]
        """
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AddDatabaseEvent.safe_create(it))
            return list_of_self
        else:
            return init


DATABASE_EVENTS_TO_CLASS = {
   "Database.addDatabase": AddDatabaseEvent,
}

DatabaseNS = namedtuple("DatabaseNS", ["AddDatabase"])

DATABASE_EVENTS_NS = DatabaseNS(
  AddDatabase="Database.addDatabase",
)
