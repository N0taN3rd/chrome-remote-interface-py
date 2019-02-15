# -*- coding: utf-8 -*-
from asyncio import AbstractEventLoop
from typing import Dict, Optional, Union

from .connection import Connection, CDPSession
from .protocol.accessibility import Accessibility
from .protocol.animation import Animation
from .protocol.applicationcache import ApplicationCache
from .protocol.audits import Audits
from .protocol.browser import Browser
from .protocol.cachestorage import CacheStorage
from .protocol.cast import Cast
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

__all__ = ["Client", "TargetSession"]


class Client(Connection):
    def __init__(
        self,
        ws_url: str,
        flatten_sessions: bool = False,
        proto_def: Optional[Dict] = None,
        loop: Optional[AbstractEventLoop] = None,
    ) -> None:
        """Construct a new instance of the ChromeRemoteInterface Client.

        :param ws_url: The WS endpoint of the remote instance
        :param flatten_sessions: Enables "flat" access to the session via specifying sessionId
        attribute in the commands
        :param proto_def: Optional protocol domain classes to be used rather than
        the pre-generated ones
        :param loop:  Optional event loop to use. Defaults to asyncio.get_event_loop
        """
        super().__init__(ws_url, flatten_sessions, loop)
        self._proto_def: Optional[Dict] = proto_def
        if proto_def is None:
            self.Accessibility: Accessibility = Accessibility(self)
            self.Animation: Animation = Animation(self)
            self.ApplicationCache: ApplicationCache = ApplicationCache(self)
            self.Audits: Audits = Audits(self)
            self.Browser: Browser = Browser(self)
            self.CacheStorage: CacheStorage = CacheStorage(self)
            self.Cast: Cast = Cast(self)
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

    def session(self, session_id: str) -> Optional["TargetSession"]:
        return self._sessions.get(session_id)

    async def create_session(self, target_id: str) -> "TargetSession":
        """Attach to the target specified by the supplied target id and creates new CDPSession for
        direct communication to it

        :param target_id: The id of the target connecting to
        :return: A new session connected to the target
        """
        params = {"targetId": target_id}
        if self._flatten_sessions:
            params["flatten"] = self._flatten_sessions
        resp = await self.send("Target.attachToTarget", params)
        session_id = resp.get("sessionId")
        if self._flatten_sessions:
            session = self._sessions.get(session_id)
            if session:
                return session
        session = self._new_session(resp.get("type", "unknown"), session_id)
        self._sessions[session_id] = session
        return session

    def _new_session(self, target_type: str, session_id: str) -> "TargetSession":
        return TargetSession(
            self,
            target_type,
            session_id,
            flat_session=self._flatten_sessions,
            proto_def=self._proto_def,
        )


class TargetSession(CDPSession):
    def __init__(
        self,
        client: Union[Client, "TargetSession"],
        target_type: str,
        session_id: str,
        flat_session: bool = False,
        proto_def: Optional[Dict] = None,
    ) -> None:
        """Make new session."""
        super().__init__(client, target_type, session_id, flat_session)
        self._proto_def: Optional[Dict] = proto_def
        if proto_def is None:
            self.Accessibility: Accessibility = Accessibility(self)
            self.Animation: Animation = Animation(self)
            self.ApplicationCache: ApplicationCache = ApplicationCache(self)
            self.Audits: Audits = Audits(self)
            self.Browser: Browser = Browser(self)
            self.CacheStorage: CacheStorage = CacheStorage(self)
            self.Cast: Cast = Cast(self)
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

    def create_session(self, target_type: str, session_id: str) -> "TargetSession":
        """Creates a new session for the target being connected to specified
        by the session_id

        :param target_type: The type of the target being connected to
        :param session_id: The session id used to communicate to the target
        :return: A new session connected to the target
        """
        connection = self._connection if self._flat_session else self
        session = TargetSession(
            connection,
            target_type,
            session_id,
            flat_session=self._flat_session,
            proto_def=self._proto_def,
        )
        if self._flat_session:
            self._connection.add_session(session)
        else:
            self._sessions[session_id] = session
        return session
