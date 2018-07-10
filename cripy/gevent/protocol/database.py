__all__ = ["Database"]


class Database(object):
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
        return wres.get()

    def getDatabaseTableNames(self, databaseId):
        """
        :param databaseId: The databaseId
        :type databaseId: str
        """
        msg_dict = dict()
        if databaseId is not None:
            msg_dict['databaseId'] = databaseId
        wres = self.chrome.send('Database.getDatabaseTableNames', msg_dict)
        return wres.get()

    def addDatabase(self, fn, once=False):
        self.chrome.on("Database.addDatabase", fn, once=once)


