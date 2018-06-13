from cripy.sync.protocol.runtime import types as Runtime

__all__ = [
    "ObjectStoreIndex",
    "ObjectStore",
    "KeyRange",
    "KeyPath",
    "Key",
    "DatabaseWithObjectStores",
    "DataEntry",
]


class ObjectStoreIndex(object):
    """
    Object store index.
    """

    def __init__(self, name, keyPath, unique, multiEntry):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.keyPath is not None:
            repr_args.append("keyPath={!r}".format(self.keyPath))
        if self.unique is not None:
            repr_args.append("unique={!r}".format(self.unique))
        if self.multiEntry is not None:
            repr_args.append("multiEntry={!r}".format(self.multiEntry))
        return "ObjectStoreIndex(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = ObjectStoreIndex(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ObjectStoreIndex.safe_create(it))
            return list_of_self
        else:
            return init


class ObjectStore(object):
    """
    Object store.
    """

    def __init__(self, name, keyPath, autoIncrement, indexes):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.keyPath is not None:
            repr_args.append("keyPath={!r}".format(self.keyPath))
        if self.autoIncrement is not None:
            repr_args.append("autoIncrement={!r}".format(self.autoIncrement))
        if self.indexes is not None:
            repr_args.append("indexes={!r}".format(self.indexes))
        return "ObjectStore(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = ObjectStore(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(ObjectStore.safe_create(it))
            return list_of_self
        else:
            return init


class KeyRange(object):
    """
    Key range.
    """

    def __init__(self, lowerOpen, upperOpen, lower, upper):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.lower is not None:
            repr_args.append("lower={!r}".format(self.lower))
        if self.upper is not None:
            repr_args.append("upper={!r}".format(self.upper))
        if self.lowerOpen is not None:
            repr_args.append("lowerOpen={!r}".format(self.lowerOpen))
        if self.upperOpen is not None:
            repr_args.append("upperOpen={!r}".format(self.upperOpen))
        return "KeyRange(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = KeyRange(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(KeyRange.safe_create(it))
            return list_of_self
        else:
            return init


class KeyPath(object):
    """
    Key path.
    """

    def __init__(self, type, string, array):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        if self.string is not None:
            repr_args.append("string={!r}".format(self.string))
        if self.array is not None:
            repr_args.append("array={!r}".format(self.array))
        return "KeyPath(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = KeyPath(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(KeyPath.safe_create(it))
            return list_of_self
        else:
            return init


class Key(object):
    """
    Key.
    """

    def __init__(self, type, number, string, date, array):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        if self.number is not None:
            repr_args.append("number={!r}".format(self.number))
        if self.string is not None:
            repr_args.append("string={!r}".format(self.string))
        if self.date is not None:
            repr_args.append("date={!r}".format(self.date))
        if self.array is not None:
            repr_args.append("array={!r}".format(self.array))
        return "Key(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = Key(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Key.safe_create(it))
            return list_of_self
        else:
            return init


class DatabaseWithObjectStores(object):
    """
    Database with an array of object stores.
    """

    def __init__(self, name, version, objectStores):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.version is not None:
            repr_args.append("version={!r}".format(self.version))
        if self.objectStores is not None:
            repr_args.append("objectStores={!r}".format(self.objectStores))
        return "DatabaseWithObjectStores(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = DatabaseWithObjectStores(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DatabaseWithObjectStores.safe_create(it))
            return list_of_self
        else:
            return init


class DataEntry(object):
    """
    Data entry.
    """

    def __init__(self, key, primaryKey, value):
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

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.key is not None:
            repr_args.append("key={!r}".format(self.key))
        if self.primaryKey is not None:
            repr_args.append("primaryKey={!r}".format(self.primaryKey))
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        return "DataEntry(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = DataEntry(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
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
