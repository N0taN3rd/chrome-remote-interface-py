# noinspection PyPep8
# noinspection PyArgumentList

from .console import Console
from .debugger import Debugger
from .heapprofiler import HeapProfiler
from .profiler import Profiler
from .runtime import Runtime
from .schema import Schema
from .accessibility import Accessibility
from .animation import Animation
from .applicationcache import ApplicationCache
from .audits import Audits
from .browser import Browser
from .css import CSS
from .cachestorage import CacheStorage
from .dom import DOM
from .domdebugger import DOMDebugger
from .domsnapshot import DOMSnapshot
from .domstorage import DOMStorage
from .database import Database
from .deviceorientation import DeviceOrientation
from .emulation import Emulation
from .headlessexperimental import HeadlessExperimental
from .io import IO
from .indexeddb import IndexedDB
from .input import Input
from .inspector import Inspector
from .layertree import LayerTree
from .log import Log
from .memory import Memory
from .network import Network
from .overlay import Overlay
from .page import Page
from .performance import Performance
from .security import Security
from .serviceworker import ServiceWorker
from .storage import Storage
from .systeminfo import SystemInfo
from .target import Target
from .tethering import Tethering
from .tracing import Tracing


class ProtocolMixin(object):

    def __init__(self):
        self.Console: Console = Console
        self.Debugger: Debugger = Debugger
        self.HeapProfiler: HeapProfiler = HeapProfiler
        self.Profiler: Profiler = Profiler
        self.Runtime: Runtime = Runtime
        self.Schema: Schema = Schema
        self.Accessibility: Accessibility = Accessibility
        self.Animation: Animation = Animation
        self.ApplicationCache: ApplicationCache = ApplicationCache
        self.Audits: Audits = Audits
        self.Browser: Browser = Browser
        self.CSS: CSS = CSS
        self.CacheStorage: CacheStorage = CacheStorage
        self.DOM: DOM = DOM
        self.DOMDebugger: DOMDebugger = DOMDebugger
        self.DOMSnapshot: DOMSnapshot = DOMSnapshot
        self.DOMStorage: DOMStorage = DOMStorage
        self.Database: Database = Database
        self.DeviceOrientation: DeviceOrientation = DeviceOrientation
        self.Emulation: Emulation = Emulation
        self.HeadlessExperimental: HeadlessExperimental = HeadlessExperimental
        self.IO: IO = IO
        self.IndexedDB: IndexedDB = IndexedDB
        self.Input: Input = Input
        self.Inspector: Inspector = Inspector
        self.LayerTree: LayerTree = LayerTree
        self.Log: Log = Log
        self.Memory: Memory = Memory
        self.Network: Network = Network
        self.Overlay: Overlay = Overlay
        self.Page: Page = Page
        self.Performance: Performance = Performance
        self.Security: Security = Security
        self.ServiceWorker: ServiceWorker = ServiceWorker
        self.Storage: Storage = Storage
        self.SystemInfo: SystemInfo = SystemInfo
        self.Target: Target = Target
        self.Tethering: Tethering = Tethering
        self.Tracing: Tracing = Tracing
