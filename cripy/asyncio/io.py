from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from .client import Client

__all__ = ["IO"]


@attr.dataclass(slots=True)
class IO(object):
    """
    Input/Output operations for streams produced by DevTools.
    """

    client: "Client" = attr.ib(repr=False)

    async def close(self, handle: str) -> Optional[dict]:
        """
        Close the stream, discard any temporary backing storage.

        :param handle: Handle of the stream to close.
        :type handle: str
        """
        msg_dict = dict()
        if handle is not None:
            msg_dict["handle"] = handle
        res = await self.client.send("IO.close", msg_dict)
        return res

    async def read(
        self, handle: str, offset: Optional[int] = None, size: Optional[int] = None
    ) -> Optional[dict]:
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
            msg_dict["handle"] = handle
        if offset is not None:
            msg_dict["offset"] = offset
        if size is not None:
            msg_dict["size"] = size
        res = await self.client.send("IO.read", msg_dict)
        return res

    async def resolveBlob(self, objectId: str) -> Optional[dict]:
        """
        Return UUID of Blob object specified by a remote object id.

        :param objectId: Object id of a Blob object wrapper.
        :type objectId: str
        """
        msg_dict = dict()
        if objectId is not None:
            msg_dict["objectId"] = objectId
        res = await self.client.send("IO.resolveBlob", msg_dict)
        return res
