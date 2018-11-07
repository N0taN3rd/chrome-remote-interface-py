import pytest

from cripy.client import Client


@pytest.mark.usefixtures("chrome")
class TestFontEndFns(object):
    @pytest.mark.asyncio
    async def test_can_list_targets(self):
        targets = await Client.List()
        page_listed = False
        for target in targets:
            if target["type"] == "page":
                page_listed = True
                break
        assert page_listed

    @pytest.mark.asyncio
    async def test_can_retrieve_version(self):
        version = await Client.Version()
        assert version["Browser"] in version["User-Agent"]

    @pytest.mark.asyncio
    async def test_can_retrieve_protocol_descriptor(self):
        version = await Client.Version()
        proto_descriptor = await Client.Protocol()
        pv = proto_descriptor["version"]
        major, minor = version["Protocol-Version"].split(".")
        assert pv["major"] == major

    @pytest.mark.asyncio
    async def test_can_create_activate_and_close_a_target(self):
        nt_url = "http://example.com"
        new_target = await Client.New(url=nt_url)
        assert new_target["id"] is not None
        targets = await Client.List()
        target_listed = False
        for target in targets:
            if target["id"] == new_target["id"]:
                target_listed = True
                break
        assert target_listed
        assert await Client.Activate(target_id=new_target['id']) == (200, 'Target activated')
        assert await Client.Close(target_id=new_target["id"]) == (200, 'Target is closing')
