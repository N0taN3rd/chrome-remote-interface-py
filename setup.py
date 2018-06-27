import sys
from os import path
from pathlib import Path

from setuptools import setup, find_packages

basedir = Path(path.dirname(path.abspath(__file__)))


def get_requirements():
    reqs = []
    reqp = basedir.joinpath("requirements.txt")
    with reqp.open("r") as rin:
        for l in rin:
            l = l.rstrip()
            if l != "black":
                reqs.append(l)
    return reqs


requirements_gevent = [
    "cffi",  # gevent dep
    "numpy",  # faster websocket-client frame py3
    "websocket-client",
    "idna",  # faster gevent dns
    "dnspython",  # faster gevent dns
    "gevent",
    "requests",
    "psutil",
    "gevent-eventemitter",
]

requirements_asyncio = [
    "pyee",
    "websockets",
    "cchardet",  # faster asyncio
    "aiodns",  # faster asyncio dns resolution
    "async-timeout",
    "aiohttp",
]

requirements = ["ujson"] + requirements_gevent

if sys.version_info.major == 3 and sys.version_info.minor >= 6:
    requirements += requirements_asyncio


setup(
    name="cripy",
    version="1.0.0",
    description="Unofficial port of chrome-remote-interface",
    author="John Berlin",
    author_email="john.berlin@rhizome.com",
    url="https://github.com/webrecorder/chrome-remote-interface-py",
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    zip_safe=False,
    keywords="cripy",
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Archivists",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: DevTools Protocol",
    ],
    python_requires=">=3",
)
