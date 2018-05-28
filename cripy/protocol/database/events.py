from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent
from cripy.protocol.database.types import (
    Database,
)


class AddDatabaseEvent(BaseEvent):

    event: str = "Database.addDatabase"

    def __init__(self, database: Database) -> None:
        """
        :param database: The database
        :type database: Database
        """
        super().__init__()
        self.database: Database = database


EVENT_TO_CLASS = {
   "Database.addDatabase": AddDatabaseEvent,
}

