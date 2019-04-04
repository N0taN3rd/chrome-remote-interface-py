"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["IO"]


class IO:
    """
    Input/Output operations for streams produced by DevTools.
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/IO`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of IO

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def close(self, handle: str) -> Awaitable[Dict]:
        """
        Close the stream, discard any temporary backing storage.

        See `https://chromedevtools.github.io/devtools-protocol/tot/IO#method-close`

        :param handle: Handle of the stream to close.
        :return: The results of the command
        """
        return self.client.send("IO.close", {"handle": handle})

    def read(
        self, handle: str, offset: Optional[int] = None, size: Optional[int] = None
    ) -> Awaitable[Dict]:
        """
        Read a chunk of the stream

        See `https://chromedevtools.github.io/devtools-protocol/tot/IO#method-read`

        :param handle: Handle of the stream to read.
        :param offset: Seek to the specified offset before reading (if not specificed, proceed with offset
         following the last read). Some types of streams may only support sequential reads.
        :param size: Maximum number of bytes to read (left upon the agent discretion if not specified).
        :return: The results of the command
        """
        msg = {"handle": handle}
        if offset is not None:
            msg["offset"] = offset
        if size is not None:
            msg["size"] = size
        return self.client.send("IO.read", msg)

    def resolveBlob(self, objectId: str) -> Awaitable[Dict]:
        """
        Return UUID of Blob object specified by a remote object id.

        See `https://chromedevtools.github.io/devtools-protocol/tot/IO#method-resolveBlob`

        :param objectId: Object id of a Blob object wrapper.
        :return: The results of the command
        """
        return self.client.send("IO.resolveBlob", {"objectId": objectId})
