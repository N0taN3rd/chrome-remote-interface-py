from cripy.gevent.protocol.console import Console
from cripy.gevent.protocol.debugger import Debugger
from cripy.gevent.protocol.heapprofiler import HeapProfiler
from cripy.gevent.protocol.profiler import Profiler
from cripy.gevent.protocol.runtime import Runtime
from cripy.gevent.protocol.schema import Schema
from cripy.gevent.protocol.accessibility import Accessibility
from cripy.gevent.protocol.animation import Animation
from cripy.gevent.protocol.applicationcache import ApplicationCache
from cripy.gevent.protocol.audits import Audits
from cripy.gevent.protocol.browser import Browser
from cripy.gevent.protocol.css import CSS
from cripy.gevent.protocol.cachestorage import CacheStorage
from cripy.gevent.protocol.dom import DOM
from cripy.gevent.protocol.domdebugger import DOMDebugger
from cripy.gevent.protocol.domsnapshot import DOMSnapshot
from cripy.gevent.protocol.domstorage import DOMStorage
from cripy.gevent.protocol.database import Database
from cripy.gevent.protocol.deviceorientation import DeviceOrientation
from cripy.gevent.protocol.emulation import Emulation
from cripy.gevent.protocol.headlessexperimental import HeadlessExperimental
from cripy.gevent.protocol.io import IO
from cripy.gevent.protocol.indexeddb import IndexedDB
from cripy.gevent.protocol.input import Input
from cripy.gevent.protocol.inspector import Inspector
from cripy.gevent.protocol.layertree import LayerTree
from cripy.gevent.protocol.log import Log
from cripy.gevent.protocol.memory import Memory
from cripy.gevent.protocol.network import Network
from cripy.gevent.protocol.overlay import Overlay
from cripy.gevent.protocol.page import Page
from cripy.gevent.protocol.performance import Performance
from cripy.gevent.protocol.security import Security
from cripy.gevent.protocol.serviceworker import ServiceWorker
from cripy.gevent.protocol.storage import Storage
from cripy.gevent.protocol.systeminfo import SystemInfo
from cripy.gevent.protocol.target import Target
from cripy.gevent.protocol.tethering import Tethering
from cripy.gevent.protocol.tracing import Tracing

__all__ = [ "ProtocolMixin" ]


class ProtocolMixin(object):
    def __init__(self, *args, **kwargs):
        super(ProtocolMixin, self).__init__(*args, **kwargs)
        self.protocol_events = dict()
        self.Console: Console = Console(self)
        self._update_protocol_events(self.Console.get_event_classes())
        self.Debugger: Debugger = Debugger(self)
        self._update_protocol_events(self.Debugger.get_event_classes())
        self.HeapProfiler: HeapProfiler = HeapProfiler(self)
        self._update_protocol_events(self.HeapProfiler.get_event_classes())
        self.Profiler: Profiler = Profiler(self)
        self._update_protocol_events(self.Profiler.get_event_classes())
        self.Runtime: Runtime = Runtime(self)
        self._update_protocol_events(self.Runtime.get_event_classes())
        self.Schema: Schema = Schema(self)
        self._update_protocol_events(self.Schema.get_event_classes())
        self.Accessibility: Accessibility = Accessibility(self)
        self._update_protocol_events(self.Accessibility.get_event_classes())
        self.Animation: Animation = Animation(self)
        self._update_protocol_events(self.Animation.get_event_classes())
        self.ApplicationCache: ApplicationCache = ApplicationCache(self)
        self._update_protocol_events(self.ApplicationCache.get_event_classes())
        self.Audits: Audits = Audits(self)
        self._update_protocol_events(self.Audits.get_event_classes())
        self.Browser: Browser = Browser(self)
        self._update_protocol_events(self.Browser.get_event_classes())
        self.CSS: CSS = CSS(self)
        self._update_protocol_events(self.CSS.get_event_classes())
        self.CacheStorage: CacheStorage = CacheStorage(self)
        self._update_protocol_events(self.CacheStorage.get_event_classes())
        self.DOM: DOM = DOM(self)
        self._update_protocol_events(self.DOM.get_event_classes())
        self.DOMDebugger: DOMDebugger = DOMDebugger(self)
        self._update_protocol_events(self.DOMDebugger.get_event_classes())
        self.DOMSnapshot: DOMSnapshot = DOMSnapshot(self)
        self._update_protocol_events(self.DOMSnapshot.get_event_classes())
        self.DOMStorage: DOMStorage = DOMStorage(self)
        self._update_protocol_events(self.DOMStorage.get_event_classes())
        self.Database: Database = Database(self)
        self._update_protocol_events(self.Database.get_event_classes())
        self.DeviceOrientation: DeviceOrientation = DeviceOrientation(self)
        self._update_protocol_events(self.DeviceOrientation.get_event_classes())
        self.Emulation: Emulation = Emulation(self)
        self._update_protocol_events(self.Emulation.get_event_classes())
        self.HeadlessExperimental: HeadlessExperimental = HeadlessExperimental(self)
        self._update_protocol_events(self.HeadlessExperimental.get_event_classes())
        self.IO: IO = IO(self)
        self._update_protocol_events(self.IO.get_event_classes())
        self.IndexedDB: IndexedDB = IndexedDB(self)
        self._update_protocol_events(self.IndexedDB.get_event_classes())
        self.Input: Input = Input(self)
        self._update_protocol_events(self.Input.get_event_classes())
        self.Inspector: Inspector = Inspector(self)
        self._update_protocol_events(self.Inspector.get_event_classes())
        self.LayerTree: LayerTree = LayerTree(self)
        self._update_protocol_events(self.LayerTree.get_event_classes())
        self.Log: Log = Log(self)
        self._update_protocol_events(self.Log.get_event_classes())
        self.Memory: Memory = Memory(self)
        self._update_protocol_events(self.Memory.get_event_classes())
        self.Network: Network = Network(self)
        self._update_protocol_events(self.Network.get_event_classes())
        self.Overlay: Overlay = Overlay(self)
        self._update_protocol_events(self.Overlay.get_event_classes())
        self.Page: Page = Page(self)
        self._update_protocol_events(self.Page.get_event_classes())
        self.Performance: Performance = Performance(self)
        self._update_protocol_events(self.Performance.get_event_classes())
        self.Security: Security = Security(self)
        self._update_protocol_events(self.Security.get_event_classes())
        self.ServiceWorker: ServiceWorker = ServiceWorker(self)
        self._update_protocol_events(self.ServiceWorker.get_event_classes())
        self.Storage: Storage = Storage(self)
        self._update_protocol_events(self.Storage.get_event_classes())
        self.SystemInfo: SystemInfo = SystemInfo(self)
        self._update_protocol_events(self.SystemInfo.get_event_classes())
        self.Target: Target = Target(self)
        self._update_protocol_events(self.Target.get_event_classes())
        self.Tethering: Tethering = Tethering(self)
        self._update_protocol_events(self.Tethering.get_event_classes())
        self.Tracing: Tracing = Tracing(self)
        self._update_protocol_events(self.Tracing.get_event_classes())

    def _update_protocol_events(self, events):
        if events is not None:
            self.protocol_events.update(events)
