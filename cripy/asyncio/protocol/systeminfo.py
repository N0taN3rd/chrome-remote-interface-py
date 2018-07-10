from typing import Any, List, Optional, Union


__all__ = ["SystemInfo"]


class SystemInfo(object):
    """
    The SystemInfo domain defines methods and events for querying low-level system information.
    """


    def __init__(self, chrome):
        """
        Construct a new SystemInfo object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def getInfo(self) -> Optional[dict]:
        """
        Returns information about the system.
        """
        res = await self.chrome.send('SystemInfo.getInfo')
        return res



