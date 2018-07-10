__all__ = ["IndexedDB"]


class IndexedDB(object):
    dependencies = ['Runtime']

    def __init__(self, chrome):
        """
        Construct a new IndexedDB object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def clearObjectStore(self, securityOrigin, databaseName, objectStoreName):
        """
        Clears all entries from an object store.

        :param securityOrigin: Security origin.
        :type securityOrigin: str
        :param databaseName: Database name.
        :type databaseName: str
        :param objectStoreName: Object store name.
        :type objectStoreName: str
        """
        msg_dict = dict()
        if securityOrigin is not None:
            msg_dict['securityOrigin'] = securityOrigin
        if databaseName is not None:
            msg_dict['databaseName'] = databaseName
        if objectStoreName is not None:
            msg_dict['objectStoreName'] = objectStoreName
        wres = self.chrome.send('IndexedDB.clearObjectStore', msg_dict)
        return wres.get()

    def deleteDatabase(self, securityOrigin, databaseName):
        """
        Deletes a database.

        :param securityOrigin: Security origin.
        :type securityOrigin: str
        :param databaseName: Database name.
        :type databaseName: str
        """
        msg_dict = dict()
        if securityOrigin is not None:
            msg_dict['securityOrigin'] = securityOrigin
        if databaseName is not None:
            msg_dict['databaseName'] = databaseName
        wres = self.chrome.send('IndexedDB.deleteDatabase', msg_dict)
        return wres.get()

    def deleteObjectStoreEntries(self, securityOrigin, databaseName, objectStoreName, keyRange):
        """
        Delete a range of entries from an object store

        :param securityOrigin: The securityOrigin
        :type securityOrigin: str
        :param databaseName: The databaseName
        :type databaseName: str
        :param objectStoreName: The objectStoreName
        :type objectStoreName: str
        :param keyRange: Range of entry keys to delete
        :type keyRange: dict
        """
        msg_dict = dict()
        if securityOrigin is not None:
            msg_dict['securityOrigin'] = securityOrigin
        if databaseName is not None:
            msg_dict['databaseName'] = databaseName
        if objectStoreName is not None:
            msg_dict['objectStoreName'] = objectStoreName
        if keyRange is not None:
            msg_dict['keyRange'] = keyRange
        wres = self.chrome.send('IndexedDB.deleteObjectStoreEntries', msg_dict)
        return wres.get()

    def disable(self):
        """
        Disables events from backend.
        """
        wres = self.chrome.send('IndexedDB.disable')
        return wres.get()

    def enable(self):
        """
        Enables events from backend.
        """
        wres = self.chrome.send('IndexedDB.enable')
        return wres.get()

    def requestData(self, securityOrigin, databaseName, objectStoreName, indexName, skipCount, pageSize, keyRange=None):
        """
        Requests data from object store or index.

        :param securityOrigin: Security origin.
        :type securityOrigin: str
        :param databaseName: Database name.
        :type databaseName: str
        :param objectStoreName: Object store name.
        :type objectStoreName: str
        :param indexName: Index name, empty string for object store data requests.
        :type indexName: str
        :param skipCount: Number of records to skip.
        :type skipCount: int
        :param pageSize: Number of records to fetch.
        :type pageSize: int
        :param keyRange: Key range.
        :type keyRange: Optional[dict]
        """
        msg_dict = dict()
        if securityOrigin is not None:
            msg_dict['securityOrigin'] = securityOrigin
        if databaseName is not None:
            msg_dict['databaseName'] = databaseName
        if objectStoreName is not None:
            msg_dict['objectStoreName'] = objectStoreName
        if indexName is not None:
            msg_dict['indexName'] = indexName
        if skipCount is not None:
            msg_dict['skipCount'] = skipCount
        if pageSize is not None:
            msg_dict['pageSize'] = pageSize
        if keyRange is not None:
            msg_dict['keyRange'] = keyRange
        wres = self.chrome.send('IndexedDB.requestData', msg_dict)
        return wres.get()

    def requestDatabase(self, securityOrigin, databaseName):
        """
        Requests database with given name in given frame.

        :param securityOrigin: Security origin.
        :type securityOrigin: str
        :param databaseName: Database name.
        :type databaseName: str
        """
        msg_dict = dict()
        if securityOrigin is not None:
            msg_dict['securityOrigin'] = securityOrigin
        if databaseName is not None:
            msg_dict['databaseName'] = databaseName
        wres = self.chrome.send('IndexedDB.requestDatabase', msg_dict)
        return wres.get()

    def requestDatabaseNames(self, securityOrigin):
        """
        Requests database names for given security origin.

        :param securityOrigin: Security origin.
        :type securityOrigin: str
        """
        msg_dict = dict()
        if securityOrigin is not None:
            msg_dict['securityOrigin'] = securityOrigin
        wres = self.chrome.send('IndexedDB.requestDatabaseNames', msg_dict)
        return wres.get()


