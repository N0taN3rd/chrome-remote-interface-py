from cripy.gevent.protocol.runtime import types as Runtime

__all__ = ["IO"]


class IO(object):
    """
    Input/Output operations for streams produced by DevTools.
    """

    def __init__(self, chrome):
        """
        Construct a new IO object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def close(self, handle):
        """
        Close the stream, discard any temporary backing storage.

        :param handle: Handle of the stream to close.
        :type handle: str
        """
        msg_dict = dict()
        if handle is not None:
            msg_dict['handle'] = handle
        wres = self.chrome.send('IO.close', msg_dict)
        return wres.get()

    def read(self, handle, offset=None, size=None):
        """
        Read a chunk of the stream

        :param handle: Handle of the stream to read.
        :type handle: str
        :param offset: Seek to the specified offset before reading (if not specificed, proceed with offset following the last read). Some types of streams may only support sequential reads.
        :type offset: Optional[int]
        :param size: Maximum number of bytes to read (left upon the agent discretion if not specified).
        :type size: Optional[int]
        """
        msg_dict = dict()
        if handle is not None:
            msg_dict['handle'] = handle
        if offset is not None:
            msg_dict['offset'] = offset
        if size is not None:
            msg_dict['size'] = size
        wres = self.chrome.send('IO.read', msg_dict)
        res = wres.get()
        return res

    def resolveBlob(self, objectId):
        """
        Return UUID of Blob object specified by a remote object id.

        :param objectId: Object id of a Blob object wrapper.
        :type objectId: str
        """
        msg_dict = dict()
        if objectId is not None:
            msg_dict['objectId'] = objectId
        wres = self.chrome.send('IO.resolveBlob', msg_dict)
        res = wres.get()
        return res

    @staticmethod
    def get_event_classes():
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return None

