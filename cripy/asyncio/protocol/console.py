from typing import Any, List, Optional, Union


__all__ = ["Console"]


class Console(object):
    """
    This domain is deprecated - use Runtime or Log instead.
    """

    dependencies = ['Runtime']


    def __init__(self, chrome):
        """
        Construct a new Console object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def clearMessages(self) -> Optional[dict]:
        """
        Does nothing.
        """
        res = await self.chrome.send('Console.clearMessages')
        return res

    async def disable(self) -> Optional[dict]:
        """
        Disables console domain, prevents further console messages from being reported to the client.
        """
        res = await self.chrome.send('Console.disable')
        return res

    async def enable(self) -> Optional[dict]:
        """
        Enables console domain, sends the messages collected so far to the client by means of the
`messageAdded` notification.
        """
        res = await self.chrome.send('Console.enable')
        return res

    def messageAdded(self, fn, once=False) -> None:
        """
        Issued when new console message is added.
        """
        if once:
            self.chrome.once("Console.messageAdded", fn)
        else:
            self.chrome.on("Console.messageAdded", fn)



