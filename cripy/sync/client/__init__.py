import json

import websocket

from cripy.sync.client.event_emitter import EventEmitter
from cripy.sync.protocol import ProtocolMixin


class Client(ProtocolMixin, EventEmitter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.browser_running = False
        self.ws = None
        self._message_id = 0
        self._callbacks = dict()

    def connect(self):
        self.ws = websocket.create_connection(self.tab_data["webSocketDebuggerUrl"])

    def send(self, method, params=None, cb=None):
        if params is None:
            params = dict()
        self._message_id += 1
        _id = self._message_id
        if cb is not None:
            self._callbacks[_id] = cb
        self.ws.send(method, json.dumps(params))

    def _recv_loop(self):
        while self.browser_running:
            rmsg = self.ws.recv()
            if rmsg:
                self._on_message(rmsg)

    def _on_message(self, rmsg):
        msg = json.loads(rmsg)
        id = msg.get("id")
        if id is not None and id in self._callbacks:
            callback = self._callbacks.pop(id)
            callback(msg)
        else:
            self._on_unsolicited(msg)

    def _on_unsolicited(self, msg):
        pass
