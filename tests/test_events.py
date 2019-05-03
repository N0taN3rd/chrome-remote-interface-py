from asyncio import AbstractEventLoop

import pytest

from cripy.cdp import connect, CDP
from cripy.client import Client
from .helpers import Cleaner


@pytest.mark.usefixtures("chrome")
class TestEventsLocal:
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
    async def test_event_on_cb_removable(
        self, mr_clean: Cleaner, event_loop: AbstractEventLoop
    ):
        future = event_loop.create_future()
        client: Client = await connect(url=self.wsurl)
        mr_clean.add_disposable(client)

        def listener(x):
            if not future.done():
                future.set_result(x)

        remove = client.Network.requestWillBeSent(listener)
        assert remove is not None and callable(remove)
        await client.Network.enable()
        await client.Page.navigate("https://google.com")
        assert await future is not None
        remove()
        assert len(client.listeners("Network.requestWillBeSent")) == 0

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
class TestEventsRemote:
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
    async def test_event_on_cb_removable(
        self, mr_clean: Cleaner, event_loop: AbstractEventLoop
    ):
        future = event_loop.create_future()
        client = await connect(url=self.wsurl, remote=True)
        mr_clean.add_disposable(client)

        def listener(x):
            if not future.done():
                future.set_result(x)

        remove = client.Network.requestWillBeSent(listener)
        assert remove is not None and callable(remove)
        await client.Network.enable()
        await client.Page.navigate("https://google.com")
        assert await future is not None
        remove()
        assert len(client.listeners("Network.requestWillBeSent")) == 0

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


@pytest.mark.usefixtures("chrome")
class TestEventsSuppliedProto:
    @pytest.mark.asyncio
    async def test_event_client_on_cb(
        self, mr_clean: Cleaner, event_loop: AbstractEventLoop
    ):
        future = event_loop.create_future()
        client = await connect(
            url=self.wsurl, protocol=await CDP.Protocol(loop=event_loop)
        )
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
        client = await connect(
            url=self.wsurl, protocol=await CDP.Protocol(loop=event_loop)
        )
        mr_clean.add_disposable(client)

        def listener(x):
            if not future.done():
                future.set_result(x)

        client.Network.requestWillBeSent(listener)

        await client.Network.enable()
        await client.Page.navigate("https://google.com")
        assert await future is not None

    @pytest.mark.asyncio
    async def test_event_on_cb_removable(
        self, mr_clean: Cleaner, event_loop: AbstractEventLoop
    ):
        future = event_loop.create_future()
        client: Client = await connect(
            url=self.wsurl, protocol=await CDP.Protocol(loop=event_loop)
        )
        mr_clean.add_disposable(client)

        def listener(x):
            if not future.done():
                future.set_result(x)

        remove = client.Network.requestWillBeSent(listener)
        assert remove is not None and callable(remove)
        await client.Network.enable()
        await client.Page.navigate("https://google.com")
        assert await future is not None
        remove()
        assert len(client.listeners("Network.requestWillBeSent")) == 0

    @pytest.mark.asyncio
    async def test_event_client_once_cb(
        self, mr_clean: Cleaner, event_loop: AbstractEventLoop
    ):
        future = event_loop.create_future()
        client = await connect(
            url=self.wsurl, protocol=await CDP.Protocol(loop=event_loop)
        )
        mr_clean.add_disposable(client)
        client.once("Network.requestWillBeSent", lambda x: future.set_result(x))
        await client.Network.enable()
        await client.Page.navigate("https://google.com")
        assert await future is not None

    @pytest.mark.asyncio
    async def test_event_once_promise(
        self, mr_clean: Cleaner, event_loop: AbstractEventLoop
    ):
        client = await connect(
            url=self.wsurl, protocol=await CDP.Protocol(loop=event_loop)
        )
        mr_clean.add_disposable(client)
        await client.Network.enable()
        await client.Page.navigate("https://google.com")
        assert await client.Network.requestWillBeSent() is not None
