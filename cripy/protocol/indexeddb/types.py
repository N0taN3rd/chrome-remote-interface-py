from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.runtime import types as Runtime


class DatabaseWithObjectStores(ChromeTypeBase):
    """Database with an array of object stores."""

    def __init__(
        self, name: str, version: int, objectStores: List["ObjectStore"]
    ) -> None:
        """
        :param name: Database name.
        :param version: Database version.
        :param objectStores: Object stores in this database.
        """
        super().__init__()
        self.name: str = name
        self.version: int = version
        self.objectStores: List[ObjectStore] = objectStores


class ObjectStore(ChromeTypeBase):
    """Object store."""

    def __init__(
        self,
        name: str,
        keyPath: "KeyPath",
        autoIncrement: bool,
        indexes: List["ObjectStoreIndex"],
    ) -> None:
        """
        :param name: Object store name.
        :param keyPath: Object store key path.
        :param autoIncrement: If true, object store has auto increment flag set.
        :param indexes: Indexes in this object store.
        """
        super().__init__()
        self.name: str = name
        self.keyPath: KeyPath = keyPath
        self.autoIncrement: bool = autoIncrement
        self.indexes: List[ObjectStoreIndex] = indexes


class ObjectStoreIndex(ChromeTypeBase):
    """Object store index."""

    def __init__(
        self, name: str, keyPath: "KeyPath", unique: bool, multiEntry: bool
    ) -> None:
        """
        :param name: Index name.
        :param keyPath: Index key path.
        :param unique: If true, index is unique.
        :param multiEntry: If true, index allows multiple entries for a key.
        """
        super().__init__()
        self.name: str = name
        self.keyPath: KeyPath = keyPath
        self.unique: bool = unique
        self.multiEntry: bool = multiEntry


class Key(ChromeTypeBase):
    """Key."""

    def __init__(
        self,
        type: str,
        number: Optional[float] = None,
        string: Optional[str] = None,
        date: Optional[float] = None,
        array: Optional[List["Key"]] = None,
    ) -> None:
        """
        :param type: Key type.
        :param number: Number value.
        :param string: String value.
        :param date: Date value.
        :param array: Array value.
        """
        super().__init__()
        self.type: str = type
        self.number: Optional[float] = number
        self.string: Optional[str] = string
        self.date: Optional[float] = date
        self.array: Optional[List[Key]] = array


class KeyRange(ChromeTypeBase):
    """Key range."""

    def __init__(
        self,
        lowerOpen: bool,
        upperOpen: bool,
        lower: Optional["Key"] = None,
        upper: Optional["Key"] = None,
    ) -> None:
        """
        :param lower: Lower bound.
        :param upper: Upper bound.
        :param lowerOpen: If true lower bound is open.
        :param upperOpen: If true upper bound is open.
        """
        super().__init__()
        self.lower: Optional[Key] = lower
        self.upper: Optional[Key] = upper
        self.lowerOpen: bool = lowerOpen
        self.upperOpen: bool = upperOpen


class DataEntry(ChromeTypeBase):
    """Data entry."""

    def __init__(
        self,
        key: "Runtime.RemoteObject",
        primaryKey: "Runtime.RemoteObject",
        value: "Runtime.RemoteObject",
    ) -> None:
        """
        :param key: Key object.
        :param primaryKey: Primary key object.
        :param value: Value object.
        """
        super().__init__()
        self.key: Runtime.RemoteObject = key
        self.primaryKey: Runtime.RemoteObject = primaryKey
        self.value: Runtime.RemoteObject = value


class KeyPath(ChromeTypeBase):
    """Key path."""

    def __init__(
        self,
        type: str,
        string: Optional[str] = None,
        array: Optional[List["str"]] = None,
    ) -> None:
        """
        :param type: Key path type.
        :param string: String value.
        :param array: Array value.
        """
        super().__init__()
        self.type: str = type
        self.string: Optional[str] = string
        self.array: Optional[List[str]] = array
