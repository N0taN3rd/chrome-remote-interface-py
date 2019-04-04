from os import path
from pathlib import Path

from setuptools import setup, find_packages

basedir = Path(path.dirname(path.abspath(__file__)))

with basedir.joinpath("README.md").open("r", encoding="utf-8") as f:
    README = f.read()


def get_requirements():
    reqs = []
    reqp = basedir.joinpath("requirements.txt")
    with reqp.open("r") as rin:
        for line in rin:
            reqs.append(line.rstrip())
    return reqs


setup(
    name="cripy",
    version="1.5.0",
    description="Unofficial port of chrome-remote-interface",
    long_description=README,
    long_description_content_type="text/markdown",
    author="John Berlin",
    author_email="john.berlin@rhizome.com",
    url="https://github.com/webrecorder/chrome-remote-interface-py",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=get_requirements(),
    package_data={"": ["templates/simple/*.j2", "templates/full/*.j2"]},
    include_package_data=True,
    zip_safe=False,
    license="Apache",
    keywords="cripy",
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Archivists",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: DevTools Protocol",
    ],
    python_requires=">=3.6",
)
