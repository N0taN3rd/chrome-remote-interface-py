from typing import Any, List, Optional, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.runtime import types as Runtime


class ObjectStoreIndex(ProtocolType):
    """
    Object store index.
    """

    def __init__(self, name: str, keyPath: Union['KeyPath', dict], unique: bool, multiEntry: bool) -> None:
        """
        :param name: Index name.
        :type name: str
        :param keyPath: Index key path.
        :type keyPath: dict
        :param unique: If true, index is unique.
        :type unique: bool
        :param multiEntry: If true, index allows multiple entries for a key.
        :type multiEntry: bool
        """
        super().__init__()
        self.name = name
        self.keyPath = KeyPath.safe_create(keyPath)
        self.unique = unique
        self.multiEntry = multiEntry

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ObjectStoreIndex', dict]]:
        if init is not None:
             try:
                ourselves = ObjectStoreIndex(**init)
                return ourselves
             except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ObjectStoreIndex', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ObjectStoreIndex.safe_create(it))
            return list_of_self
        else:
            return init


class ObjectStore(ProtocolType):
    """
    Object store.
    """

    def __init__(self, name: str, keyPath: Union['KeyPath', dict], autoIncrement: bool, indexes: List[Union['ObjectStoreIndex', dict]]) -> None:
        """
        :param name: Object store name.
        :type name: str
        :param keyPath: Object store key path.
        :type keyPath: dict
        :param autoIncrement: If true, object store has auto increment flag set.
        :type autoIncrement: bool
        :param indexes: Indexes in this object store.
        :type indexes: List[dict]
        """
        super().__init__()
        self.name = name
        self.keyPath = KeyPath.safe_create(keyPath)
        self.autoIncrement = autoIncrement
        self.indexes = ObjectStoreIndex.safe_create_from_list(indexes)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['ObjectStore', dict]]:
        if init is not None:
             try:
                ourselves = ObjectStore(**init)
                return ourselves
             except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['ObjectStore', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ObjectStore.safe_create(it))
            return list_of_self
        else:
            return init


class KeyRange(ProtocolType):
    """
    Key range.
    """

    def __init__(self, lowerOpen: bool, upperOpen: bool, lower: Optional[Union['Key', dict]] = None, upper: Optional[Union['Key', dict]] = None) -> None:
        """
        :param lower: Lower bound.
        :type lower: Optional[dict]
        :param upper: Upper bound.
        :type upper: Optional[dict]
        :param lowerOpen: If true lower bound is open.
        :type lowerOpen: bool
        :param upperOpen: If true upper bound is open.
        :type upperOpen: bool
        """
        super().__init__()
        self.lower = Key.safe_create(lower)
        self.upper = Key.safe_create(upper)
        self.lowerOpen = lowerOpen
        self.upperOpen = upperOpen

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['KeyRange', dict]]:
        if init is not None:
             try:
                ourselves = KeyRange(**init)
                return ourselves
             except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['KeyRange', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(KeyRange.safe_create(it))
            return list_of_self
        else:
            return init


class KeyPath(ProtocolType):
    """
    Key path.
    """

    def __init__(self, type: str, string: Optional[str] = None, array: Optional[List[str]] = None) -> None:
        """
        :param type: Key path type.
        :type type: str
        :param string: String value.
        :type string: Optional[str]
        :param array: Array value.
        :type array: Optional[List[str]]
        """
        super().__init__()
        self.type = type
        self.string = string
        self.array = array

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['KeyPath', dict]]:
        if init is not None:
             try:
                ourselves = KeyPath(**init)
                return ourselves
             except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['KeyPath', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(KeyPath.safe_create(it))
            return list_of_self
        else:
            return init


class Key(ProtocolType):
    """
    Key.
    """

    def __init__(self, type: str, number: Optional[float] = None, string: Optional[str] = None, date: Optional[float] = None, array: Optional[List[Union['Key', dict]]] = None) -> None:
        """
        :param type: Key type.
        :type type: str
        :param number: Number value.
        :type number: Optional[float]
        :param string: String value.
        :type string: Optional[str]
        :param date: Date value.
        :type date: Optional[float]
        :param array: Array value.
        :type array: Optional[List[dict]]
        """
        super().__init__()
        self.type = type
        self.number = number
        self.string = string
        self.date = date
        self.array = Key.safe_create_from_list(array)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['Key', dict]]:
        if init is not None:
             try:
                ourselves = Key(**init)
                return ourselves
             except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['Key', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Key.safe_create(it))
            return list_of_self
        else:
            return init


class DatabaseWithObjectStores(ProtocolType):
    """
    Database with an array of object stores.
    """

    def __init__(self, name: str, version: int, objectStores: List[Union['ObjectStore', dict]]) -> None:
        """
        :param name: Database name.
        :type name: str
        :param version: Database version.
        :type version: int
        :param objectStores: Object stores in this database.
        :type objectStores: List[dict]
        """
        super().__init__()
        self.name = name
        self.version = version
        self.objectStores = ObjectStore.safe_create_from_list(objectStores)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['DatabaseWithObjectStores', dict]]:
        if init is not None:
             try:
                ourselves = DatabaseWithObjectStores(**init)
                return ourselves
             except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['DatabaseWithObjectStores', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DatabaseWithObjectStores.safe_create(it))
            return list_of_self
        else:
            return init


class DataEntry(ProtocolType):
    """
    Data entry.
    """

    def __init__(self, key: Union['Runtime.RemoteObject', dict], primaryKey: Union['Runtime.RemoteObject', dict], value: Union['Runtime.RemoteObject', dict]) -> None:
        """
        :param key: Key object.
        :type key: dict
        :param primaryKey: Primary key object.
        :type primaryKey: dict
        :param value: Value object.
        :type value: dict
        """
        super().__init__()
        self.key = Runtime.RemoteObject.safe_create(key)
        self.primaryKey = Runtime.RemoteObject.safe_create(primaryKey)
        self.value = Runtime.RemoteObject.safe_create(value)

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['DataEntry', dict]]:
        if init is not None:
             try:
                ourselves = DataEntry(**init)
                return ourselves
             except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['DataEntry', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DataEntry.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "ObjectStoreIndex": ObjectStoreIndex,
    "ObjectStore": ObjectStore,
    "KeyRange": KeyRange,
    "KeyPath": KeyPath,
    "Key": Key,
    "DatabaseWithObjectStores": DatabaseWithObjectStores,
    "DataEntry": DataEntry,
}
