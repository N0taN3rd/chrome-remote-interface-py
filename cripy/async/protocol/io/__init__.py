from typing import Any, List, Optional, Union
from cripy.async.protocol.runtime import types as Runtime
from cripy.async.protocol.io import types as Types


class IO(object):
    """
    Input/Output operations for streams produced by DevTools.
    """

    def __init__(self, chrome):
        self.chrome = chrome

    async def close(self, handle: str) -> Optional[dict]:
        """
        :param handle: Handle of the stream to close.
        :type handle: str
        """
        msg_dict = dict()
        if handle is not None:
            msg_dict["handle"] = handle
        mayberes = await self.chrome.send("IO.close", msg_dict)
        return mayberes

    async def read(
        self, handle: str, offset: Optional[int] = None, size: Optional[int] = None
    ) -> Optional[dict]:
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
        mayberes = await self.chrome.send("IO.read", msg_dict)
        res = await mayberes
        return res

    async def resolveBlob(self, objectId: str) -> Optional[dict]:
        """
        :param objectId: Object id of a Blob object wrapper.
        :type objectId: str
        """
        msg_dict = dict()
        if objectId is not None:
            msg_dict["objectId"] = objectId
        mayberes = await self.chrome.send("IO.resolveBlob", msg_dict)
        res = await mayberes
        return res

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return None
