from typing import Dict, List, Callable, Any, Optional

import pytest
from aiohttp import ClientConnectorError

from cripy.cdp import CDP
from .helpers import (
    Cleaner,
    evaluation_result,
    make_target_selector,
    get_target_from_list,
)

TARGET_SELECTORS: List[Callable[[List[Dict[str, str]]], Any]] = [
    make_target_selector("dict"),
    make_target_selector("idx"),
    make_target_selector("str"),
]

TARGET_SELECTORS_IDS: List[str] = [
    "function returning target dict",
    "function returning target index",
    "function returning target ws url",
]


class TestCDPClientConnectionFailsNoChrome(object):
    @pytest.mark.asyncio
    async def test_cdp_client_fails_with_nothing_to_connect_to(self):
        with pytest.raises(ClientConnectorError):
            await CDP.client()

    @pytest.mark.asyncio
    async def test_cdp_client_fails_supplied_ws_url_bad(self):
        with pytest.raises(Exception):
            await CDP.client(target="ws://nope")

    @pytest.mark.asyncio
    async def test_cdp_ws_connection_fails_with_nothing_to_connect_to(self):
        with pytest.raises(ClientConnectorError):
            await CDP.ws_connection()

    @pytest.mark.asyncio
    async def test_cdp_ws_connection_fails_supplied_ws_url_bad(self):
        with pytest.raises(Exception):
            await CDP.ws_connection(target="ws://nope")


@pytest.mark.usefixtures("chrome")
class TestCDPClientCreation(object):
    @pytest.mark.asyncio
    async def test_cdp_client_connects_using_defaults(self, mr_clean: Cleaner):
        client = await CDP.client()
        mr_clean.add_disposable(client)
        version = await client.Browser.getVersion()
        assert version["product"] in version["userAgent"]

    @pytest.mark.asyncio
    async def test_cdp_client_connects_using_defaults_remote(self, mr_clean: Cleaner):
        client = await CDP.client(remote=True)
        mr_clean.add_disposable(client)
        version = await client.Browser.getVersion()
        assert version["product"] in version["userAgent"]

    @pytest.mark.asyncio
    async def test_cdp_client_connects_using_ws_url(self, mr_clean: Cleaner):
        ws_url = await get_target_from_list("wsurl")
        assert ws_url is not None
        client = await CDP.client(target=ws_url)
        mr_clean.add_disposable(client)
        version = await client.Browser.getVersion()
        assert version["product"] in version["userAgent"]

    @pytest.mark.asyncio
    async def test_cdp_client_connects_using_relative_ws_url(self, mr_clean: Cleaner):
        ws_url = await get_target_from_list("wsurl")
        assert ws_url is not None
        client = await CDP.client(target=ws_url[ws_url.index("/dev") :])
        mr_clean.add_disposable(client)
        version = await client.Browser.getVersion()
        assert version["product"] in version["userAgent"]

    @pytest.mark.asyncio
    async def test_cdp_client_connects_using_target_id(self, mr_clean: Cleaner):
        target_id = await get_target_from_list("id")
        assert target_id is not None
        client = await CDP.client(target=target_id)
        mr_clean.add_disposable(client)
        version = await client.Browser.getVersion()
        assert version["product"] in version["userAgent"]

    @pytest.mark.asyncio
    async def test_cdp_client_connects_using_target_dict(self, mr_clean: Cleaner):
        the_target = await get_target_from_list("target")
        assert the_target is not None
        client = await CDP.client(target=the_target)
        mr_clean.add_disposable(client)
        version = await client.Browser.getVersion()
        assert version["product"] in version["userAgent"]

    @pytest.mark.asyncio
    async def test_cdp_client_connects_using_supplied_target_http_url(
        self, mr_clean: Cleaner
    ):
        client = await CDP.client(target="http://localhost:9222")
        mr_clean.add_disposable(client)
        version = await client.Browser.getVersion()
        assert version["product"] in version["userAgent"]

    @pytest.mark.asyncio
    async def test_cdp_client_connects_using_supplied_target_http_url_remote(
        self, mr_clean: Cleaner
    ):
        client = await CDP.client(target="http://localhost:9222", remote=True)
        mr_clean.add_disposable(client)
        version = await client.Browser.getVersion()
        assert version["product"] in version["userAgent"]

    @pytest.mark.parametrize("fn", TARGET_SELECTORS, ids=TARGET_SELECTORS_IDS)
    @pytest.mark.asyncio
    async def test_cdp_client_connects_using_supplied_target_function_remote_protocol_fetch(
        self, fn: Callable[[List[Dict[str, str]]], Any]
    ):
        client = await CDP.client(target=fn, remote=True)
        version = await client.Browser.getVersion()
        assert version["product"] in version["userAgent"]
        result_type, result = await evaluation_result(
            client, expression="window.location.href"
        )
        assert result_type == "string"
        assert result == "about:blank"
        await client.dispose()

    @pytest.mark.parametrize("fn", TARGET_SELECTORS, ids=TARGET_SELECTORS_IDS)
    @pytest.mark.asyncio
    async def test_cdp_client_connects_using_supplied_target_function_pregen_protocol(
        self, fn: Callable[[List[Dict[str, str]]], Any]
    ):
        client = await CDP.client(target=fn)
        version = await client.Browser.getVersion()
        assert version["product"] in version["userAgent"]
        result_type, result = await evaluation_result(
            client, expression="window.location.href"
        )
        assert result_type == "string"
        assert result == "about:blank"
        await client.dispose()

    @pytest.mark.parametrize("fn", TARGET_SELECTORS, ids=TARGET_SELECTORS_IDS)
    @pytest.mark.asyncio
    async def test_cdp_client_connects_using_supplied_target_function_supplied_protocol(
        self, fn: Callable[[List[Dict[str, str]]], Any]
    ):
        proto = await CDP.Protocol()
        client = await CDP.client(target=fn, protocol=proto)
        version = await client.Browser.getVersion()
        assert version["product"] in version["userAgent"]
        result_type, result = await evaluation_result(
            client, expression="window.location.href"
        )
        assert result_type == "string"
        assert result == "about:blank"
        await client.dispose()


@pytest.mark.usefixtures("chrome")
class TestCDPWSConnectionCreation(object):
    @pytest.mark.asyncio
    async def test_cdp_ws_connection_connects_using_defaults(self, mr_clean: Cleaner):
        connection = await CDP.ws_connection()
        mr_clean.add_disposable(connection)
        version = await connection.send("Browser.getVersion")
        assert version["product"] in version["userAgent"]

    @pytest.mark.asyncio
    async def test_cdp_ws_connection_connects_using_ws_url(self, mr_clean: Cleaner):
        ws_url = await get_target_from_list("wsurl")
        assert ws_url is not None
        connection = await CDP.ws_connection(target=ws_url)
        mr_clean.add_disposable(connection)
        version = await connection.send("Browser.getVersion")
        assert version["product"] in version["userAgent"]

    @pytest.mark.asyncio
    async def test_cdp_ws_connection_connects_using_relative_ws_url(
        self, mr_clean: Cleaner
    ):
        ws_url = await get_target_from_list("wsurl")
        assert ws_url is not None
        connection = await CDP.ws_connection(target=ws_url[ws_url.index("/dev") :])
        mr_clean.add_disposable(connection)
        version = await connection.send("Browser.getVersion")
        assert version["product"] in version["userAgent"]

    @pytest.mark.asyncio
    async def test_cdp_ws_connection_connects_using_target_id(self, mr_clean: Cleaner):
        target_id = await get_target_from_list("id")
        assert target_id is not None
        connection = await CDP.ws_connection(target=target_id)
        mr_clean.add_disposable(connection)
        version = await connection.send("Browser.getVersion")
        assert version["product"] in version["userAgent"]

    @pytest.mark.asyncio
    async def test_cdp_ws_connection_connects_using_target_dict(
        self, mr_clean: Cleaner
    ):
        the_target = await get_target_from_list("target")
        assert the_target is not None
        connection = await CDP.ws_connection(target=the_target)
        mr_clean.add_disposable(connection)
        version = await connection.send("Browser.getVersion")
        assert version["product"] in version["userAgent"]

    @pytest.mark.asyncio
    async def test_cdp_ws_connection_connects_using_supplied_target_http_url(
        self, mr_clean: Cleaner
    ):
        connection = await CDP.ws_connection(target="http://localhost:9222")
        mr_clean.add_disposable(connection)
        version = await connection.send("Browser.getVersion")
        assert version["product"] in version["userAgent"]

    @pytest.mark.parametrize("fn", TARGET_SELECTORS, ids=TARGET_SELECTORS_IDS)
    @pytest.mark.asyncio
    async def test_cdp_ws_connection_connects_using_supplied_target_function(
        self, fn: Callable[[List[Dict[str, str]]], Any]
    ):
        connection = await CDP.ws_connection(target=fn)
        version = await connection.send("Browser.getVersion")
        assert version["product"] in version["userAgent"]
        result_type, result = await evaluation_result(
            connection, expression="window.location.href"
        )
        assert result_type == "string"
        assert result == "about:blank"
        await connection.dispose()


FRONT_END_URLS: List[Optional[str]] = [None, "http://localhost:9222"]
FRONT_END_URLS_IDS: List[str] = ["using defaults", "using supplied HTTP url"]


@pytest.mark.usefixtures("chrome")
class TestFontEndFns(object):
    @pytest.mark.parametrize("frontend_url", FRONT_END_URLS, ids=FRONT_END_URLS_IDS)
    @pytest.mark.asyncio
    async def test_can_list_targets(self, frontend_url: Any):
        if frontend_url is not None:
            targets = await CDP.List(frontend_url=frontend_url)
        else:
            targets = await CDP.List()
        page_listed = False
        for target in targets:
            if target["type"] == "page":
                page_listed = True
                break
        assert page_listed

    @pytest.mark.parametrize("frontend_url", FRONT_END_URLS, ids=FRONT_END_URLS_IDS)
    @pytest.mark.asyncio
    async def test_can_retrieve_version(self, frontend_url: Any):
        if frontend_url is not None:
            version = await CDP.Version(frontend_url=frontend_url)
        else:
            version = await CDP.Version()
        assert version["Browser"] in version["User-Agent"]

    @pytest.mark.parametrize("frontend_url", FRONT_END_URLS, ids=FRONT_END_URLS_IDS)
    @pytest.mark.asyncio
    async def test_can_retrieve_protocol_descriptor(self, frontend_url: Any):
        if frontend_url is not None:
            version = await CDP.Version(frontend_url=frontend_url)
            proto_descriptor = await CDP.Protocol(frontend_url=frontend_url)
        else:
            version = await CDP.Version()
            proto_descriptor = await CDP.Protocol()
        pv = proto_descriptor["version"]
        major, minor = version["Protocol-Version"].split(".")
        assert pv["major"] == major

    @pytest.mark.parametrize("frontend_url", FRONT_END_URLS, ids=FRONT_END_URLS_IDS)
    @pytest.mark.asyncio
    async def test_can_create_activate_and_close_a_target(self, frontend_url: Any):
        nt_url = "http://example.com"
        if frontend_url is not None:
            new_target = await CDP.New(frontend_url=frontend_url, url=nt_url)
        else:
            new_target = await CDP.New(url=nt_url)
        assert new_target["id"] is not None
        if frontend_url is not None:
            targets = await CDP.List(frontend_url=frontend_url)
        else:
            targets = await CDP.List()
        target_listed = False
        for target in targets:
            if target["id"] == new_target["id"]:
                target_listed = True
                break
        assert target_listed
        if frontend_url is not None:
            activate_results = await CDP.Activate(
                frontend_url=frontend_url, target_id=new_target["id"]
            )
            close_results = await CDP.Close(
                frontend_url=frontend_url, target_id=new_target["id"]
            )
        else:
            activate_results = await CDP.Activate(target_id=new_target["id"])
            close_results = await CDP.Close(target_id=new_target["id"])
        assert activate_results == (200, "Target activated")
        assert close_results == (200, "Target is closing")
