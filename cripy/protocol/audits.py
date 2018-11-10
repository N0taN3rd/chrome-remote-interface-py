# -*- coding: utf-8 -*-
"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Audits"]


@attr.dataclass(slots=True, cmp=False)
class Audits(object):
    """
    Audits domain allows investigation of page violations and possible improvements.
    """

    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def getEncodedResponse(
        self,
        requestId: str,
        encoding: str,
        quality: Optional[float] = None,
        sizeOnly: Optional[bool] = None,
    ) -> Awaitable[Optional[dict]]:
        """
        Returns the response body and size if it were re-encoded with the specified settings. Only
applies to images.

        :param requestId: Identifier of the network request to get content for.
        :type requestId: str
        :param encoding: The encoding to use.
        :type encoding: str
        :param quality: The quality of the encoding (0-1). (defaults to 1)
        :type quality: Optional[float]
        :param sizeOnly: Whether to only return the size information (defaults to false).
        :type sizeOnly: Optional[bool]
        """
        msg_dict = dict()
        if requestId is not None:
            msg_dict["requestId"] = requestId
        if encoding is not None:
            msg_dict["encoding"] = encoding
        if quality is not None:
            msg_dict["quality"] = quality
        if sizeOnly is not None:
            msg_dict["sizeOnly"] = sizeOnly
        return self.client.send("Audits.getEncodedResponse", msg_dict)
