import asyncio
import base64
import json
import logging
import ujson
from urllib.parse import urljoin
from typing import Optional, List, Dict, Union
from pyee import EventEmitter
import aiohttp
import aiojobs
import websockets
import websockets.protocol

from cripy.async.protocol import ProtocolMixin

DEFAULT_HOST: str = "localhost"
DEFAULT_PORT: int = 9222
TIMEOUT_S = 25
MAX_PAYLOAD_SIZE_BYTES = 2 ** 30
MAX_PAYLOAD_SIZE_MB = MAX_PAYLOAD_SIZE_BYTES / 1024 ** 2  # ~ 1GB


class NetworkError(Exception):  # noqa: D204
    """Network/Protocol related exception."""

    pass


class Client(ProtocolMixin, EventEmitter):

    def __init__(
        self,
        url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[int] = DEFAULT_PORT,
        secure: Optional[bool] = False,
        wsurl: Optional[str] = None,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self._host = host
        self._port = port
        self._url = self._make_url(url, secure)
        self._tabs = []
        self.is_connected = False
        self._ws_url = wsurl
        self._ws: Optional[websockets.WebSocketClientProtocol] = None
        self._recv_task = None
        self._message_id = 1
        self._connected = False
        self._callbacks: Dict[int, asyncio.Future] = dict()

    async def disconnect(self):
        if self._recv_task:
            self._recv_task.cancel()
            await self._recv_task
        try:
            await self._ws.close()
        except Exception as e:
            print(e)
        self._connected = False
        asyncio.get_event_loop().close()

    async def connect(self):
        if self._ws_url is not None:
            self._ws = await websockets.connect(
                self._ws_url, compression=None, max_queue=0, timeout=20
            )
            self._recv_task = asyncio.ensure_future(self._recv_loop())
        else:
            tabs = await self.List(url=self._url)
            it: Dict[str, str] = list(filter(lambda x: x["type"] == "page", tabs))[0]
            self._ws_url = it["webSocketDebuggerUrl"]
            self._ws = await websockets.connect(
                self._ws_url, compression=None, max_queue=0, timeout=20
            )
            self._recv_task = asyncio.ensure_future(self._recv_loop())
        print("connect done")

    async def _recv_loop(self):
        self._connected = True
        while self._connected:
            try:
                resp = await self._ws.recv()
                if resp:
                    self._on_message(resp)
                print(resp)
            except (
                websockets.ConnectionClosed,
                ConnectionResetError,
                asyncio.CancelledError,
            ):
                await self.disconnect()
                break

    def _on_message(self, message: str) -> None:
        msg = ujson.loads(message)
        if msg.get("id") in self._callbacks:
            self._on_response(msg)
        else:
            self._on_query(msg)

    def _on_response(self, msg: dict) -> None:
        callback = self._callbacks.pop(msg.get("id", -1))
        if "error" in msg:
            error = msg["error"]
            callback.set_exception(NetworkError(f"Protocol Error: {error}"))
        else:
            callback.set_result(msg.get("result"))

    def _on_query(self, msg: dict) -> None:
        params = msg.get("params", {})
        method = msg.get("method", "")
        if method in self.protocol_events:
            params = self.protocol_events[method].safe_create(params)
        try:
            self.emit(method, params)
        except Exception as e:
            print("emit execption", e)

    async def _send_async(self, msg: str) -> None:
        while not self._connected:
            print("while not connected")
            await asyncio.sleep(0)
        await self._ws.send(msg)

    def send(self, method: str = None, params: dict = None) -> None:
        if params is None:
            params = dict()
        self._message_id += 1
        _id = self._message_id
        msg = ujson.dumps(dict(method=method, params=params, id=_id))
        asyncio.ensure_future(self._send_async(msg))
        callback = asyncio.get_event_loop().create_future()
        self._callbacks[_id] = callback
        callback.method = method  # type: ignore
        return callback

    async def close(self):
        await self.Browser.close()

    @property
    def connected(self):
        return self._connected

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def url(self):
        return self._url

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
            if not url.endswith("/json"):
                url = urljoin(url, "json")
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
