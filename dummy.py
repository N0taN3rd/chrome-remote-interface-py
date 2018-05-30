import asyncio
from cripy.chrome import Chrome


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


def main():
    loop = asyncio.get_event_loop()  # event loop
    future = asyncio.ensure_future(go())  # tasks to do
    asyncio.async(future)
    loop.run_forever()


if __name__ == "__main__":
    # main()
    def it(a):
        print(a)
    it(a=1)
    it(**{"a":2})