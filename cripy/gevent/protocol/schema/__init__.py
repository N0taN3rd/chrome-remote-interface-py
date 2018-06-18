from cripy.gevent.protocol.schema import types as Types

__all__ = ["Schema"] + Types.__all__


class Schema(object):
    """
    This domain is deprecated.
    """

    def __init__(self, chrome):
        self.chrome = chrome

    def getDomains(self):
        wres = self.chrome.send("Schema.getDomains")
        res = wres.get()
        res["domains"] = Types.Domain.safe_create_from_list(res["domains"])
        return res

    @staticmethod
    def get_event_classes():
        return None
