import os
import subprocess
import sys
import time
from typing import Any, AsyncGenerator, Generator
from requests import Session

import psutil
import pytest
import uvloop
from _pytest.fixtures import SubRequest

from cripy.asyncio import Client
from .helpers import ChromeLauncher


@pytest.fixture(scope="class")
def event_loop() -> Generator[uvloop.Loop, Any, None]:
    loop = uvloop.new_event_loop()
    yield loop
    loop.close()


@pytest.yield_fixture(scope="class")
def chrome(request: SubRequest):
    cp, tempdir, wsurl = ChromeLauncher.launch()
    if request.cls:
        request.cls.wsurl = wsurl
    yield wsurl
    tempdir.cleanup()
    cp.kill()
    cp.wait()


@pytest.fixture(scope="class")
async def async_client(request: SubRequest):
    client = Client(wsurl=request.cls.wsurl)
    await client.connect()
    request.cls.client = client
    yield client
    await client.disconnect()
