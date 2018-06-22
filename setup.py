from os import path
from typing import List

from setuptools import setup, find_packages
from pathlib import Path
from m2r import M2R


basedir = Path(path.dirname(path.abspath(__file__)))


def get_requirements() -> List[str]:
    reqs = []
    reqp = basedir.joinpath("requirements.txt")
    with reqp.open("r") as rin:
        for l in rin:
            l = l.rstrip()
            if l != "black":
                reqs.append(l)
    return reqs


def transform_readme() -> str:
    readmep = basedir / 'README.md'
    with readmep.open('r') as rin:
        src = rin.read()
        try:
            readme = M2R()(src)
        except:
            readme = src
    return readme


extra_args = {}
setup(
    name="cripy",
    version="0.0.1",
    description=(
        "Unofficial port of chrome-remote-interface and fork of pyppeteer"
        "(unofficial port of puppeteer)"
    ),
    long_description=transform_readme(),
    author="John Berlin",
    author_email="n0tan3rd@gmail.com",
    url="https://github.com/n0tan3rd/chrome-remote-interface-py",
    packages=['cripy'] + find_packages(),
    include_package_data=True,
    install_requires=get_requirements(),
    zip_safe=True,
    keywords="cripy",
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Archivists",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        'Topic :: Software Development :: DevTools Protocol',
    ],
    python_requires=">=3.6",
    **extra_args,
)
