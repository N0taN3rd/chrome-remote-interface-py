from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.runtime import types as Runtime


class DatabaseWithObjectStores(ChromeTypeBase):

    def __init__(
        self, name: str, version: int, objectStores: List["ObjectStore"]
    ) -> None:
        super().__init__()
        self.name: str = name
        self.version: int = version
        self.objectStores: List[ObjectStore] = objectStores


class ObjectStore(ChromeTypeBase):

    def __init__(
        self,
        name: str,
        keyPath: "KeyPath",
        autoIncrement: bool,
        indexes: List["ObjectStoreIndex"],
    ) -> None:
        super().__init__()
        self.name: str = name
        self.keyPath: KeyPath = keyPath
        self.autoIncrement: bool = autoIncrement
        self.indexes: List[ObjectStoreIndex] = indexes


class ObjectStoreIndex(ChromeTypeBase):

    def __init__(
        self, name: str, keyPath: "KeyPath", unique: bool, multiEntry: bool
    ) -> None:
        super().__init__()
        self.name: str = name
        self.keyPath: KeyPath = keyPath
        self.unique: bool = unique
        self.multiEntry: bool = multiEntry


class Key(ChromeTypeBase):

    def __init__(
        self,
        type: str,
        number: Optional[float] = None,
        string: Optional[str] = None,
        date: Optional[float] = None,
        array: Optional[List["Key"]] = None,
    ) -> None:
        super().__init__()
        self.type: str = type
        self.number: Optional[float] = number
        self.string: Optional[str] = string
        self.date: Optional[float] = date
        self.array: Optional[List[Key]] = array


class KeyRange(ChromeTypeBase):

    def __init__(
        self,
        lowerOpen: bool,
        upperOpen: bool,
        lower: Optional["Key"] = None,
        upper: Optional["Key"] = None,
    ) -> None:
        super().__init__()
        self.lower: Optional[Key] = lower
        self.upper: Optional[Key] = upper
        self.lowerOpen: bool = lowerOpen
        self.upperOpen: bool = upperOpen


class DataEntry(ChromeTypeBase):

    def __init__(
        self,
        key: "Runtime.RemoteObject",
        primaryKey: "Runtime.RemoteObject",
        value: "Runtime.RemoteObject",
    ) -> None:
        super().__init__()
        self.key: Runtime.RemoteObject = key
        self.primaryKey: Runtime.RemoteObject = primaryKey
        self.value: Runtime.RemoteObject = value


class KeyPath(ChromeTypeBase):

    def __init__(
        self,
        type: str,
        string: Optional[str] = None,
        array: Optional[List["str"]] = None,
    ) -> None:
        super().__init__()
        self.type: str = type
        self.string: Optional[str] = string
        self.array: Optional[List[str]] = array
