# -*- coding: utf-8 -*-
from asyncio import AbstractEventLoop
from typing import Optional, Union

from .connection import Connection, CDPSession
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
from .protocol.fetch import Fetch
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

__all__ = [
    "Client",
    "TargetSession",
]


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
        :param proto_def: Optional protocol domain classes to be used rather than
        the pre-generated ones
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
            self.Fetch: Fetch = Fetch(self)
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
        """Attach to the target specified by target id and create new TargetSession for direct
        communication to it."""
        resp = await self.send("Target.attachToTarget", {"targetId": targetId})
        sessionId = resp.get("sessionId")
        session = TargetSession(
            self, resp.get("type", "unknown"), sessionId, proto_def=self._proto_def
        )
        self._sessions[sessionId] = session
        return session


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

    def createTargetSession(self, targetType: str, sessionId: str) -> "TargetSession":
        sesh = TargetSession(self, targetType, sessionId, proto_def=self._proto_def)
        self._sessions[sessionId] = sesh
        return sesh
