"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Audits"]


class Audits:
    """
    Audits domain allows investigation of page violations and possible improvements.
     
    Domain Dependencies: 
      * Network
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/Audits`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of Audits

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def getEncodedResponse(
        self,
        requestId: str,
        encoding: str,
        quality: Optional[Union[int, float]] = None,
        sizeOnly: Optional[bool] = None,
    ) -> Awaitable[Dict]:
        """
        Returns the response body and size if it were re-encoded with the specified settings. Only
        applies to images.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Audits#method-getEncodedResponse`

        :param requestId: Identifier of the network request to get content for.
        :param encoding: The encoding to use.
        :param quality: The quality of the encoding (0-1). (defaults to 1)
        :param sizeOnly: Whether to only return the size information (defaults to false).
        :return: The results of the command
        """
        msg = {"requestId": requestId, "encoding": encoding}
        if quality is not None:
            msg["quality"] = quality
        if sizeOnly is not None:
            msg["sizeOnly"] = sizeOnly
        return self.client.send("Audits.getEncodedResponse", msg)
