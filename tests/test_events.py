from asyncio import AbstractEventLoop

import pytest

from cripy.client import connect
from .helpers import Cleaner


@pytest.mark.usefixtures("chrome")
class TestEventsLocal(object):
    @pytest.mark.asyncio
    async def test_event_client_on_cb(
        self, mr_clean: Cleaner, event_loop: AbstractEventLoop
    ):
        future = event_loop.create_future()
        client = await connect(url=self.wsurl)
        mr_clean.add_disposable(client)

        def listener(x):
            if not future.done():
                future.set_result(x)

        client.on("Network.requestWillBeSent", listener)

        await client.Network.enable()
        await client.Page.navigate("https://google.com")
        assert await future is not None

    @pytest.mark.asyncio
    async def test_event_on_cb(self, mr_clean: Cleaner, event_loop: AbstractEventLoop):
        future = event_loop.create_future()
        client = await connect(url=self.wsurl)
        mr_clean.add_disposable(client)

        def listener(x):
            if not future.done():
                future.set_result(x)

        client.Network.requestWillBeSent(listener)

        await client.Network.enable()
        await client.Page.navigate("https://google.com")
        assert await future is not None

    @pytest.mark.asyncio
    async def test_event_client_once_cb(
        self, mr_clean: Cleaner, event_loop: AbstractEventLoop
    ):
        future = event_loop.create_future()
        client = await connect(url=self.wsurl)
        mr_clean.add_disposable(client)
        client.once("Network.requestWillBeSent", lambda x: future.set_result(x))
        await client.Network.enable()
        await client.Page.navigate("https://google.com")
        assert await future is not None

    @pytest.mark.asyncio
    async def test_event_once_promise(self, mr_clean: Cleaner):
        client = await connect(url=self.wsurl)
        mr_clean.add_disposable(client)
        await client.Network.enable()
        await client.Page.navigate("https://google.com")
        assert await client.Network.requestWillBeSent() is not None


@pytest.mark.usefixtures("chrome")
class TestEventsRemote(object):
    @pytest.mark.asyncio
    async def test_event_client_on_cb(
        self, mr_clean: Cleaner, event_loop: AbstractEventLoop
    ):
        future = event_loop.create_future()
        client = await connect(url=self.wsurl, remote=True)
        mr_clean.add_disposable(client)

        def listener(x):
            if not future.done():
                future.set_result(x)

        client.on("Network.requestWillBeSent", listener)

        await client.Network.enable()
        await client.Page.navigate("https://google.com")
        assert await future is not None

    @pytest.mark.asyncio
    async def test_event_on_cb(self, mr_clean: Cleaner, event_loop: AbstractEventLoop):
        future = event_loop.create_future()
        client = await connect(url=self.wsurl, remote=True)
        mr_clean.add_disposable(client)

        def listener(x):
            if not future.done():
                future.set_result(x)

        client.Network.requestWillBeSent(listener)

        await client.Network.enable()
        await client.Page.navigate("https://google.com")
        assert await future is not None

    @pytest.mark.asyncio
    async def test_event_client_once_cb(
        self, mr_clean: Cleaner, event_loop: AbstractEventLoop
    ):
        future = event_loop.create_future()
        client = await connect(url=self.wsurl, remote=True)
        mr_clean.add_disposable(client)
        client.once("Network.requestWillBeSent", lambda x: future.set_result(x))
        await client.Network.enable()
        await client.Page.navigate("https://google.com")
        assert await future is not None

    @pytest.mark.asyncio
    async def test_event_once_promise(self, mr_clean: Cleaner):
        client = await connect(url=self.wsurl, remote=True)
        mr_clean.add_disposable(client)
        await client.Network.enable()
        await client.Page.navigate("https://google.com")
        assert await client.Network.requestWillBeSent() is not None
