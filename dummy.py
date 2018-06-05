import asyncio
import aiohttp
from cripy.client.launcher import launch
from cripy.client import Client

wsurl = "ws://localhost:9222/devtools/page/16EC887194626130148B6660141B019D"


async def go():
    chrome = Client(wsurl=wsurl)
    print("connected?")
    await chrome.Page.enable()
    print("page enable")
    await chrome.Network.enable()
    print("network enable enable")
    await chrome.Page.navigate(url="https://www.reuters.com/")

    def print_on(event):
        print(event)
        print(event.__dict__)

    chrome.on("Network.requestWillBeSent", print_on)
    chrome.on("Network.responseReceived", print_on)


async def err():
    async with aiohttp.ClientSession() as session:
        try:
            data = await session.get("http://localhost:9000")
        except Exception as e:
            print(e)
            print(type(e))


async def test_launch():
    res = await Client.JSON()
    for it in res:
        print(it)


def main():
    loop = asyncio.get_event_loop()  # event loop
    loop.run_until_complete(test_launch())


if __name__ == "__main__":
    class It(object):
        def __init__(self):
            self.i = 0

        def __getitem__(self, k):
            return self.__dict__[k]

        def get(self, what, default=None):
            return self.__dict__.get(what, default)
    it = It()
    print(it.get('i'))