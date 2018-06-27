from typing import Any, List, Optional, Union
from cripy.asyncio.protocol.log import events as Events
from cripy.asyncio.protocol.log import types as Types

__all__ = ["Log"]


class Log(object):
    """
    Provides access to log entries.
    """

    dependencies = ['Runtime', 'Network']

    events = Events.LOG_EVENTS_NS

    def __init__(self, chrome):
        """
        Construct a new Log object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def clear(self) -> Optional[dict]:
        """
        Clears the log.
        """
        res = await self.chrome.send('Log.clear')
        return res

    async def disable(self) -> Optional[dict]:
        """
        Disables log domain, prevents further log entries from being reported to the client.
        """
        res = await self.chrome.send('Log.disable')
        return res

    async def enable(self) -> Optional[dict]:
        """
        Enables log domain, sends the entries collected so far to the client by means of the
`entryAdded` notification.
        """
        res = await self.chrome.send('Log.enable')
        return res

    async def startViolationsReport(self, config: List[dict]) -> Optional[dict]:
        """
        start violation reporting.

        :param config: Configuration for violations.
        :type config: List[dict]
        """
        msg_dict = dict()
        if config is not None:
            msg_dict['config'] = config
        res = await self.chrome.send('Log.startViolationsReport', msg_dict)
        return res

    async def stopViolationsReport(self) -> Optional[dict]:
        """
        Stop violation reporting.
        """
        res = await self.chrome.send('Log.stopViolationsReport')
        return res

    def entryAdded(self, fn, once=False):
        if once:
            self.chrome.once("Log.entryAdded", fn)
        else:
            self.chrome.on("Log.entryAdded", fn)

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return Events.LOG_EVENTS_TO_CLASS

