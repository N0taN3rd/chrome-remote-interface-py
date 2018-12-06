from asyncio import AbstractEventLoop

import pytest
from aiohttp import ClientConnectorError
from async_timeout import timeout
from websockets import InvalidURI

from cripy.client import connect
from cripy.connection import Connection
from .helpers import Cleaner


class TestConnectFailsNoChrome(object):
    @pytest.mark.asyncio
    async def test_connect_fails_with_nothing_to_connect_to(self):
        with pytest.raises(ClientConnectorError):
            await connect()

    @pytest.mark.asyncio
    async def test_connect_fails_supplied_ws_url_bad(self):
        with pytest.raises(Exception):
            await connect("ws://nope")

    @pytest.mark.asyncio
    async def test_connection_connect_fails_with_no_supplied_ws_url(self):
        with pytest.raises(InvalidURI):
            conn = Connection()
            await conn.connect()

    @pytest.mark.asyncio
    async def test_client_connect_fails_supplied_ws_url_bad_constructor(self):
        with pytest.raises(Exception):
            conn = Connection("ws://nope")
            await conn.connect()

    @pytest.mark.asyncio
    async def test_client_connect_fails_supplied_ws_url_bad_connect(self):
        with pytest.raises(Exception):
            conn = Connection()
            await conn.connect("ws://nope")


@pytest.mark.usefixtures("chrome")
class TestConnect(object):
    @pytest.mark.asyncio
    async def test_connects_using_default_url(self, mr_clean: Cleaner):
        client = await connect()
        mr_clean.add_disposable(client)
        version = await client.Browser.getVersion()
        assert version["product"] in version["userAgent"]

    @pytest.mark.asyncio
    async def test_connects_using_default_url_remote(self, mr_clean: Cleaner):
        client = await connect(remote=True)
        mr_clean.add_disposable(client)
        version = await client.Browser.getVersion()
        assert version["product"] in version["userAgent"]

    @pytest.mark.asyncio
    async def test_connects_using_supplied_url(self, mr_clean: Cleaner):
        client = await connect(url="http://localhost:9222")
        mr_clean.add_disposable(client)
        version = await client.Browser.getVersion()
        assert version["product"] in version["userAgent"]

    @pytest.mark.asyncio
    async def test_connects_using_supplied_url_remote(self, mr_clean: Cleaner):
        client = await connect(url="http://localhost:9222", remote=True)
        mr_clean.add_disposable(client)
        version = await client.Browser.getVersion()
        assert version["product"] in version["userAgent"]

    @pytest.mark.asyncio
    async def test_connects_and_emits_closed_after_dispose_default_url(
        self, mr_clean: Cleaner, event_loop: AbstractEventLoop
    ):
        future = event_loop.create_future()
        client = await connect()

        def listener():
            if not future.done():
                future.set_result(True)

        mr_clean.addEventListener(client, client.Events.Disconnected, listener)

        async with timeout(10, loop=event_loop):
            await client.dispose()

        async with timeout(10, loop=event_loop):
            assert await future

    @pytest.mark.asyncio
    async def test_connects_and_calls_closecb_after_dispose_default_url(
        self, event_loop: AbstractEventLoop
    ):
        future = event_loop.create_future()
        client = await connect()

        def cb():
            if not future.done():
                future.set_result(True)

        client.set_close_callback(cb)

        async with timeout(10, loop=event_loop):
            await client.dispose()

        async with timeout(10, loop=event_loop):
            assert await future

    @pytest.mark.asyncio
    async def test_connects_and_emits_closed_after_dispose_supplied_url(
        self, mr_clean: Cleaner, event_loop: AbstractEventLoop
    ):
        future = event_loop.create_future()
        client = await connect(url="http://localhost:9222")

        def listener():
            if not future.done():
                future.set_result(True)

        mr_clean.addEventListener(client, client.Events.Disconnected, listener)

        async with timeout(10, loop=event_loop):
            await client.dispose()

        async with timeout(10, loop=event_loop):
            assert await future

    @pytest.mark.asyncio
    async def test_connects_and_emits_closed_after_dispose_supplied_url(
        self, event_loop: AbstractEventLoop
    ):
        future = event_loop.create_future()
        client = await connect(url="http://localhost:9222")

        def cb():
            if not future.done():
                future.set_result(True)

        client.set_close_callback(cb)

        async with timeout(10, loop=event_loop):
            await client.dispose()

        async with timeout(10, loop=event_loop):
            assert await future
