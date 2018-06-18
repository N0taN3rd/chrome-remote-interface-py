from cripy.gevent.protocol.database import events as Events
from cripy.gevent.protocol.database import types as Types

__all__ = ["Database"] + Events.__all__ + Types.__all__


class Database(object):

    def __init__(self, chrome):
        self.chrome = chrome

    def disable(self):
        wres = self.chrome.send("Database.disable")
        return wres.get()

    def enable(self):
        wres = self.chrome.send("Database.enable")
        return wres.get()

    def executeSQL(self, databaseId, query):
        """
        :param databaseId: The databaseId
        :type databaseId: str
        :param query: The query
        :type query: str
        """
        msg_dict = dict()
        if databaseId is not None:
            msg_dict["databaseId"] = databaseId
        if query is not None:
            msg_dict["query"] = query
        wres = self.chrome.send("Database.executeSQL", msg_dict)
        res = wres.get()
        res["sqlError"] = Types.Error.safe_create(res["sqlError"])
        return res

    def getDatabaseTableNames(self, databaseId):
        """
        :param databaseId: The databaseId
        :type databaseId: str
        """
        msg_dict = dict()
        if databaseId is not None:
            msg_dict["databaseId"] = databaseId
        wres = self.chrome.send("Database.getDatabaseTableNames", msg_dict)
        res = wres.get()
        return res

    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS
