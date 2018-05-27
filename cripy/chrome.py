import asyncio
import base64
import json
import logging
from typing import Optional, List

import aiohttp
import websockets
import websockets.protocol

from .protocol import ProtocolMixin


class Chrome(ProtocolMixin):

    def __init__(
        self, host: Optional[str] = "localhost", port: Optional[int] = 9222
    ) -> None:
        super().__init__()
        self._host: str = host
        self._port: int = port
        self._url: str = "http://%s:%d" % (self.host, self.port)
        self._tabs: List = []
        self.is_connected: bool = False

    async def connect(self):
        """ Get all open browser tabs that are pages tabs
        """
        if not self.is_connected:
            try:
                await asyncio.wait_for(self.attempt_tab_fetch(), timeout=5)
            except TimeoutError:
                self._log.error("Unable to fetch tabs! Timeout")

    async def attempt_tab_fetch(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self._url + "/json") as resp:
                tabs = []
                data = await resp.json()
                if not len(data):
                    self._log.warning(
                        "Empty data, will attempt to reconnect until able to get pages."
                    )
                for tab in filter(lambda x: x["type"] == "page", data):
                    t = await ChromeTab.create_from_json(tab, self._host, self._port)
                    tabs.append(t)
                self._tabs = tabs
                self._log.debug(
                    "Connected to Chrome! Found {} tabs".format(len(self._tabs))
                )
        self.is_connected = True
