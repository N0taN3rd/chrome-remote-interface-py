from cripy.sync.protocol.runtime import types as Runtime
from cripy.sync.protocol.io import types as Types

__all__ = ["IO"]+ Types.__all__ 


class IO(object):
    """
    Input/Output operations for streams produced by DevTools.
    """


    def __init__(self, chrome):
        self.chrome = chrome

    def close(self, handle, cb=None):
        """
        :param handle: Handle of the stream to close.
        :type handle: str
        """
        msg_dict = dict()
        if handle is not None:
            msg_dict['handle'] = handle
        self.chrome.send('IO.close', params=msg_dict)


    def read(self, handle, offset, size, cb=None):
        """
        :param handle: Handle of the stream to read.
        :type handle: str
        :param offset: Seek to the specified offset before reading (if not specificed, proceed with offset following the last read). Some types of streams may only support sequential reads.
        :type offset: Optional[int]
        :param size: Maximum number of bytes to read (left upon the agent discretion if not specified).
        :type size: Optional[int]
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if handle is not None:
            msg_dict['handle'] = handle
        if offset is not None:
            msg_dict['offset'] = offset
        if size is not None:
            msg_dict['size'] = size
        self.chrome.send('IO.read', params=msg_dict, cb=cb_wrapper)


    def resolveBlob(self, objectId, cb=None):
        """
        :param objectId: Object id of a Blob object wrapper.
        :type objectId: str
        """
        def cb_wrapper(res):
            cb(res)
        msg_dict = dict()
        if objectId is not None:
            msg_dict['objectId'] = objectId
        self.chrome.send('IO.resolveBlob', params=msg_dict, cb=cb_wrapper)


    @staticmethod
    def get_event_classes():
        return None

