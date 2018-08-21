# -*- coding: utf-8 -*-
import asyncio
import logging
import traceback
from asyncio import Future
from typing import Optional, Dict, Callable, List
from urllib.parse import urljoin

import aiohttp
import ujson as json
import websockets
import websockets.protocol
from pyee import EventEmitter
from websockets import WebSocketClientProtocol

from .accessibility import Accessibility
from .animation import Animation
from .applicationcache import ApplicationCache
from .audits import Audits
from .browser import Browser
from .cachestorage import CacheStorage
from .console import Console
from .css import CSS
from .database import Database
from .debugger import Debugger
from .deviceorientation import DeviceOrientation
from .dom import DOM
from .domdebugger import DOMDebugger
from .domsnapshot import DOMSnapshot
from .domstorage import DOMStorage
from .emulation import Emulation
from .headlessexperimental import HeadlessExperimental
from .heapprofiler import HeapProfiler
from .indexeddb import IndexedDB
from .input import Input
from .inspector import Inspector
from .io import IO
from .layertree import LayerTree
from .log import Log
from .memory import Memory
from .network import Network
from .overlay import Overlay
from .page import Page
from .performance import Performance
from .profiler import Profiler
from .runtime import Runtime
from .schema import Schema
from .security import Security
from .serviceworker import ServiceWorker
from .storage import Storage
from .systeminfo import SystemInfo
from .target import Target
from .tethering import Tethering
from .tracing import Tracing

__all__ = ["Client"]

logger = logging.getLogger(__name__)


try:
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass

DEFAULT_HOST: str = "localhost"
DEFAULT_PORT: int = 9222
DEFAULT_URL: str = "http://localhost:9222"


def createProtocolError(method, msg) -> str:
    error = msg["error"]
    data = error.get("data")
    emsg = f"Protocol Error ({method}): {error.get('message')}"
    if data:
        emsg += f" {data}"
    return emsg


class NetworkError(Exception):
    """Network/Protocol related exception."""


class ClientError(Exception):
    """Network/Protocol related exception."""


class Client(EventEmitter):
    """Websocket Connection To The Remote Browser"""

    def __init__(self, ws_url: str) -> None:
        super().__init__(loop=asyncio.get_event_loop())
        self._url: str = ws_url
        self._lastId: int = 0
        self._callbacks: Dict[int, Future] = dict()
        self.connected: bool = False
        self._ws: WebSocketClientProtocol = None
        self._recv_fut: Optional[Future] = None
        self._closeCallback: Optional[Callable[[], None]] = None

        self.Accessibility: Accessibility = Accessibility(self)
        self.Animation: Animation = Animation(self)
        self.ApplicationCache: ApplicationCache = ApplicationCache(self)
        self.Audits: Audits = Audits(self)
        self.Browser: Browser = Browser(self)
        self.CacheStorage: CacheStorage = CacheStorage(self)
        self.Console: Console = Console(self)
        self.CSS: CSS = CSS(self)
        self.Database: Database = Database(self)
        self.Debugger: Debugger = Debugger(self)
        self.DeviceOrientation: DeviceOrientation = DeviceOrientation(self)
        self.DOM: DOM = DOM(self)
        self.DOMDebugger: DOMDebugger = DOMDebugger(self)
        self.DOMSnapshot: DOMSnapshot = DOMSnapshot(self)
        self.DOMStorage: DOMStorage = DOMStorage(self)
        self.Emulation: Emulation = Emulation(self)
        self.HeadlessExperimental: HeadlessExperimental = HeadlessExperimental(self)
        self.HeapProfiler: HeapProfiler = HeapProfiler(self)
        self.IO: IO = IO(self)
        self.IndexedDB: IndexedDB = IndexedDB(self)
        self.Input: Input = Input(self)
        self.Inspector: Inspector = Inspector(self)
        self.LayerTree: LayerTree = LayerTree(self)
        self.Log: Log = Log(self)
        self.Memory: Memory = Memory(self)
        self.Network: Network = Network(self)
        self.Overlay: Overlay = Overlay(self)
        self.Page: Page = Page(self)
        self.Performance: Performance = Performance(self)
        self.Profiler: Profiler = Profiler(self)
        self.Runtime: Runtime = Runtime(self)
        self.Schema: Schema = Schema(self)
        self.Security: Security = Security(self)
        self.ServiceWorker: ServiceWorker = ServiceWorker(self)
        self.Storage: Storage = Storage(self)
        self.SystemInfo: SystemInfo = SystemInfo(self)
        self.Target: Target = Target(self)
        self.Tethering: Tethering = Tethering(self)
        self.Tracing: Tracing = Tracing(self)

    def __await__(self) -> "Client":
        yield from self.connect().__await__()
        return self

    @property
    def url(self) -> str:
        """Get connected WebSocket url."""
        return self.url

    @staticmethod
    async def connect_to_remote(url: Optional[str] = DEFAULT_URL) -> "Client":
        tabs = await Client.List(url=url)
        for tab in tabs:
            if tab["type"] == "page":
                return await Client(tab["webSocketDebuggerUrl"])
        raise ClientError("Could not find a page to connect to.")

    async def connect(self) -> None:
        self._ws = await websockets.client.connect(
            self._url, compression=None, max_queue=0, timeout=20
        )
        self._recv_fut = asyncio.ensure_future(self._recv_loop(), loop=self._loop)

    async def _recv_loop(self) -> None:
        self.connected = True
        while self.connected:
            try:
                resp = await self._ws.recv()
                if resp:
                    self._on_message(resp)
            except (websockets.ConnectionClosed, ConnectionResetError) as e:
                logger.info("connection closed")
                break
        if self.connected:
            await self.dispose()

    def send(self, method: str, params: Optional[dict] = None) -> Future:
        if self._lastId and not self.connected:
            raise NetworkError("Connection is closed")
        if params is None:
            params = dict()
        self._lastId += 1
        _id = self._lastId
        msg = json.dumps(dict(method=method, params=params, id=_id))
        asyncio.ensure_future(self._send_async(msg, _id), loop=self._loop)
        callback = self._loop.create_future()
        self._callbacks[_id] = callback
        callback.method = method  # type: ignore
        return callback

    async def _send_async(self, msg: str, callback_id: int) -> None:
        while not self.connected:
            await asyncio.sleep(0)

        try:
            await self._ws.send(msg)
        except websockets.ConnectionClosed:
            logger.error("connection unexpectedly closed")
            callback = self._callbacks.get(callback_id, None)
            if callback and not callback.done():
                callback.set_result(None)
                await self.dispose()

    async def dispose(self) -> None:
        """Close all connection."""
        self.connected = False
        await self._on_close()

    def set_close_callback(self, callback: Callable[[], None]) -> None:
        """Set closed callback."""
        self._closeCallback = callback

    def _on_message(self, message: str) -> None:
        msg = json.loads(message)
        if msg.get("id") in self._callbacks:
            self._on_response(msg)
        else:
            self._on_unsolicited(msg)

    def _on_response(self, msg: dict) -> None:
        callback = self._callbacks.pop(msg.get("id", -1))
        if callback and not callback.done():
            if "error" in msg:
                callback.set_exception(
                    NetworkError(createProtocolError(callback.method, msg))
                )
            else:
                callback.set_result(msg.get("result"))

    def _on_unsolicited(self, msg: dict) -> None:
        params = msg.get("params", {})
        method = msg.get("method", "")
        try:
            self.emit(method, params)
        except Exception as e:
            traceback.print_exc()
            print("_on_unsolicited error", e)
            print("_on_unsolicited error", params)

    async def _on_close(self) -> None:
        if self._closeCallback:
            self._closeCallback()
            self._closeCallback = None

        for cb in self._callbacks.values():
            cb.cancel()
        self._callbacks.clear()

        # close connection
        if not self._recv_fut.done():
            self._recv_fut.cancel()

        try:
            await self._ws.close()
        except:
            pass

    @classmethod
    async def JSON(
        cls,
        url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[int] = DEFAULT_PORT,
        secure: Optional[bool] = False,
    ) -> Dict[str, str]:
        async with aiohttp.ClientSession() as session:
            if url is None:
                url = f"{'https:' if secure else 'http:'}//{host}:{port}/json"
            if not url.endswith("/json"):
                url = urljoin(url, "json")
            data = await session.get(url)
            json_ = await data.json()
        return json_

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
    ) -> List[Dict[str, str]]:
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
