from typing import Any, List, Optional, Union
from cripy.protocol.log import events as Events
from cripy.protocol.log import types as Types


class Log(object):
    """
    Provides access to log entries.
    """

    dependencies = ['Runtime', 'Network']

    def __init__(self, chrome):
        self.chrome = chrome

    async def clear(self) -> Optional[dict]:
        res = await self.chrome.send('Log.clear')
        return res

    async def disable(self) -> Optional[dict]:
        res = await self.chrome.send('Log.disable')
        return res

    async def enable(self) -> Optional[dict]:
        res = await self.chrome.send('Log.enable')
        return res

    async def startViolationsReport(self, config: List[dict]) -> Optional[dict]:
        """
        :param config: Configuration for violations.
        :type config: List[dict]
        """
        msg_dict = dict()
        if config is not None:
            msg_dict['config'] = config
        res = await self.chrome.send('Log.startViolationsReport', msg_dict)
        return res

    async def stopViolationsReport(self) -> Optional[dict]:
        res = await self.chrome.send('Log.stopViolationsReport')
        return res

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return Events.EVENT_TO_CLASS

