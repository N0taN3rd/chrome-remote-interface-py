from typing import Any, List, Optional, Union


__all__ = ["Schema"]


class Schema(object):
    """
    This domain is deprecated.
    """


    def __init__(self, chrome):
        """
        Construct a new Schema object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def getDomains(self) -> Optional[dict]:
        """
        Returns supported domains.
        """
        res = await self.chrome.send('Schema.getDomains')
        return res



