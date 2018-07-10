import pytest
from cripy.asyncio import connect


@pytest.mark.usefixtures("chrome")
class TestEvents(object):
    @pytest.mark.asyncio
    async def test_event_cb(self):
        results = []
        client = await connect(wsurl=self.wsurl)
        client.once("Network.requestWillBeSent", lambda x: results.append(True))
        await client.Network.enable()
        await client.Page.navigate("https://google.com")
        assert len(results) == 1
        await client.disconnect()
