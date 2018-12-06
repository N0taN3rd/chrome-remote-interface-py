import pytest
import uvloop
from _pytest.fixtures import SubRequest

from cripy import Client, connect
from .helpers import launch_chrome, Cleaner


@pytest.yield_fixture(scope="class")
def event_loop() -> uvloop.Loop:
    loop = uvloop.new_event_loop()
    yield loop
    loop.close()


@pytest.yield_fixture(scope="class")
async def chrome(request: SubRequest):
    cp, tempdir, wsurl = await launch_chrome()
    if request.cls:
        request.cls.wsurl = wsurl
    yield wsurl
    cp.kill()
    await cp.wait()
    tempdir.cleanup()


@pytest.yield_fixture
async def client(request: SubRequest) -> Client:
    _client = await connect(url=request.cls.wsurl, remote=True)
    request.cls.client = _client
    yield _client
    await _client.dispose()


@pytest.yield_fixture
async def mr_clean(request: SubRequest) -> Cleaner:
    cleaner = Cleaner()
    yield cleaner
    await cleaner.clean_up()
