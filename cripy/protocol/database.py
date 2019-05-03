"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Database"]


class Database:
    """
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/Database`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of Database

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def disable(self) -> Awaitable[Dict]:
        """
        Disables database tracking, prevents database events from being sent to the client.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Database#method-disable`

        :return: The results of the command
        """
        return self.client.send("Database.disable", {})

    def enable(self) -> Awaitable[Dict]:
        """
        Enables database tracking, database events will now be delivered to the client.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Database#method-enable`

        :return: The results of the command
        """
        return self.client.send("Database.enable", {})

    def executeSQL(self, databaseId: str, query: str) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/Database#method-executeSQL`

        :param databaseId: The databaseId
        :param query: The query
        :return: The results of the command
        """
        return self.client.send(
            "Database.executeSQL", {"databaseId": databaseId, "query": query}
        )

    def getDatabaseTableNames(self, databaseId: str) -> Awaitable[Dict]:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/Database#method-getDatabaseTableNames`

        :param databaseId: The databaseId
        :return: The results of the command
        """
        return self.client.send(
            "Database.getDatabaseTableNames", {"databaseId": databaseId}
        )

    def addDatabase(
        self, listener: Optional[Callable[[Dict[str, Any]], Any]] = None
    ) -> Any:
        """
        See `https://chromedevtools.github.io/devtools-protocol/tot/Database#event-addDatabase`

        :param listener: Optional listener function
        :return: If a listener was supplied the return value is a callable that
        will remove the supplied listener otherwise a future that resolves
        with the value of the event
        """
        event_name = "Database.addDatabase"
        if listener is None:
            future = self.client.loop.create_future()

            def _listener(event: Optional[Dict] = None) -> None:
                future.set_result(event)

            self.client.once(event_name, _listener)

            return future

        self.client.on(event_name, listener)
        return lambda: self.client.remove_listener(event_name, listener)
