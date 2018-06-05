import asyncio
import aiohttp
import logging
import sys
from cripy.chrome.launcher import launch

wsurl = "ws://localhost:9222/devtools/page/16EC887194626130148B6660141B019D"


def print_Req(r):
    print(r.preq)


def print_Res(r):
    print(r.pres)


async def tlaunch():
    browser = await launch(executablePath="google-chrome-beta", headless=False)
    browser.on('disconnected', lambda x: print('disconnected'))
    page = await browser.newPage()
    await page.goto("https://www.example.com/", dict(waitUntil="load"))
    await page.screenshot({"path": "example.png"})
    await browser.close()


def main():
    loop = asyncio.get_event_loop()  # event loop
    loop.run_until_complete(tlaunch())
    # loop.run_forever()


if __name__ == "__main__":
    main()
