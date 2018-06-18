from typing import Any, List, Optional, Union
from cripy.async.protocol.schema import types as Types


class Schema(object):
    """
    This domain is deprecated.
    """

    def __init__(self, chrome):
        self.chrome = chrome

    async def getDomains(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Schema.getDomains")
        res = await mayberes
        res["domains"] = Types.Domain.safe_create_from_list(res["domains"])
        return res

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return None
