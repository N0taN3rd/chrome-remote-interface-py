import asyncio
import base64
import json
import logging
from urllib.parse import urljoin
from typing import Optional, List, Dict

import aiohttp
import websockets
import websockets.protocol

DEFAULT_HOST: str = "localhost"
DEFAULT_PORT: str = 9222


class Chrome(object):

    def __init__(
        self, host: Optional[str] = DEFAULT_HOST, port: Optional[int] = DEFAULT_PORT
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
            await asyncio.wait_for(self.attempt_tab_fetch(), timeout=5)

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

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def url(self):
        return self._url

    @property
    def tabs(self):
        if not len(self._tabs):
            raise ValueError("Must call connect_s or connect first!")
        return tuple(self._tabs)

    async def create_tab(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self._url + "/json/new") as resp:
                data = await resp.json()
                t = await ChromeTab.create_from_json(data, self._host, self._port)
                self._tabs.append(t)
        return t

    async def close_tab(self, tab):
        await tab.disconnect()
        async with aiohttp.ClientSession() as session:
            await session.get(self._url + f"/json/close/{tab.id_}")

    @classmethod
    async def Activate(
        cls,
        id: str,
        url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[int] = DEFAULT_PORT,
        secure: Optional[bool] = False,
    ) -> Dict[str, str]:
        async with aiohttp.ClientSession() as session:
            if url is None:
                url = f"{'https:' if secure else 'http:'}//{host}:{port}/json/activate"
            data = await session.get(urljoin(url, id))
            json_ = await data.json()
            return json_

    @classmethod
    async def List(
        cls,
        url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[int] = DEFAULT_PORT,
        secure: Optional[bool] = False,
    ) -> Dict[str, str]:
        async with aiohttp.ClientSession() as session:
            if url is None:
                url = f"{'https:' if secure else 'http:'}//{host}:{port}"
            data = await session.get(urljoin(url, "json/list"))
            json_ = await data.json()
            return json_

    @classmethod
    async def New(
        cls,
        url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[int] = DEFAULT_PORT,
        secure: Optional[bool] = False,
    ) -> Dict[str, str]:
        async with aiohttp.ClientSession() as session:
            if url is None:
                url = f"{'https:' if secure else 'http:'}//{host}:{port}"
            data = await session.get(urljoin(url, "json/new"))
            json_ = await data.json()
            return json_

    @classmethod
    async def Protocol(
        cls,
        url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[int] = DEFAULT_PORT,
        secure: Optional[bool] = False,
    ) -> Dict[str, str]:
        async with aiohttp.ClientSession() as session:
            if url is None:
                url = f"{'https:' if secure else 'http:'}//{host}:{port}"
            data = await session.get(urljoin(url, "json/protocol"))
            json_ = await data.json()
            return json_

    @classmethod
    async def Version(
        cls,
        url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[int] = DEFAULT_PORT,
        secure: Optional[bool] = False,
    ) -> Dict[str, str]:
        async with aiohttp.ClientSession() as session:
            if url is None:
                url = f"{'https:' if secure else 'http:'}//{host}:{port}"
            data = await session.get(urljoin(url, "json/version"))
            json_ = await data.json()
            return json_
