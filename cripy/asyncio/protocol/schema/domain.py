from typing import Any, List, Optional, Union
from cripy.asyncio.protocol.schema import types as Types

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
        mayberes = await self.chrome.send('Schema.getDomains')
        res = await mayberes
        res['domains'] = Types.Domain.safe_create_from_list(res['domains'])
        return res

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return None

