import asyncio
import uvloop
from cripy.asyncio.client import Client
import ujson as json
# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


def on_life(event):
    print(event)


async def run() -> None:
    client = await Client.connect_to_remote()
    client.Page.lifecycleEvent(on_life)
    await client.Page.enable()
    await client.Page.setLifecycleEventsEnabled(enabled=True)
    await client.Page.navigate('https://www.reuters.com/')
    await asyncio.sleep(15)
    await client.Browser.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
