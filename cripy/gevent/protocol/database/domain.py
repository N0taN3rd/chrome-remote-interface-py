from cripy.gevent.protocol.database import events as Events
from cripy.gevent.protocol.database import types as Types

__all__ = ["Database"]


class Database(object):
    events = Events.DATABASE_EVENTS_NS

    def __init__(self, chrome):
        """
        Construct a new Database object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def disable(self):
        """
        Disables database tracking, prevents database events from being sent to the client.
        """
        wres = self.chrome.send('Database.disable')
        return wres.get()

    def enable(self):
        """
        Enables database tracking, database events will now be delivered to the client.
        """
        wres = self.chrome.send('Database.enable')
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
            msg_dict['databaseId'] = databaseId
        if query is not None:
            msg_dict['query'] = query
        wres = self.chrome.send('Database.executeSQL', msg_dict)
        res = wres.get()
        res['sqlError'] = Types.Error.safe_create(res['sqlError'])
        return res

    def getDatabaseTableNames(self, databaseId):
        """
        :param databaseId: The databaseId
        :type databaseId: str
        """
        msg_dict = dict()
        if databaseId is not None:
            msg_dict['databaseId'] = databaseId
        wres = self.chrome.send('Database.getDatabaseTableNames', msg_dict)
        res = wres.get()
        return res

    def addDatabase(self, fn, once=False):
        self.chrome.on("Database.addDatabase", fn, once=once)

    @staticmethod
    def get_event_classes():
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return Events.DATABASE_EVENTS_TO_CLASS

