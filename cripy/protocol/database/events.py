from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class AddDatabaseEvent(BaseEvent):

    event: str = "Database.addDatabase"

    def __init__(self) -> None:
        """
        :param database: The database
        :type Database:
        """
        super().__init__()


EVENT_TO_CLASS = {
   "Database.addDatabase": AddDatabaseEvent,
}

