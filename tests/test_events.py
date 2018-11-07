import pytest
from cripy.client import connect


@pytest.mark.usefixtures("chrome")
class TestEvents(object):
    @pytest.mark.asyncio
    async def test_event_once_cb(self):
        results = []
        client = await connect(url=self.wsurl, remote=True)
        client.once("Network.requestWillBeSent", lambda x: results.append(True))
        await client.Network.enable()
        await client.Page.navigate("https://google.com")
        await client.dispose()
        assert len(results) == 1

    @pytest.mark.asyncio
    async def test_event_once_promise(self):
        client = await connect(url=self.wsurl, remote=True)
        await client.Network.enable()
        await client.Page.navigate("https://google.com")
        assert await client.Network.requestWillBeSent() is not None
        await client.dispose()
