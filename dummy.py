from gevent import monkey as george

george.patch_all()

import gevent
import signal

from cripy.gevent.client import Client


def signal_shutdown(*args, **kwargs):
    raise KeyboardInterrupt


def star_msg(msg):
    print(msg)


def run():
    c = Client()
    c.on("*", star_msg)
    c.connect()
    res = c.Page.getFrameTree()
    print(res)
    # print(c.Page.enable())
    # print(c.Network.enable())
    # print(c.Runtime.enable())
    # print(c.DOM.enable())
    # print(c.Log.enable())
    # print(c.Page.setLifecycleEventsEnabled(enabled=True))
    # c.Page.navigate(url="https://google.com")


def main():
    gevent.signal(signal.SIGQUIT, signal_shutdown)
    gevent.signal(signal.SIGINT, signal_shutdown)
    gevent.signal(signal.SIGTERM, signal_shutdown)
    greenlet = gevent.spawn(run)
    greenlet.join()
    forever = gevent.event.Event()
    try:
        forever.wait()
    except KeyboardInterrupt:
        print("done")
        gevent.kill(greenlet)


if __name__ == "__main__":
    main()
    # with open("protocol.json", "w") as out:
    #     proto = Client.Protocol()
    #     print(proto)
    #     import ujson
    #     out.write(ujson.dumps(proto))
