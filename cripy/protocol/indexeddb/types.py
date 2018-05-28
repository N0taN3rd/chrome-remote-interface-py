from typing import Any, List, Optional, Set, Union, TypeVar
from cripy.helpers import ChromeTypeBase
from cripy.protocol.runtime import types as Runtime


class ObjectStoreIndex(ChromeTypeBase):
    """Object store index."""
    def __init__(self, name: str, keyPath: 'KeyPath', unique: bool, multiEntry: bool) -> None:
        """
        :param name: Index name.
        :type name: str
        :param keyPath: Index key path.
        :type keyPath: KeyPath
        :param unique: If true, index is unique.
        :type unique: bool
        :param multiEntry: If true, index allows multiple entries for a key.
        :type multiEntry: bool
        """
        super().__init__()
        self.name: str = name
        self.keyPath: KeyPath = keyPath
        self.unique: bool = unique
        self.multiEntry: bool = multiEntry


class ObjectStore(ChromeTypeBase):
    """Object store."""
    def __init__(self, name: str, keyPath: 'KeyPath', autoIncrement: bool, indexes: List['ObjectStoreIndex']) -> None:
        """
        :param name: Object store name.
        :type name: str
        :param keyPath: Object store key path.
        :type keyPath: KeyPath
        :param autoIncrement: If true, object store has auto increment flag set.
        :type autoIncrement: bool
        :param indexes: Indexes in this object store.
        :type indexes: array
        """
        super().__init__()
        self.name: str = name
        self.keyPath: KeyPath = keyPath
        self.autoIncrement: bool = autoIncrement
        self.indexes: List[ObjectStoreIndex] = indexes


class KeyRange(ChromeTypeBase):
    """Key range."""
    def __init__(self, lowerOpen: bool, upperOpen: bool, lower: Optional['Key'] = None, upper: Optional['Key'] = None) -> None:
        """
        :param lower: Lower bound.
        :type lower: Key
        :param upper: Upper bound.
        :type upper: Key
        :param lowerOpen: If true lower bound is open.
        :type lowerOpen: bool
        :param upperOpen: If true upper bound is open.
        :type upperOpen: bool
        """
        super().__init__()
        self.lower: Optional[Key] = lower
        self.upper: Optional[Key] = upper
        self.lowerOpen: bool = lowerOpen
        self.upperOpen: bool = upperOpen


class KeyPath(ChromeTypeBase):
    """Key path."""
    def __init__(self, type: str, string: Optional[str] = None, array: Optional[List['str']] = None) -> None:
        """
        :param type: Key path type.
        :type type: str
        :param string: String value.
        :type string: str
        :param array: Array value.
        :type array: array
        """
        super().__init__()
        self.type: str = type
        self.string: Optional[str] = string
        self.array: Optional[List[str]] = array


class Key(ChromeTypeBase):
    """Key."""
    def __init__(self, type: str, number: Optional[float] = None, string: Optional[str] = None, date: Optional[float] = None, array: Optional[List['Key']] = None) -> None:
        """
        :param type: Key type.
        :type type: str
        :param number: Number value.
        :type number: float
        :param string: String value.
        :type string: str
        :param date: Date value.
        :type date: float
        :param array: Array value.
        :type array: array
        """
        super().__init__()
        self.type: str = type
        self.number: Optional[float] = number
        self.string: Optional[str] = string
        self.date: Optional[float] = date
        self.array: Optional[List[Key]] = array


class DatabaseWithObjectStores(ChromeTypeBase):
    """Database with an array of object stores."""
    def __init__(self, name: str, version: int, objectStores: List['ObjectStore']) -> None:
        """
        :param name: Database name.
        :type name: str
        :param version: Database version.
        :type version: int
        :param objectStores: Object stores in this database.
        :type objectStores: array
        """
        super().__init__()
        self.name: str = name
        self.version: int = version
        self.objectStores: List[ObjectStore] = objectStores


class DataEntry(ChromeTypeBase):
    """Data entry."""
    def __init__(self, key: 'Runtime.RemoteObject', primaryKey: 'Runtime.RemoteObject', value: 'Runtime.RemoteObject') -> None:
        """
        :param key: Key object.
        :type key: Runtime.RemoteObject
        :param primaryKey: Primary key object.
        :type primaryKey: Runtime.RemoteObject
        :param value: Value object.
        :type value: Runtime.RemoteObject
        """
        super().__init__()
        self.key: Runtime.RemoteObject = key
        self.primaryKey: Runtime.RemoteObject = primaryKey
        self.value: Runtime.RemoteObject = value


