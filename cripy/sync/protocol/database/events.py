from types import SimpleNamespace
try:
    from cripy.sync.protocol.database.types import *
except ImportError:
    pass

__all__ = [
    "AddDatabaseEvent",
]


class AddDatabaseEvent(object):

    event = "Database.addDatabase"

    def __init__(self, database):
        """
        :param database: The database
        :type database: dict
        """
        super().__init__()
        self.database = Database.safe_create(database)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.database is not None:
            repr_args.append("database={!r}".format(self.database))
        return "AddDatabaseEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = AddDatabaseEvent(**init)
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
                list_of_self.append(AddDatabaseEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "Database.addDatabase": AddDatabaseEvent,
}

EVENT_NS = SimpleNamespace(
  AddDatabase="Database.addDatabase",
)
