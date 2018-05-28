from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.runtime import types as Runtime


class DatabaseWithObjectStores(ChromeTypeBase):
    """Database with an array of object stores."""

    def __init__(self, name: str, version: int, objectStores: List['ObjectStore']) -> None:
        """
        :param name: Database name.
        :type str:
        :param version: Database version.
        :type int:
        :param objectStores: Object stores in this database.
        :type array:
        """
        super().__init__()
        self.name: str = name
        self.version: int = version
        self.objectStores: List[ObjectStore] = objectStores


class ObjectStore(ChromeTypeBase):
    """Object store."""

    def __init__(self, name: str, keyPath: 'KeyPath', autoIncrement: bool, indexes: List['ObjectStoreIndex']) -> None:
        """
        :param name: Object store name.
        :type str:
        :param keyPath: Object store key path.
        :type KeyPath:
        :param autoIncrement: If true, object store has auto increment flag set.
        :type bool:
        :param indexes: Indexes in this object store.
        :type array:
        """
        super().__init__()
        self.name: str = name
        self.keyPath: KeyPath = keyPath
        self.autoIncrement: bool = autoIncrement
        self.indexes: List[ObjectStoreIndex] = indexes


class ObjectStoreIndex(ChromeTypeBase):
    """Object store index."""

    def __init__(self, name: str, keyPath: 'KeyPath', unique: bool, multiEntry: bool) -> None:
        """
        :param name: Index name.
        :type str:
        :param keyPath: Index key path.
        :type KeyPath:
        :param unique: If true, index is unique.
        :type bool:
        :param multiEntry: If true, index allows multiple entries for a key.
        :type bool:
        """
        super().__init__()
        self.name: str = name
        self.keyPath: KeyPath = keyPath
        self.unique: bool = unique
        self.multiEntry: bool = multiEntry


class Key(ChromeTypeBase):
    """Key."""

    def __init__(self, type: str, number: Optional[float] = None, string: Optional[str] = None, date: Optional[float] = None, array: Optional[List['Key']] = None) -> None:
        """
        :param type: Key type.
        :type str:
        :param number: Number value.
        :type float:
        :param string: String value.
        :type str:
        :param date: Date value.
        :type float:
        :param array: Array value.
        :type array:
        """
        super().__init__()
        self.type: str = type
        self.number: Optional[float] = number
        self.string: Optional[str] = string
        self.date: Optional[float] = date
        self.array: Optional[List[Key]] = array


class KeyRange(ChromeTypeBase):
    """Key range."""

    def __init__(self, lowerOpen: bool, upperOpen: bool, lower: Optional['Key'] = None, upper: Optional['Key'] = None) -> None:
        """
        :param lower: Lower bound.
        :type Key:
        :param upper: Upper bound.
        :type Key:
        :param lowerOpen: If true lower bound is open.
        :type bool:
        :param upperOpen: If true upper bound is open.
        :type bool:
        """
        super().__init__()
        self.lower: Optional[Key] = lower
        self.upper: Optional[Key] = upper
        self.lowerOpen: bool = lowerOpen
        self.upperOpen: bool = upperOpen


class DataEntry(ChromeTypeBase):
    """Data entry."""

    def __init__(self, key: 'Runtime.RemoteObject', primaryKey: 'Runtime.RemoteObject', value: 'Runtime.RemoteObject') -> None:
        """
        :param key: Key object.
        :type Runtime.RemoteObject:
        :param primaryKey: Primary key object.
        :type Runtime.RemoteObject:
        :param value: Value object.
        :type Runtime.RemoteObject:
        """
        super().__init__()
        self.key: Runtime.RemoteObject = key
        self.primaryKey: Runtime.RemoteObject = primaryKey
        self.value: Runtime.RemoteObject = value


class KeyPath(ChromeTypeBase):
    """Key path."""

    def __init__(self, type: str, string: Optional[str] = None, array: Optional[List['str']] = None) -> None:
        """
        :param type: Key path type.
        :type str:
        :param string: String value.
        :type str:
        :param array: Array value.
        :type array:
        """
        super().__init__()
        self.type: str = type
        self.string: Optional[str] = string
        self.array: Optional[List[str]] = array


