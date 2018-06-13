from cripy.sync.protocol.database import events as Events
from cripy.sync.protocol.database import types as Types

__all__ = ["Database"] + Events.__all__ + Types.__all__ 


class Database(object):

    def __init__(self, chrome):
        self.chrome = chrome

    def disable(self, cb=None):
        self.chrome.send('Database.disable')


    def enable(self, cb=None):
        self.chrome.send('Database.enable')


    def executeSQL(self, databaseId, query, cb=None):
        """
        :param databaseId: The databaseId
        :type databaseId: str
        :param query: The query
        :type query: str
        """
        def cb_wrapper(res):
            res['sqlError'] = Types.Error.safe_create(res['sqlError'])
            cb(res)
        msg_dict = dict()
        if databaseId is not None:
            msg_dict['databaseId'] = databaseId
        if query is not None:
            msg_dict['query'] = query
        self.chrome.send('Database.executeSQL', params=msg_dict, cb=cb_wrapper)


    def getDatabaseTableNames(self, databaseId, cb=None):
        """
        :param databaseId: The databaseId
        :type databaseId: str
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if databaseId is not None:
            msg_dict['databaseId'] = databaseId
        self.chrome.send('Database.getDatabaseTableNames', params=msg_dict, cb=cb_wrapper)


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS

