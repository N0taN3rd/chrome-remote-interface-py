from typing import Dict, TYPE_CHECKING, Union

from .connection import CDPSession
from .protocol import (
    Accessibility,
    Animation,
    ApplicationCache,
    Audits,
    BackgroundService,
    Browser,
    CSS,
    CacheStorage,
    Cast,
    Console,
    DOM,
    DOMDebugger,
    DOMSnapshot,
    DOMStorage,
    Database,
    Debugger,
    DeviceOrientation,
    Emulation,
    Fetch,
    HeadlessExperimental,
    HeapProfiler,
    IO,
    IndexedDB,
    Input,
    Inspector,
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

if TYPE_CHECKING:
    from .client import Client, ClientDynamic

__all__ = ["TargetSession", "TargetSessionDynamic"]


class TargetSession(CDPSession):
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
        client: Union["Client", "TargetSession"],
        target_type: str,
        session_id: str,
        flat_session: bool = False,
    ) -> None:
        """Creat a new TargetSession

        :param client: The client or connection to be used
        :param target_type: The type of the target
        :param session_id: The session id for communication with the target
        :param flat_session: Is flat session mode enabled
        """
        super().__init__(client, target_type, session_id, flat_session)
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

    def create_session(self, target_type: str, session_id: str) -> "TargetSession":
        """Creates a new session for the target being connected to specified
        by the session_id

        :param target_type: The type of the target being connected to
        :param session_id: The session id used to communicate to the target
        :return: A new session connected to the target
        """
        connection = self._connection if self._flat_session else self
        session = TargetSession(
            connection, target_type, session_id, flat_session=self._flat_session
        )
        if self._flat_session:
            self._connection.add_session(session)
        else:
            self._sessions[session_id] = session
        return session


class TargetSessionDynamic(CDPSession):
    def __init__(
        self,
        client: Union["ClientDynamic", "TargetSessionDynamic"],
        target_type: str,
        session_id: str,
        flat_session: bool = False,
        proto_def: Dict = None,
    ) -> None:
        """Creat a new TargetSession

        :param client: The client or connection to be used
        :param target_type: The type of the target
        :param session_id: The session id for communication with the target
        :param flat_session: Is flat session mode enabled
        :param proto_def: The CDP protocol definition
        """
        super().__init__(client, target_type, session_id, flat_session)
        self._proto_def: Dict = proto_def
        for domain, clazz in proto_def.items():
            setattr(self, domain, clazz(self))

    def create_session(
        self, target_type: str, session_id: str
    ) -> "TargetSessionDynamic":
        """Creates a new session for the target being connected to specified
        by the session_id

        :param target_type: The type of the target being connected to
        :param session_id: The session id used to communicate to the target
        :return: A new session connected to the target
        """
        connection = self._connection if self._flat_session else self
        session = TargetSessionDynamic(
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
