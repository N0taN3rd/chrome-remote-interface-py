from cripy.sync.protocol.database import events as Events
from cripy.sync.protocol.database import types as Types

__all__ = ["Database"] + Events.__all__ + Types.__all__ 


class Database(object):

    def __init__(self, chrome):
        self.chrome = chrome

    def disable(self):
        self.chrome.send('Database.disable')


    def enable(self):
        self.chrome.send('Database.enable')


    def executeSQL(self, databaseId, query):
        """
        :param databaseId: The databaseId
        :type databaseId: str
        :param query: The query
        :type query: str
        """
        def cb(res):
            res['sqlError'] = Types.Error.safe_create(res['sqlError'])
            self.chrome.emit('Database.executeSQL', res)
        msg_dict = dict()
        if databaseId is not None:
            msg_dict['databaseId'] = databaseId
        if query is not None:
            msg_dict['query'] = query
        self.chrome.send('Database.executeSQL', params=msg_dict, cb=cb)


    def getDatabaseTableNames(self, databaseId):
        """
        :param databaseId: The databaseId
        :type databaseId: str
        """
        def cb(res):
            self.chrome.emit('Database.getDatabaseTableNames', res)
        msg_dict = dict()
        if databaseId is not None:
            msg_dict['databaseId'] = databaseId
        self.chrome.send('Database.getDatabaseTableNames', params=msg_dict, cb=cb)


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

