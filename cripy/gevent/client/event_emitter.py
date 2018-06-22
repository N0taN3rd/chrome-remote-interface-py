from collections import defaultdict, OrderedDict

__all__ = ["EventEmitter"]


class EventEmitter(object):

    def __init__(self):
        self._events = defaultdict(OrderedDict)

    def on(self, event, f):
        self._add_event_handler(event, f, f)

    def once(self, event, f):
        myself = self

        def _wrapper(f):

            def g(*args, **kwargs):
                myself.remove_listener(event, f)
                return f(*args, **kwargs)

            myself._add_event_handler(event, f, g)
            return f

        return _wrapper(f)

    def emit(self, event, *args, **kwargs):
        handled = False
        for f in list(self._events[event].values()):
            try:
                result = f(*args, **kwargs)
            except Exception:
                pass
            handled = True
        return handled

    def remove_listener(self, event, f):
        self._events[event].pop(f)

    def remove_all_listeners(self, event=None):
        if event is not None:
            self._events[event] = OrderedDict()
        else:
            self._events = defaultdict(OrderedDict)

    def listeners(self, event):
        return list(self._events[event].keys())

    def _add_event_handler(self, event, k, v):
        self._events[event][k] = v
