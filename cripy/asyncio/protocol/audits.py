from typing import Any, List, Optional, Union


__all__ = ["Audits"]


class Audits(object):
    """
    Audits domain allows investigation of page violations and possible improvements.
    """

    dependencies = ['Network']


    def __init__(self, chrome):
        """
        Construct a new Audits object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def getEncodedResponse(self, requestId: str, encoding: str, quality: Optional[float] = None, sizeOnly: Optional[bool] = None) -> Optional[dict]:
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
            msg_dict['requestId'] = requestId
        if encoding is not None:
            msg_dict['encoding'] = encoding
        if quality is not None:
            msg_dict['quality'] = quality
        if sizeOnly is not None:
            msg_dict['sizeOnly'] = sizeOnly
        res = await self.chrome.send('Audits.getEncodedResponse', msg_dict)
        return res



