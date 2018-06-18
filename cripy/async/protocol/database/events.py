from typing import Any, List, Optional, Union
from types import SimpleNamespace

try:
    from cripy.async.protocol.database.types import *
except ImportError:
    pass


class AddDatabaseEvent(object):

    event = "Database.addDatabase"

    def __init__(self, database: Union[Database, dict]) -> None:
        """
        :param database: The database
        :type database: dict
        """
        super().__init__()
        self.database = Database.safe_create(database)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.database is not None:
            repr_args.append("database={!r}".format(self.database))
        return "AddDatabaseEvent(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["AddDatabaseEvent", dict]]:
        if init is not None:
            try:
                ourselves = AddDatabaseEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["AddDatabaseEvent", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(AddDatabaseEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {"Database.addDatabase": AddDatabaseEvent}

EVENT_NS = SimpleNamespace(AddDatabase="Database.addDatabase")
