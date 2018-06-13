from cripy.sync.protocol.schema import types as Types

__all__ = ["Schema"]+ Types.__all__ 


class Schema(object):
    """
    This domain is deprecated.
    """


    def __init__(self, chrome):
        self.chrome = chrome

    def getDomains(self, cb=None):
        def cb_wrapper(res):
            res['domains'] = Types.Domain.safe_create_from_list(res['domains'])
            cb(res)
        self.chrome.send('Schema.getDomains', cb=cb_wrapper)


    @staticmethod
    def get_event_classes():
        return None

