import asyncio
from websockets import client
import logging
import sys
import ujson as json
from typing import Awaitable, Optional

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

WS_URL = "ws://localhost:9222/devtools/page/61FD92ECB83E8BA0E07282BAC9580069"


class DebugWS(object):
    def __init__(self, wsurl: str) -> None:
        self.wsurl = wsurl
        self.ws: Optional = None
        self._recv_task: Optional = None
        self._id = 0

    async def connect(self):
        self.ws = client.connect(
            self.wsurl, max_size=None, compression=None, max_queue=0, timeout=20
        )
        print("connected")
        await self.ws.ensure_open()
        self._recv_task = asyncio.ensure_future(self.recv())

    def next_id(self):
        last_id = self._id
        self._id += 1
        return last_id

    async def send_test(self):
        msg = json.dumps(
            dict(id=self.next_id(), method="Runtime.enable", params={}),
            ensure_ascii=False,
        )
        await self.ws.send(msg)
        msg = json.dumps(
            dict(id=self.next_id(), method="Page.enable", params={}), ensure_ascii=False
        )
        await self.ws.send(msg)
        msg = json.dumps(
            dict(id=self.next_id(), method="Network.enable", params={}),
            ensure_ascii=False,
        )
        await self.ws.send(msg)
        msg = json.dumps(
            dict(
                id=self.next_id(),
                method="Page.setLifecycleEventsEnabled",
                params=dict(enabled=True),
            ),
            ensure_ascii=False,
        )
        await self.ws.send(msg)

    async def recv(self):
        print("starting recv loop")
        while True:
            msg = await self.ws.recv()
            print("Got message", msg)


async def do_it() -> None:
    dws = DebugWS(wsurl=WS_URL)
    await dws.connect()
    await dws.send_test()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(do_it())
    loop.run_forever()
    # msg  = json.dumps(dict(id=1, method='Page.enable', params={}), ensure_ascii=False)
    # print(type(msg))
    # print(json.dumps({"id":1, "method": "Page.enable", "params":{}}, ensure_ascii=False))
