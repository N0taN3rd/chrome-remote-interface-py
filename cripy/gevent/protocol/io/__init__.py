from cripy.gevent.protocol.runtime import types as Runtime
from cripy.gevent.protocol.io import types as Types

__all__ = ["IO"] + Types.__all__


class IO(object):
    """
    Input/Output operations for streams produced by DevTools.
    """

    def __init__(self, chrome):
        self.chrome = chrome

    def close(self, handle):
        """
        :param handle: Handle of the stream to close.
        :type handle: str
        """
        msg_dict = dict()
        if handle is not None:
            msg_dict["handle"] = handle
        wres = self.chrome.send("IO.close", msg_dict)
        return wres.get()

    def read(self, handle, offset=None, size=None):
        """
        :param handle: Handle of the stream to read.
        :type handle: str
        :param offset: Seek to the specified offset before reading (if not specificed, proceed with offset following the last read). Some types of streams may only support sequential reads.
        :type offset: Optional[int]
        :param size: Maximum number of bytes to read (left upon the agent discretion if not specified).
        :type size: Optional[int]
        """
        msg_dict = dict()
        if handle is not None:
            msg_dict["handle"] = handle
        if offset is not None:
            msg_dict["offset"] = offset
        if size is not None:
            msg_dict["size"] = size
        wres = self.chrome.send("IO.read", msg_dict)
        res = wres.get()
        return res

    def resolveBlob(self, objectId):
        """
        :param objectId: Object id of a Blob object wrapper.
        :type objectId: str
        """
        msg_dict = dict()
        if objectId is not None:
            msg_dict["objectId"] = objectId
        wres = self.chrome.send("IO.resolveBlob", msg_dict)
        res = wres.get()
        return res

    @staticmethod
    def get_event_classes():
        return None
