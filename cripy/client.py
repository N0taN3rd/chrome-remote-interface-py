from asyncio import AbstractEventLoop
from typing import Dict, Optional, Union

from .connection import Connection
from .protocol import (
    Accessibility,
    Animation,
    ApplicationCache,
    Audits,
    Browser,
    BackgroundService,
    CacheStorage,
    Cast,
    Console,
    CSS,
    Database,
    Debugger,
    DeviceOrientation,
    DOM,
    DOMDebugger,
    DOMSnapshot,
    DOMStorage,
    Emulation,
    Fetch,
    HeadlessExperimental,
    HeapProfiler,
    IndexedDB,
    Input,
    Inspector,
    IO,
    LayerTree,
    Log,
    Memory,
    Network,
    Overlay,
    Page,
    Performance,
    Profiler,
    Runtime,
    Schema,
    Security,
    ServiceWorker,
    Storage,
    SystemInfo,
    Target,
    Tethering,
    Tracing,
    WebAudio,
)

from .target_session import TargetSession, TargetSessionDynamic

__all__ = ["Client", "ClientDynamic"]


class Client(Connection):
    __slots__ = [
        "Accessibility",
        "Animation",
        "ApplicationCache",
        "Audits",
        "BackgroundService",
        "Browser",
        "CSS",
        "CacheStorage",
        "Cast",
        "Console",
        "DOM",
        "DOMDebugger",
        "DOMSnapshot",
        "DOMStorage",
        "Database",
        "Debugger",
        "DeviceOrientation",
        "Emulation",
        "Fetch",
        "HeadlessExperimental",
        "HeapProfiler",
        "IO",
        "IndexedDB",
        "Input",
        "Inspector",
        "LayerTree",
        "Log",
        "Memory",
        "Network",
        "Overlay",
        "Page",
        "Performance",
        "Profiler",
        "Runtime",
        "Schema",
        "Security",
        "ServiceWorker",
        "Storage",
        "SystemInfo",
        "Target",
        "Tethering",
        "Tracing",
        "WebAudio",
    ]

    def __init__(
        self,
        ws_url: Optional[str] = None,
        flatten_sessions: bool = False,
        loop: Optional[AbstractEventLoop] = None,
    ) -> None:
        """Construct a new instance of the ChromeRemoteInterface Client.

        :param ws_url: The WS endpoint of the remote instance
        :param flatten_sessions: Enables "flat" access to the session via specifying sessionId
        attribute in the commands
        :param loop:  Optional event loop to use. Defaults to asyncio.get_event_loop
        """
        super().__init__(ws_url, flatten_sessions, loop)
        self.Accessibility: Accessibility = Accessibility(self)
        self.Animation: Animation = Animation(self)
        self.ApplicationCache: ApplicationCache = ApplicationCache(self)
        self.Audits: Audits = Audits(self)
        self.Browser: Browser = Browser(self)
        self.BackgroundService: BackgroundService = BackgroundService(self)
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
        self.Tethering: Tethering = Tethering(self)
        self.Tracing: Tracing = Tracing(self)
        self.WebAudio: WebAudio = WebAudio(self)

    def session(self, session_id: str) -> Optional["TargetSession"]:
        """Returns the TargetSession associated with the supplied session id
        if it exists

        :param session_id: The id of the session
        :return: The TargetSession instance associated with the supplied id if it exists
        """
        return self._sessions.get(session_id)

    async def create_session(self, target_id: str) -> "TargetSession":
        """Attach to the target specified by the supplied target id and creates new CDPSession for
        direct communication to it

        :param target_id: The id of the target connecting to
        :return: A new session connected to the target
        """
        params: Dict[str, Union[str, bool]] = {"targetId": target_id}
        if self._flatten_sessions:
            params["flatten"] = self._flatten_sessions
        resp = await self.send("Target.attachToTarget", params)
        session_id = resp.get("sessionId")
        if self._flatten_sessions:
            session: TargetSession = self._sessions.get(session_id)
            if session:
                return session
        session = self._new_session(resp.get("type", "unknown"), session_id)
        self._sessions[session_id] = session
        return session

    def _new_session(self, target_type: str, session_id: str) -> "TargetSession":
        """Create a new session for the supplied target

        :param target_type: The type of the target
        :param session_id: The session id for the target
        :return: A TargetSession connected to the target
        """
        return TargetSession(
            self, target_type, session_id, flat_session=self._flatten_sessions
        )


class ClientDynamic(Connection):
    def __init__(
        self,
        ws_url: Optional[str] = None,
        flatten_sessions: bool = False,
        proto_def: Dict = None,
        loop: Optional[AbstractEventLoop] = None,
    ) -> None:
        """Construct a new instance of ClientDynamic.

        :param ws_url: The WS endpoint of the remote instance
        :param flatten_sessions: Enables "flat" access to the session via specifying sessionId
        attribute in the commands
        :param proto_def: Optional protocol domain classes to be used rather than
        the pre-generated ones
        :param loop:  Optional event loop to use. Defaults to asyncio.get_event_loop
        """
        super().__init__(ws_url, flatten_sessions, loop)
        self._proto_def: Dict = proto_def
        for domain, clazz in proto_def.items():
            setattr(self, domain, clazz(self))

    def session(self, session_id: str) -> Optional["TargetSessionDynamic"]:
        """Returns the TargetSession associated with the supplied session id
        if it exists

        :param session_id: The id of the session
        :return: The TargetSession instance associated with the supplied id if it exists
        """
        return self._sessions.get(session_id)

    async def create_session(self, target_id: str) -> "TargetSessionDynamic":
        """Attach to the target specified by the supplied target id and creates new CDPSession for
        direct communication to it

        :param target_id: The id of the target connecting to
        :return: A new session connected to the target
        """
        params: Dict[str, Union[str, bool]] = {"targetId": target_id}
        if self._flatten_sessions:
            params["flatten"] = self._flatten_sessions
        resp = await self.send("Target.attachToTarget", params)
        session_id = resp.get("sessionId")
        if self._flatten_sessions:
            session: TargetSessionDynamic = self._sessions.get(session_id)
            if session:
                return session
        session = self._new_session(resp.get("type", "unknown"), session_id)
        self._sessions[session_id] = session
        return session

    def _new_session(self, target_type: str, session_id: str) -> "TargetSessionDynamic":
        """Create a new session for the supplied target

        :param target_type: The type of the target
        :param session_id: The session id for the target
        :return: A TargetSession connected to the target
        """
        return TargetSessionDynamic(
            self,
            target_type,
            session_id,
            flat_session=self._flatten_sessions,
            proto_def=self._proto_def,
        )
