from typing import Dict, List, Union

import pytest
import uvloop
from _pytest.fixtures import SubRequest

from cripy import CDP, Client, connect
from .helpers import Cleaner, launch_chrome

uvloop.install()


@pytest.fixture(scope="class")
def event_loop() -> uvloop.Loop:
    loop = uvloop.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="class")
async def chrome(request: SubRequest):
    cp, tempdir, wsurl = await launch_chrome()
    if request.cls:
        request.cls.wsurl = wsurl
    yield wsurl
    cp.kill()
    await cp.wait()
    try:
        tempdir.cleanup()
    except Exception:
        pass


@pytest.fixture
async def client(request: SubRequest) -> Client:
    _client = await connect(url=request.cls.wsurl, remote=True)
    request.cls.client = _client
    yield _client
    await _client.dispose()


@pytest.fixture
async def mr_clean(request: SubRequest) -> Cleaner:
    cleaner = Cleaner()
    yield cleaner
    await cleaner.clean_up()


@pytest.fixture(scope="class")
async def protocol_def(request: SubRequest) -> Dict[str, Union[List[Dict], Dict]]:
    protocol = await CDP.Protocol()
    request.cls.protocol = protocol
    yield protocol
