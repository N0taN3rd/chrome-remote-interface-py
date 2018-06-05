CRIPY
=========
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Chrome Remote Interface Python or Cripy for short is an unofficial port of [chrome-remote-interface](https://github.com/cyrus-and/chrome-remote-interface) by [@cyrus-and](https://github.com/cyrus-and).

Also included (currently) is an unofficial fork of [Pyppeteer](https://github.com/miyakogi/pyppeteer) (MIT) by [@miyakogi](https://github.com/miyakogi)that has been updated and adapted to work with CRIPY's primary reason for existing which is a python version of the [chrome-remote-interface](https://github.com/cyrus-and/chrome-remote-interface).

CRIPY's implementation of the [chrome-remote-interface](https://github.com/cyrus-and/chrome-remote-interface) took inspiration by  [chromewhip](https://github.com/chuckus/chromewhip) (MIT) by [@chuckus](https://github.com/chuckus) and the project generated its protocol python classes.

CRIPY's generation implementation, unlike [chromewhip](https://github.com/chuckus/chromewhip)'s, uses a generation scheme backed by more detailed static analysis of the protocol in order to generate an intelligent set of classes that understand their types.  

CRIPY is
* Free software: MIT license
* Python 3.6 Only
