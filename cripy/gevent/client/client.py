import gevent
from gevent import monkey as george; george.patch_all()
import ujson as json
from gevent.event import AsyncResult
from gevent.queue import UnboundQueue
import websocket
import requests
from urllib.parse import urljoin
from eventemitter import EventEmitter
from ..protocol import ProtocolMixin

__all__ = ["Client"]

DEFAULT_HOST: str = "localhost"
DEFAULT_PORT: int = 9222


def ensure_url(url, host, port, secure, suffix):
    """

    :param url: 
    :param host: 
    :param port: 
    :param secure: 
    :param suffix: 

    """
    if url is None:
        url = "{0}//{1}:{2}".format("https:" if secure else "http:", host, port)
    if not url.endswith(suffix):
        url = urljoin(url, suffix)
    return url


class Client(ProtocolMixin, EventEmitter):
    """ """

    def __init__(
        self,
        url=None,
        host=DEFAULT_HOST,
        port=DEFAULT_PORT,
        secure=None,
        wsurl=None,
        *args,
        **kwargs,
    ):
        super(Client, self).__init__(*args, **kwargs)
        self.connected = False
        self.ws = None
        self._ws_url = wsurl  # type: str
        self._host = host  # type: str
        self._port = port  # type: int
        self._url = self._make_url(url, secure)  # type: str
        self._message_id = 0  # type: int
        self._callbacks = dict()  # type: Dict[int, AsyncResult]
        self._recv_let = None  # type: gevent.Greenlet
        self._send_queue = UnboundQueue()  # type: UnboundQueue
        self._sendlet = None  # type: gevent.Greenlet

    def _make_url(self, url=None, secure=False):
        """
        :param url:  (Default value = None)
        :param secure:  (Default value = False)
        """
        if url is None:
            return "{0}//{1}:{2}".format(
                "https:" if secure else "http:", self._host, self._port
            )
        return url

    def connect(self):
        """ """
        if self._ws_url is None:
            tabs = self.List(self._url)
            found = list(filter(lambda x: x["type"] == "page", tabs))[0]
            self._ws_url = found["webSocketDebuggerUrl"]
        self.ws = websocket.create_connection(self._ws_url)
        self._recv_let = gevent.spawn(self._recv_loop)

    def send(self, method, params=None):
        """
        :param method:
        :param params:  (Default value = None)
        """
        if params is None:
            params = dict()
        self._message_id += 1
        _id = self._message_id
        cb = AsyncResult()
        self._callbacks[_id] = cb
        msg = json.dumps(dict(method=method, params=params, id=_id))
        self._send_async(msg)
        # self.ws.send(msg)
        return cb

    def _send_async(self, msg):
        """
        :param msg:
        """
        self._send_queue.put(msg, block=False)
        if self._sendlet is None or self._sendlet.ready():
            self._sendlet = gevent.spawn(self._send_worker)
        # gevent.spawn(self.ws.send, msg)

    def _send_worker(self):
        """ """
        for msg in self._send_queue:
            # self.ws.send(msg)
            gevent.spawn(self.ws.send, msg)
            gevent.idle()
            if self._send_queue.empty():
                break

    def _recv_loop(self):
        """ """
        self.connected = True
        while self.connected:
            rmsg = self.ws.recv()
            if rmsg:
                self._on_message(rmsg)

    def _on_message(self, rmsg):
        """
        :param rmsg:
        """
        msg = json.loads(rmsg)
        id = msg.get("id")
        if id is not None and id in self._callbacks:
            callback = self._callbacks.pop(id)  # type: AsyncResult
            if "error" in msg:
                callback.set_exception(Exception(msg["error"]))
            else:
                callback.set(msg["result"])
        else:
            params = msg.get("params", {})
            method = msg.get("method", "")
            if method in self.protocol_events:
                params = self.protocol_events[method].safe_create(params)
            try:
                self.emit(method, params)
                self.emit("*", (method, params))
            except Exception as e:
                print("emit execption", e)

    @classmethod
    def JSON(cls, url=None, host=DEFAULT_HOST, port=DEFAULT_PORT, secure=False):
        """

        :param url:  (Default value = None)
        :param host:  (Default value = DEFAULT_HOST)
        :param port:  (Default value = DEFAULT_PORT)
        :param secure:  (Default value = False)
        """
        url = ensure_url(url, host, port, secure, "/json")
        try:
            res = requests.get(url)
            return res.json()
        except Exception:
            return {}

    @classmethod
    def Activate(cls, id, url=None, host=DEFAULT_HOST, port=DEFAULT_PORT, secure=False):
        """

        :param id: 
        :param url:  (Default value = None)
        :param host:  (Default value = DEFAULT_HOST)
        :param port:  (Default value = DEFAULT_PORT)
        :param secure:  (Default value = False)
        """
        url = ensure_url(url, host, port, secure, "/json/activate")
        try:
            res = requests.get(urljoin(url, id))
            return res.json()
        except Exception:
            return {}

    @classmethod
    def List(cls, url=None, host=DEFAULT_HOST, port=DEFAULT_PORT, secure=False):
        """

        :param url:  (Default value = None)
        :param host:  (Default value = DEFAULT_HOST)
        :param port:  (Default value = DEFAULT_PORT)
        :param secure:  (Default value = False)

        """
        url = ensure_url(url, host, port, secure, "json/list")
        try:
            res = requests.get(url)
            return res.json()
        except Exception as E:
            return {}

    @classmethod
    def New(cls, url=None, host=DEFAULT_HOST, port=DEFAULT_PORT, secure=False):
        """

        :param url:  (Default value = None)
        :param host:  (Default value = DEFAULT_HOST)
        :param port:  (Default value = DEFAULT_PORT)
        :param secure:  (Default value = False)

        """
        url = ensure_url(url, host, port, secure, "/json/new")
        try:
            res = requests.get(url)
            return res.json()
        except Exception:
            return {}

    @classmethod
    def Protocol(cls, url=None, host=DEFAULT_HOST, port=DEFAULT_PORT, secure=False):
        """

        :param url:  (Default value = None)
        :param host:  (Default value = DEFAULT_HOST)
        :param port:  (Default value = DEFAULT_PORT)
        :param secure:  (Default value = False)

        """
        url = ensure_url(url, host, port, secure, "/json/protocol")
        try:
            res = requests.get(url)
            return res.json()
        except Exception:
            return {}

    @classmethod
    def Version(cls, url=None, host=DEFAULT_HOST, port=DEFAULT_PORT, secure=False):
        """

        :param url:  (Default value = None)
        :param host:  (Default value = DEFAULT_HOST)
        :param port:  (Default value = DEFAULT_PORT)
        :param secure:  (Default value = False)

        """
        url = ensure_url(url, host, port, secure, "/json/version")
        try:
            res = requests.get(url)
            return res.json()
        except Exception:
            return {}
