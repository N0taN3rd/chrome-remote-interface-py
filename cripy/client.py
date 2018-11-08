# -*- coding: utf-8 -*-
from asyncio import AbstractEventLoop
from typing import List, Optional, Dict, Any, Union, Tuple
from urllib.parse import urljoin, urlparse

import aiohttp

from .connection import Connection, CDPSession
from .errors import ClientError
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
from .protocol.testing import Testing
from .protocol.tethering import Tethering
from .protocol.tracing import Tracing
from .protogen.generate import dynamically_generate_domains

__all__ = [
    "Client",
    "TargetSession",
    "DEFAULT_HOST",
    "DEFAULT_PORT",
    "DEFAULT_URL",
    "connect",
    "gen_proto_classes",
]

DEFAULT_HOST: str = "localhost"
DEFAULT_PORT: int = 9222
DEFAULT_URL: str = "http://localhost:9222"


class Client(Connection):
    def __init__(
        self,
        ws_url: str,
        loop: Optional[AbstractEventLoop] = None,
        proto_def: Optional[dict] = None,
    ) -> None:
        """Construct a new instance of the ChromeRemoteInterface Client.

        :param ws_url: The WS endpoint of the remote instance
        :param loop:  Optional event loop to use. Defaults to asyncio.get_event_loop
        :param proto_def: Optional protocol domain classes to be used rather than the pre-generated ones
        """
        super().__init__(ws_url, loop)
        self._proto_def: Optional[dict] = proto_def
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
            self.Testing: Testing = Testing(self)
            self.Tethering: Tethering = Tethering(self)
            self.Tracing: Tracing = Tracing(self)
        else:
            for domain, clazz in proto_def.items():
                setattr(self, domain, clazz(self))

    async def createTargetSession(self, targetId: str) -> "TargetSession":
        """Attach to the target specified by target id and create new TargetSession for direct communication to it."""
        resp = await self.send("Target.attachToTarget", {"targetId": targetId})
        sessionId = resp.get("sessionId")
        session = TargetSession(
            self, resp.get("type", "unknown"), sessionId, proto_def=self._proto_def
        )
        self._sessions[sessionId] = session
        return session

    @staticmethod
    async def Close(
        target_id: str,
        frontend_url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[Union[int, str]] = DEFAULT_PORT,
        secure: Optional[bool] = False,
    ) -> Tuple[int, str]:
        """Close an open target/tab of the remote instance.

        :param target_id: Target id. Required, no default
        :param frontend_url: Base HTTP endpoint url to use (e.g. http(s)://localhost:9222)
        :param host: HTTP frontend host. Defaults to localhost
        :param port: HTTP frontend port. Defaults to 9222
        :param secure: HTTPS/WSS frontend. Defaults to false
        """
        async with aiohttp.ClientSession() as session:
            if frontend_url is None:
                frontend_url = (
                    f"{'https:' if secure else 'http:'}//{host}:{port}/json/close/"
                )
            if "json/close" in frontend_url and not frontend_url.endswith("/"):
                frontend_url += "/"
            if not frontend_url.endswith("json/close/"):
                frontend_url = urljoin(frontend_url, "json/close/")
            res = await session.get(urljoin(frontend_url, target_id))
            text = await res.text()
            return res.status, text

    @staticmethod
    async def Activate(
        target_id: str,
        frontend_url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[Union[int, str]] = DEFAULT_PORT,
        secure: Optional[bool] = False,
    ) -> Tuple[int, str]:
        """Activate an open target/tab of the remote instance.

        :param target_id: Target id. Required, no default
        :param frontend_url: Base HTTP endpoint url to use (e.g. http(s)://localhost:9222)
        :param host: HTTP frontend host. Defaults to localhost
        :param port: HTTP frontend port. Defaults to 9222
        :param secure: HTTPS/WSS frontend. Defaults to false
        """
        async with aiohttp.ClientSession() as session:
            if frontend_url is None:
                frontend_url = (
                    f"{'https:' if secure else 'http:'}//{host}:{port}/json/activate/"
                )
            if "json/activate" in frontend_url and not frontend_url.endswith("/"):
                frontend_url += "/"
            if not frontend_url.endswith("json/activate/"):
                frontend_url = urljoin(frontend_url, "json/activate/")
            res = await session.get(urljoin(frontend_url, target_id))
            text = await res.text()
            return res.status, text

    @staticmethod
    async def Protocol(
        frontend_url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[Union[int, str]] = DEFAULT_PORT,
        secure: Optional[bool] = False,
    ) -> Dict[str, Union[List[Dict], Dict]]:
        """Fetch the Chrome DevTools Protocol descriptor.

        :param frontend_url: Base HTTP endpoint url to use (e.g. http(s)://localhost:9222)
        :param host: HTTP frontend host. Defaults to localhost
        :param port: HTTP frontend port. Defaults to 9222
        :param secure: HTTPS/WSS frontend. Defaults to false
        """
        async with aiohttp.ClientSession() as session:
            if frontend_url is None:
                frontend_url = (
                    f"{'https:' if secure else 'http:'}//{host}:{port}/json/protocol"
                )
            if not frontend_url.endswith("json/protocol"):
                frontend_url = urljoin(frontend_url, "json/protocol")
            data = await session.get(frontend_url)
            return await data.json()

    @staticmethod
    async def List(
        frontend_url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[Union[int, str]] = DEFAULT_PORT,
        secure: Optional[bool] = False,
    ) -> List[Dict[str, str]]:
        """Request a list of the available open targets/tabs of the remote instance.

        :param frontend_url: Base HTTP endpoint url to use (e.g. http(s)://localhost:9222)
        :param host: HTTP frontend host. Defaults to localhost
        :param port: HTTP frontend port. Defaults to 9222
        :param secure: HTTPS/WSS frontend. Defaults to false
        """
        async with aiohttp.ClientSession() as session:
            if frontend_url is None:
                frontend_url = (
                    f"{'https:' if secure else 'http:'}//{host}:{port}/json/list"
                )
            if not frontend_url.endswith("json/list"):
                frontend_url = urljoin(frontend_url, "json/list")
            data = await session.get(frontend_url)
            return await data.json()

    @staticmethod
    async def New(
        url: Optional[str] = None,
        frontend_url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[Union[int, str]] = DEFAULT_PORT,
        secure: Optional[bool] = False,
    ) -> Dict[str, str]:
        """Create a new target/tab in the remote instance.

        :param url: The URL for the new tab. Defaults to about:blank
        :param frontend_url: Base HTTP endpoint url to use (e.g. http(s)://localhost:9222)
        :param host: HTTP frontend host. Defaults to localhost
        :param port: HTTP frontend port. Defaults to 9222
        :param secure: HTTPS/WSS frontend. Defaults to false
        :return:
        """
        async with aiohttp.ClientSession() as session:
            if frontend_url is None:
                frontend_url = f"{'https:' if secure else 'http:'}//{host}:{port}"
            if not frontend_url.endswith("json/new"):
                frontend_url = urljoin(frontend_url, "json/new")
            if url is not None:
                frontend_url = f"{frontend_url}?{url}"
            data = await session.get(frontend_url)
            return await data.json()

    @staticmethod
    async def Version(
        frontend_url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[Union[int, str]] = DEFAULT_PORT,
        secure: Optional[bool] = False,
    ) -> Dict[str, str]:
        """Request version information from the remote instance.

        :param frontend_url: Base HTTP endpoint url to use (e.g. http(s)://localhost:9222)
        :param host: HTTP frontend host. Defaults to localhost
        :param port: HTTP frontend port. Defaults to 9222
        :param secure: HTTPS/WSS frontend. Defaults to false
        """
        async with aiohttp.ClientSession() as session:
            if frontend_url is None:
                frontend_url = (
                    f"{'https:' if secure else 'http:'}//{host}:{port}/json/version"
                )
            if not frontend_url.endswith("json/version"):
                frontend_url = urljoin(frontend_url, "json/version")
            data = await session.get(frontend_url)
            return await data.json()

    def __await__(self) -> "Client":
        yield from self.connect().__await__()
        return self

    def __str__(self) -> str:
        return f"Client(wsurl={self._url}, connected={self.connected})"


class TargetSession(CDPSession):
    def __init__(
        self,
        client: Union[Client, "TargetSession"],
        targetType: str,
        sessionId: str,
        proto_def: Optional[dict] = None,
    ) -> None:
        """Make new session."""
        super().__init__(client, targetType, sessionId)
        self._proto_def: Optional[dict] = proto_def
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
            self.Testing: Testing = Testing(self)
            self.Tethering: Tethering = Tethering(self)
            self.Tracing: Tracing = Tracing(self)
        else:
            for domain, clazz in proto_def.items():
                setattr(self, domain, clazz(self))

    def createSession(self, targetType: str, sessionId: str) -> "TargetSession":
        sesh = TargetSession(
            self, targetType, sessionId, proto_def=self._proto_def
        )
        self._sessions[sessionId] = sesh
        return sesh

    def __str__(self) -> str:
        return f"TargetSession(target={self._targetType}, sessionId={self._sessionId})"


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
) -> Client:
    """Convince function for creating an instance of the ChromeRemoteInterface and connecting it to the remote instance.

    :param url: URL or WS URL to use for making the CDP connection. Defaults to http://localhost:9222
    :param loop: The event loop instance to use. Defaults to asyncio.get_event_loop
    :param remote: Boolean indicating if the protocol should be fetched from the remote instance or
    to use the local one. Defaults to False (use local)
    :return: ChromeRemoteInterface
    """
    ws_url = None
    if not url.startswith("ws"):
        tabs = await Client.List(frontend_url=url)
        for tab in tabs:
            if tab["type"] == "page":
                ws_url = tab["webSocketDebuggerUrl"]
                break
        if ws_url is None:
            raise ClientError("Could not find a page to connect to.")
    else:
        ws_url = url
    if remote:
        proto_def = await gen_proto_classes(ws_url)
    else:
        proto_def = None
    return await Client(ws_url, loop=loop, proto_def=proto_def)
