import asyncio
import aiohttp
from cripy.chrome import Chrome
from cripy.chrome.launcher import launch


async def go():
    chrome = Chrome()
    await chrome.connect()
    print('connected?')
    await chrome.Page.enable()
    await chrome.Network.enable()
    await chrome.Page.navigate(url='https://www.reuters.com/')
    def print_on(event):
        print(event)
        print(event.__dict__)
    chrome.on('Network.requestWillBeSent', print_on)
    chrome.on('Network.responseReceived', print_on)


async def err():
    async with aiohttp.ClientSession() as session:
        try:
            data = await session.get('http://localhost:9000')
        except Exception as e:
            print(e)
            print(type(e))


async def test_launch():
    chrome = await launch(executablePath='google-chrome-unstable', headless=False)
    await asyncio.sleep(10)
    await chrome.close()


def main():
    loop = asyncio.get_event_loop()  # event loop
    future = asyncio.ensure_future(test_launch())  # tasks to do
    loop.run_until_complete(future)


if __name__ == "__main__":
    main()
