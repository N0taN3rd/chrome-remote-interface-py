from cripy.sync.protocol.indexeddb import types as Types

__all__ = ["IndexedDB"]+ Types.__all__ 


class IndexedDB(object):
    dependencies = ['Runtime']

    def __init__(self, chrome):
        self.chrome = chrome

    def clearObjectStore(self, securityOrigin, databaseName, objectStoreName):
        """
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
        self.chrome.send('IndexedDB.clearObjectStore', params=msg_dict)


    def deleteDatabase(self, securityOrigin, databaseName):
        """
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
        self.chrome.send('IndexedDB.deleteDatabase', params=msg_dict)


    def deleteObjectStoreEntries(self, securityOrigin, databaseName, objectStoreName, keyRange):
        """
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
        self.chrome.send('IndexedDB.deleteObjectStoreEntries', params=msg_dict)


    def disable(self):
        self.chrome.send('IndexedDB.disable')


    def enable(self):
        self.chrome.send('IndexedDB.enable')


    def requestData(self, securityOrigin, databaseName, objectStoreName, indexName, skipCount, pageSize, keyRange):
        """
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
        def cb(res):
            res['objectStoreDataEntries'] = Types.DataEntry.safe_create_from_list(res['objectStoreDataEntries'])
            self.chrome.emit('IndexedDB.requestData', res)
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
        self.chrome.send('IndexedDB.requestData', params=msg_dict, cb=cb)


    def requestDatabase(self, securityOrigin, databaseName):
        """
        :param securityOrigin: Security origin.
        :type securityOrigin: str
        :param databaseName: Database name.
        :type databaseName: str
        """
        def cb(res):
            res['databaseWithObjectStores'] = Types.DatabaseWithObjectStores.safe_create(res['databaseWithObjectStores'])
            self.chrome.emit('IndexedDB.requestDatabase', res)
        msg_dict = dict()
        if securityOrigin is not None:
            msg_dict['securityOrigin'] = securityOrigin
        if databaseName is not None:
            msg_dict['databaseName'] = databaseName
        self.chrome.send('IndexedDB.requestDatabase', params=msg_dict, cb=cb)


    def requestDatabaseNames(self, securityOrigin):
        """
        :param securityOrigin: Security origin.
        :type securityOrigin: str
        """
        def cb(res):
            self.chrome.emit('IndexedDB.requestDatabaseNames', res)
        msg_dict = dict()
        if securityOrigin is not None:
            msg_dict['securityOrigin'] = securityOrigin
        self.chrome.send('IndexedDB.requestDatabaseNames', params=msg_dict, cb=cb)


    @staticmethod
    def get_event_classes():
        return None

