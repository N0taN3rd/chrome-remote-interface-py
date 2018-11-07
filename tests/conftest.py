import pytest
import uvloop
from _pytest.fixtures import SubRequest

from cripy import Client, connect
from .helpers import launch_chrome


@pytest.yield_fixture
def event_loop() -> uvloop.Loop:
    loop = uvloop.new_event_loop()
    yield loop
    loop.close()


@pytest.yield_fixture
async def chrome(request: SubRequest):
    cp, tempdir, wsurl = await launch_chrome()
    if request.cls:
        request.cls.wsurl = wsurl
    yield wsurl
    tempdir.cleanup()
    cp.terminate()
    await cp.wait()


@pytest.fixture
async def client(request: SubRequest) -> Client:
    client = await connect(url=request.cls.wsurl, remote=True)
    request.cls.client = client
    yield client
    await client.dispose()
