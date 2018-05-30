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
    def safe_create(init: Optional[dict]) -> Optional['ObjectStoreIndex']:
        if init is not None:
            return ObjectStoreIndex(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ObjectStoreIndex']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ObjectStoreIndex(**it))
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
    def safe_create(init: Optional[dict]) -> Optional['ObjectStore']:
        if init is not None:
            return ObjectStore(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['ObjectStore']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ObjectStore(**it))
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
    def safe_create(init: Optional[dict]) -> Optional['KeyRange']:
        if init is not None:
            return KeyRange(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['KeyRange']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(KeyRange(**it))
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
    def safe_create(init: Optional[dict]) -> Optional['KeyPath']:
        if init is not None:
            return KeyPath(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['KeyPath']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(KeyPath(**it))
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
    def safe_create(init: Optional[dict]) -> Optional['Key']:
        if init is not None:
            return Key(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['Key']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Key(**it))
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
    def safe_create(init: Optional[dict]) -> Optional['DatabaseWithObjectStores']:
        if init is not None:
            return DatabaseWithObjectStores(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['DatabaseWithObjectStores']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DatabaseWithObjectStores(**it))
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
    def safe_create(init: Optional[dict]) -> Optional['DataEntry']:
        if init is not None:
            return DataEntry(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['DataEntry']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DataEntry(**it))
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
