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
from .console import Console
from .debugger import Debugger
from .heapprofiler import HeapProfiler
from .profiler import Profiler
from .runtime import Runtime
from .schema import Schema

__all__ = ["ProtocolMixin"]


class ProtocolMixin(object):
    def __init__(self, *args, **kwargs):
        super(ProtocolMixin, self).__init__(*args, **kwargs)
        self.Accessibility = Accessibility(self)
        self.Animation = Animation(self)
        self.ApplicationCache = ApplicationCache(self)
        self.Audits = Audits(self)
        self.Browser = Browser(self)
        self.CSS = CSS(self)
        self.CacheStorage = CacheStorage(self)
        self.DOM = DOM(self)
        self.DOMDebugger = DOMDebugger(self)
        self.DOMSnapshot = DOMSnapshot(self)
        self.DOMStorage = DOMStorage(self)
        self.Database = Database(self)
        self.DeviceOrientation = DeviceOrientation(self)
        self.Emulation = Emulation(self)
        self.HeadlessExperimental = HeadlessExperimental(self)
        self.IO = IO(self)
        self.IndexedDB = IndexedDB(self)
        self.Input = Input(self)
        self.Inspector = Inspector(self)
        self.LayerTree = LayerTree(self)
        self.Log = Log(self)
        self.Memory = Memory(self)
        self.Network = Network(self)
        self.Overlay = Overlay(self)
        self.Page = Page(self)
        self.Performance = Performance(self)
        self.Security = Security(self)
        self.ServiceWorker = ServiceWorker(self)
        self.Storage = Storage(self)
        self.SystemInfo = SystemInfo(self)
        self.Target = Target(self)
        self.Tethering = Tethering(self)
        self.Tracing = Tracing(self)
        self.Console = Console(self)
        self.Debugger = Debugger(self)
        self.HeapProfiler = HeapProfiler(self)
        self.Profiler = Profiler(self)
        self.Runtime = Runtime(self)
        self.Schema = Schema(self)
