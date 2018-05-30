import asyncio
import base64
import json
import logging
from urllib.parse import urljoin
from typing import Optional, List, Dict, Union
import ujson
import aiohttp
import websockets
import websockets.protocol

DEFAULT_HOST: str = "localhost"
DEFAULT_PORT: int = 9222
TIMEOUT_S = 25
MAX_PAYLOAD_SIZE_BYTES = 2 ** 30
MAX_PAYLOAD_SIZE_MB = MAX_PAYLOAD_SIZE_BYTES / 1024 ** 2 # ~ 1GB


class Chrome(object):

    def __init__(
        self,
        url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[int] = DEFAULT_PORT,
        secure: Optional[bool] = False,
        wsurl: Optional[str] = None,
    ):
        self._host = host
        self._port = port
        self._url = self._make_url(url, secure)
        self._tabs = []
        self.is_connected = False
        self._ws_url = wsurl
        self._ws: Optional[websockets.WebSocketClientProtocol] = None
        self._recv_task = None
        self._message_id = 1

    async def connect(self):
        if self._ws_url is not None:
            self._ws = await websockets.connect(
                self._ws_url, max_size=None, read_limit=2 ** 32
            )
            self._recv_task = asyncio.ensure_future(self.recv_handler())
        else:
            tabs = await self.List(url=self._url)
            it: Dict[str, str] = list(filter(lambda x: x['type'] == 'page', tabs))[0]
            self._ws_url = it['webSocketDebuggerUrl']
            self._ws = await websockets.connect(
                self._ws_url, max_size=None, read_limit=2 ** 32
            )
            self._recv_task = asyncio.ensure_future(self.recv_handler())


    async def disconnect(self):
        if self._recv_task:
            self._recv_task.cancel()
            await self._recv_task
        await self._ws.close()

    async def recv_handler(self):
        try:
            while True:
                result = await self._ws.recv()
                print(result)
                print(ujson.loads(result))
        except (websockets.ConnectionClosed, ConnectionResetError, asyncio.CancelledError):
            await self.disconnect()


    async def _send(self, domain: str = None, what: dict = None):
        res = await self._ws.send(
            ujson.dumps({"method": "Page.enable", "params": {}, "id": self._message_id})
        )
        self._message_id += 1
        print(res)
        res = await self._ws.send(
            ujson.dumps(
                {
                    "method": "Page.setLifecycleEventsEnabled",
                    "params": {"enabled": True},
                    "id": self._message_id,
                }
            )
        )
        self._message_id += 1
        print(res)
        res = await self._ws.send(
            ujson.dumps({"method": "Network.enable", "params": {}, "id": self._message_id})
        )
        self._message_id += 1
        print(res)

    @classmethod
    async def JSON(
        cls,
        url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[int] = DEFAULT_PORT,
        secure: Optional[bool] = False,
    ):
        async with aiohttp.ClientSession() as session:
            if url is None:
                url = f"{'https:' if secure else 'http:'}//{host}:{port}/json"
            data = await session.get(url)
            json_ = await data.json()
        return json_

    def _make_url(self, url: Optional[str] = None, secure: Optional[bool] = False):
        if url is None:
            return f"{'https:' if secure else 'http:'}//{self._host}:{self._port}"
        return url

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


async def go():
    chrome = Chrome()
    await chrome.connect()
    await chrome._send()


def main():
    loop = asyncio.get_event_loop()  # event loop
    future = asyncio.ensure_future(go())  # tasks to do
    asyncio.async(future)
    loop.run_forever()

if __name__ == "__main__":
    class IT(dict):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    it = IT(dict(a=2))
    print(it)
