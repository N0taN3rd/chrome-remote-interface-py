# -*- coding: utf-8 -*-
import asyncio
import logging
import traceback
from asyncio import Future, AbstractEventLoop, Task
from typing import Callable, Optional, Dict, ClassVar, Union
from typing import List, Any
from urllib.parse import urljoin, urlparse

import aiohttp
import attr
import ujson as json
import websockets
import websockets.protocol
from pyee import EventEmitter
from websockets import WebSocketClientProtocol

from .protocol.accessibility import Accessibility
from .protocol.animation import Animation
from .protocol.applicationcache import ApplicationCache
from .protocol.audits import Audits
from .protocol.browser import Browser
from .protocol.cachestorage import CacheStorage
from .protocol.console import Console
from .protocol.css import CSS
from .protocol.database import Database
from .protocol.debugger import Debugger
from .protocol.deviceorientation import DeviceOrientation
from .protocol.dom import DOM
from .protocol.domdebugger import DOMDebugger
from .protocol.domsnapshot import DOMSnapshot
from .protocol.domstorage import DOMStorage
from .protocol.emulation import Emulation
from .protocol.headlessexperimental import HeadlessExperimental
from .protocol.heapprofiler import HeapProfiler
from .protocol.indexeddb import IndexedDB
from .protocol.input import Input
from .protocol.inspector import Inspector
from .protocol.io import IO
from .protocol.layertree import LayerTree
from .protocol.log import Log
from .protocol.memory import Memory
from .protocol.network import Network
from .protocol.overlay import Overlay
from .protocol.page import Page
from .protocol.performance import Performance
from .protocol.profiler import Profiler
from .protocol.runtime import Runtime
from .protocol.schema import Schema
from .protocol.security import Security
from .protocol.serviceworker import ServiceWorker
from .protocol.storage import Storage
from .protocol.systeminfo import SystemInfo
from .protocol.target import Target
from .protocol.tethering import Tethering
from .protocol.tracing import Tracing
from .protogen.generate import dynamically_generate_domains

__all__ = [
    "Client",
    "ClientError",
    "connect",
    "TargetSession",
    "NetworkError",
    "DEFAULT_HOST",
    "DEFAULT_PORT",
    "DEFAULT_URL",
    "createProtocolError",
    "ConnectEvents",
    "gen_proto_classes",
]

DEFAULT_HOST: str = "localhost"
DEFAULT_PORT: int = 9222
DEFAULT_URL: str = "http://localhost:9222"

logger = logging.getLogger(__name__)


def createProtocolError(method, msg) -> str:
    error = msg["error"]
    data = error.get("data")
    emsg = f"Protocol Error ({method}): {error.get('message')}"
    if data:
        emsg += f" {data}"
    return emsg


@attr.dataclass
class ConnectEvents(object):
    Disconnected: str = attr.ib(default="Disconnected")


class NetworkError(Exception):
    """Network/Protocol related exception."""


class ClientError(Exception):
    """Client specific exception."""


class Client(EventEmitter):
    """Chrome DevTools Protocol Client Class.

    This class provides a simple abstraction for using the CDP.
    """

    Events: ClassVar[ConnectEvents] = ConnectEvents()

    def __init__(
        self,
        ws_url: str,
        loop: Optional[AbstractEventLoop] = None,
        proto_def: Optional[dict] = None,
    ) -> None:
        """Construct a new instance of the CDP Client.

        :param ws_url: The WS endpoint of the remote instance
        :param loop:  Optional event loop to use. Defaults to asyncio.get_event_loop
        :param proto_def: Optional protocol domain classes to be used rather than the pre-generated ones
        """
        if loop is None:
            loop = asyncio.get_event_loop()
        super().__init__(loop=loop)
        self.connected: bool = False
        self._url: str = ws_url
        self._lastId: int = 0
        self._callbacks: Dict[int, Future] = dict()
        self._ws: WebSocketClientProtocol = None
        self._recv_task: Optional[Task] = None
        self._closeCallback: Optional[Callable[[], None]] = None
        self._sessions: Dict[str, TargetSession] = dict()
        self._proto_def = proto_def
        self._closed: bool = False

        if proto_def is None:
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
        else:
            for domain, clazz in proto_def.items():
                setattr(self, domain, clazz(self))

    @staticmethod
    def fromSession(sessionOrClient: Union["Client", "TargetSession"]) -> "Client":
        if isinstance(sessionOrClient, TargetSession):
            return sessionOrClient._connection
        return sessionOrClient

    @property
    def url(self) -> str:
        """Get connected WebSocket url."""
        return self._url

    async def connect(self) -> None:
        """Connect to the remote websocket endpoint"""
        self._ws = await websockets.client.connect(
            self._url,
            ping_interval=None,  # chrome no ping pong and websockets closes down on no pong :'(
            max_size=None,
            compression=None,
            max_queue=2 ** 7,
            loop=self._loop,
        )
        self._recv_task = self._loop.create_task(self._recv_loop())

    async def createTargetSession(self, targetId: str) -> "TargetSession":
        """Attach to the target specified by target id and create new TargetSession for direct communication to it."""
        resp = await self.send("Target.attachToTarget", {"targetId": targetId})
        sessionId = resp.get("sessionId")
        session = TargetSession(self, targetId, sessionId)
        self._sessions[sessionId] = session
        return session

    def set_close_callback(self, callback: Callable[[], None]) -> None:
        """Set closed callback."""
        self._closeCallback = callback

    def send(self, method: str, params: Optional[Dict] = None) -> Future:
        """Send a protocol msg to the remote chrome instance.

        :param method: The method to be used
        :param params: The optional parameters (arguments) for the command
        :return: A future that resolves once the commands response is received
        """
        if self._lastId and not self.connected:
            raise NetworkError("Connection is closed")
        if params is None:
            params = dict()
        self._lastId += 1
        _id = self._lastId
        msg = json.dumps(dict(method=method, params=params, id=_id))
        self._loop.create_task(self._send_async(msg, _id))
        callback = self._loop.create_future()
        self._callbacks[_id] = callback
        callback.method = method  # type: ignore
        return callback

    async def dispose(self) -> None:
        """Close all connection."""
        self.connected = False
        await self._on_close()

    async def _recv_loop(self) -> None:
        """Loop that listens for messages from the remote chrome instance and handles them.

        When a msg is received, the _on_message method is called with the raw msg contents.
        """
        self.connected = True
        while self.connected:
            try:
                resp = await self._ws.recv()
                if resp:
                    self._on_message(resp)
            except (websockets.ConnectionClosed, ConnectionResetError) as e:
                logger.info("connection closed")
                break
            await asyncio.sleep(0)
        if self.connected:
            self._loop.create_task(self.dispose())

    async def _send_async(self, msg: str, callback_id: int) -> None:
        """Actually send the msg to remote instance.

        :param msg: The msg to send
        :param callback_id: The id identifying the callback associated with the msg
        """
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

    def _on_message(self, message: str) -> None:
        """Handles a message received from the remote instance.

        If the message contains a callback id, _on_response is called with the parsed message.
        Otherwise _on_unsolicited is called with the parsed message.
        :param message: The JSON message string.
        """
        msg = json.loads(message)
        if msg.get("id") in self._callbacks:
            self._on_response(msg)
        else:
            self._on_unsolicited(msg)

    def _on_response(self, msg: Dict) -> None:
        """Handles a response to protocol method.

        If the response is an error, the callback (future) associated with the messages id has
        the exception set otherwise the result of the callback will be the messages results.
        :param msg: The response to a protocol method issued
        """
        callback = self._callbacks.pop(msg.get("id", -1))
        if callback and not callback.done():
            if "error" in msg:
                callback.set_exception(
                    NetworkError(createProtocolError(callback.method, msg))
                )
            else:
                callback.set_result(msg.get("result"))

    def _on_unsolicited(self, msg: Dict) -> None:
        """Emits the message ent by the remote chrome instance that were not requested as the method -> params events.

        If an listener to one of these unsolicited messages throws an error. It is caught here and reported.
        :param msg: The unsolicited message
        """
        params = msg.get("params", {})
        method = msg.get("method", "")
        sessionId = params.get("sessionId")
        try:
            if method == "Target.receivedMessageFromTarget":
                session = self._sessions.get(sessionId)
                if session:
                    session.on_message(params.get("message"))
            elif method == "Target.detachedFromTarget":
                session = self._sessions.get(sessionId)
                if session:
                    session.on_closed()
                    del self._sessions[sessionId]
            else:
                self.emit(method, params)
        except Exception as e:
            traceback.print_exc()
            print(f"_on_unsolicited error {method}", e)
            print(f"_on_unsolicited error {method}", params)

    async def _on_close(self) -> None:
        """Closes the websocket connection and cleans up internals.

        All pending protocol method callbacks are canceled and the receive loop is stopped.
        Calls the on close callback if it was supplied and the "connection-closed" method is emitted
        """
        if self._closed:
            return
        self._closed = True
        if self._closeCallback:
            self._closeCallback()
            self._closeCallback = None

        for cb in self._callbacks.values():
            if not cb.done():
                cb.set_exception(
                    NetworkError(f"Protocol error {cb.method}: Target closed.")
                )
        self._callbacks.clear()

        for session in self._sessions.values():
            session.on_closed()
        self._sessions.clear()

        # close connection
        if not self._ws.closed:
            try:
                await self._ws.close()
            except Exception:
                pass

        if self._recv_task is not None and not self._recv_task.done():
            self._recv_task.cancel()

        self.emit(self.Events.Disconnected)

    @staticmethod
    async def Close(
        id: str,
        url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[int] = DEFAULT_PORT,
        secure: Optional[bool] = False,
    ) -> Dict[str, str]:
        """Close an open target/tab of the remote instance.

        :param id: Target id. Required, no default
        :param url: Base HTTP endpoint url to use (e.g. http(s)://localhost:9222)
        :param host: HTTP frontend host. Defaults to localhost
        :param port: HTTP frontend port. Defaults to 9222
        :param secure: HTTPS/WSS frontend. Defaults to false
        """
        async with aiohttp.ClientSession() as session:
            if url is None:
                url = f"{'https:' if secure else 'http:'}//{host}:{port}/json/close"
            if not url.endswith("json/close"):
                url = urljoin(url, "json/close")
            data = await session.get(urljoin(url, id))
            json_ = await data.json()
        return json_

    @staticmethod
    async def Activate(
        id: str,
        url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[int] = DEFAULT_PORT,
        secure: Optional[bool] = False,
    ) -> Dict[str, str]:
        """Activate an open target/tab of the remote instance.

        :param id: Target id. Required, no default
        :param url: Base HTTP endpoint url to use (e.g. http(s)://localhost:9222)
        :param host: HTTP frontend host. Defaults to localhost
        :param port: HTTP frontend port. Defaults to 9222
        :param secure: HTTPS/WSS frontend. Defaults to false
        """
        async with aiohttp.ClientSession() as session:
            if url is None:
                url = f"{'https:' if secure else 'http:'}//{host}:{port}/json/activate"
            if not url.endswith("json/activate"):
                url = urljoin(url, "json/activate")
            data = await session.get(urljoin(url, id))
            json_ = await data.json()
            return json_

    @staticmethod
    async def List(
        url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[int] = DEFAULT_PORT,
        secure: Optional[bool] = False,
    ) -> List[Dict[str, str]]:
        """Request a list of the available open targets/tabs of the remote instance.

        :param url: Base HTTP endpoint url to use (e.g. http(s)://localhost:9222)
        :param host: HTTP frontend host. Defaults to localhost
        :param port: HTTP frontend port. Defaults to 9222
        :param secure: HTTPS/WSS frontend. Defaults to false
        """
        async with aiohttp.ClientSession() as session:
            if url is None:
                url = f"{'https:' if secure else 'http:'}//{host}:{port}"
            data = await session.get(urljoin(url, "json/list"))
            json_ = await data.json()
            return json_

    @staticmethod
    async def New(
        url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[int] = DEFAULT_PORT,
        secure: Optional[bool] = False,
    ) -> Dict[str, str]:
        """Create a new target/tab in the remote instance.

        :param url: Base HTTP endpoint url to use (e.g. http(s)://localhost:9222)
        :param host: HTTP frontend host. Defaults to localhost
        :param port: HTTP frontend port. Defaults to 9222
        :param secure: HTTPS/WSS frontend. Defaults to false
        :return:
        """
        async with aiohttp.ClientSession() as session:
            if url is None:
                url = f"{'https:' if secure else 'http:'}//{host}:{port}"
            data = await session.get(urljoin(url, "json/new"))
            json_ = await data.json()
            return json_

    @staticmethod
    async def Protocol(
        url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[int] = DEFAULT_PORT,
        secure: Optional[bool] = False,
    ) -> Dict[str, str]:
        """Fetch the Chrome DevTools Protocol descriptor.

        :param url: Base HTTP endpoint url to use (e.g. http(s)://localhost:9222)
        :param host: HTTP frontend host. Defaults to localhost
        :param port: HTTP frontend port. Defaults to 9222
        :param secure: HTTPS/WSS frontend. Defaults to false
        """
        async with aiohttp.ClientSession() as session:
            if url is None:
                url = f"{'https:' if secure else 'http:'}//{host}:{port}"
            data = await session.get(urljoin(url, "json/protocol"))
            json_ = await data.json()
            return json_

    @staticmethod
    async def Version(
        url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[int] = DEFAULT_PORT,
        secure: Optional[bool] = False,
    ) -> Dict[str, str]:
        """Request version information from the remote instance.

        :param url: Base HTTP endpoint url to use (e.g. http(s)://localhost:9222)
        :param host: HTTP frontend host. Defaults to localhost
        :param port: HTTP frontend port. Defaults to 9222
        :param secure: HTTPS/WSS frontend. Defaults to false
        """
        async with aiohttp.ClientSession() as session:
            if url is None:
                url = f"{'https:' if secure else 'http:'}//{host}:{port}"
            data = await session.get(urljoin(url, "json/version"))
            json_ = await data.json()
            return json_

    def __await__(self) -> "Client":
        yield from self.connect().__await__()
        return self

    def __str__(self):
        return f"Client(wsurl={self._url}, connected={self.connected})"

    def __repr__(self):
        return self.__str__()


class TargetSession(EventEmitter):
    def __init__(self, client: Client, targetId: str, sessionId: str) -> None:
        """Make new session."""
        super().__init__(loop=client._loop)
        self._lastId: int = 0
        self._callbacks: Dict[int, Future] = dict()
        self._connection: Client = client
        self._targetId: str = targetId
        self._sessionId: str = sessionId
        self._sessions: Dict[str, TargetSession] = dict()

        if self._connection._proto_def is None:
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
        else:
            for domain, clazz in self._connection._proto_def.items():
                setattr(self, domain, clazz(self))

    def send(self, method: str, params: Optional[dict] = None) -> Future:
        """Send message to the connected session.
        :arg str method: Protocol method name.
        :arg dict params: Optional method parameters.
        """
        if not self._connection:
            raise NetworkError(
                f"Protocol Error ({method}): Session closed. Most likely the "
                f"target has been closed."
            )

        if params is None:
            params = dict()
        self._lastId += 1
        _id = self._lastId
        msg = json.dumps(dict(id=_id, method=method, params=params))
        callback = self._connection._loop.create_future()
        self._callbacks[_id] = callback
        callback.method = method
        try:
            self._connection.send(
                "Target.sendMessageToTarget",
                {"sessionId": self._sessionId, "message": msg},
            )
        except Exception as e:
            # The response from target might have been already dispatched
            if _id in self._callbacks:
                cb = self._callbacks[_id]
                del self._callbacks[_id]
                if not cb.done():
                    cb.set_exception(NetworkError(e.args[0]))
        return callback

    async def detach(self) -> None:
        """Detach session from target.
        Once detached, session won't emit any events and can't be used to send
        messages.
        """
        if not self._connection:
            raise NetworkError("TargetSession already closed.")
        await self._connection.send(
            "Target.detachFromTarget", {"sessionId": self._sessionId}
        )

    def create_session(self, targetId: str, sessionId: str) -> "TargetSession":
        sesh = TargetSession(self._connection, targetId, sessionId)
        self._sessions[sessionId] = sesh
        return sesh

    def on_message(self, message: str) -> None:
        obj = json.loads(message)
        _id = obj.get("id")
        if _id and _id in self._callbacks:
            callback = self._callbacks.pop(_id)
            if "error" in obj:
                callback.set_exception(
                    NetworkError(createProtocolError(callback.method, obj))
                )
            else:
                result = obj.get("result")
                if callback and not callback.done():
                    callback.set_result(result)
        else:
            method = obj.get("method")
            params = obj.get("params")
            if method == "Target.receivedMessageFromTarget":
                session = self._sessions.get(params.get("sessionId"))
                if session is not None:
                    session.on_message(params.get("message"))
            elif method == "Target.detachedFromTarget":
                sessionId = params.get("sessionId")
                session = self._sessions.get(sessionId)
                if session is not None:
                    session.on_closed()
                    del self._sessions[sessionId]
            self.emit(method, params)

    def on_closed(self) -> None:
        for cb in self._callbacks.values():
            if not cb.done():
                cb.set_exception(
                    NetworkError(
                        f"Protocol error {cb.method}: Target closed."  # type: ignore
                    )
                )
        self._callbacks.clear()
        self._connection = None

    def __repr__(self):
        return f"TargetSession(targetId={self._targetId:}, sessionId={self._sessionId})"


async def gen_proto_classes(url: str) -> Dict[str, Any]:
    purl = urlparse(url)
    host, port = purl.netloc.split(":")
    is_https = purl.scheme.startswith("wss") or purl.scheme.startswith("https")
    raw_proto = await Client.Protocol(host=host, port=port, secure=is_https)
    proto_def = await dynamically_generate_domains(raw_proto)
    return proto_def


async def connect(
    url: Optional[str] = DEFAULT_URL,
    loop: Optional[AbstractEventLoop] = None,
    remote: bool = False,
) -> "Client":
    """Convince function for creating a CDP client and connecting it to the remote instance.

    :param url: URL or WS URL to use for making the CDP connection. Defaults to http://localhost:9222
    :param loop: The event loop instance to use. Defaults to asyncio.get_event_loop
    :param remote: Boolean indicating if the protocol should be fetched from the remote instance or
    to use the local one. Defaults to False (use local)
    :return: CDP Client
    """
    if remote:
        proto_def = await gen_proto_classes(url)
    else:
        proto_def = None

    if not url.startswith("ws"):
        tabs = await Client.List(url=url)
        for tab in tabs:
            if tab["type"] == "page":
                return await Client(
                    tab["webSocketDebuggerUrl"], loop=loop, proto_def=proto_def
                )
        raise ClientError("Could not find a page to connect to.")
    return await Client(url, loop=loop, proto_def=proto_def)
