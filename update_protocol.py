import asyncio
from aiohttp import ClientSession
from typing import List, Tuple
import pathlib
from cripy import CDP
from ujson import dumps

try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass


async def fetch(url: str, session: ClientSession) -> Tuple[str, bytes]:
    """Fetch a url, using specified ClientSession."""
    async with session.get(url) as response:
        resp = await response.read()
        return url, resp


async def fetch_all(urls: List[str]) -> None:
    """Launch requests for all web pages."""
    tasks = []
    async with ClientSession() as session:
        for url in urls:
            task = asyncio.ensure_future(fetch(url, session))
            tasks.append(task)  # create list of tasks
        done = await asyncio.gather(*tasks)
        dp = pathlib.Path("data")
        for url, res in done:
            fp = dp.joinpath(url[url.find("json") + 5 :])
            with fp.open("w") as out:
                out.write(res.decode("utf-8"))


async def get_proto_from_browser() -> None:
    proto = await CDP.Protocol(loop=asyncio.get_event_loop())
    with open('./data/protocol.json', 'w') as out:
        out.write(dumps(proto))
    print(proto)

if __name__ == "__main__":
    # urls = [
    #     "https://raw.githubusercontent.com/ChromeDevTools/devtools-protocol/master/json/browser_protocol.json",
    #     "https://raw.githubusercontent.com/ChromeDevTools/devtools-protocol/master/json/js_protocol.json",
    # ]
    loop = asyncio.get_event_loop()  # event loop
    loop.run_until_complete(get_proto_from_browser())
