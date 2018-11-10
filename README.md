CRIPY
=========
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Chrome Remote Interface Python or cripy for short is an unofficial port of [chrome-remote-interface](https://github.com/cyrus-and/chrome-remote-interface) by [@cyrus-and](https://github.com/cyrus-and).
Python 3.5+ only.

Sample Usage
----------------

```python3
import asyncio
import traceback

from cripy import connect

async def go() -> None:
    client = None
    try:
        client = await connect()
        await asyncio.gather(client.Page.enable(), client.Network.enable())
        await client.Page.navigate(
            "https://github.com/webrecorder/chrome-remote-interface-py"
        )
        await client.Page.loadEventFired()
    except Exception:
        traceback.print_exc()
    finally:
        if client is not None:
            await client.dispose()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(go())
```

Implementations
---------------

This module should work with every application implementing the
[Chrome Debugging Protocol]. 

Below is a list of known implementations for reference

Implementation             | Protocol version   | [Protocol] | [List] | [New] | [Activate] | [Close] | [Version]
---------------------------|--------------------|------------|--------|-------|------------|---------|-----------
[Google Chrome][1.1]       | [tip-of-tree][1.2] | yes¹       | yes    | yes   | yes        | yes     | yes
[Opera][2.1]               | [tip-of-tree][2.2] | yes        | yes    | yes   | yes        | yes     | yes
[Node.js][3.1] ([v6.3.0]+) | [node][3.2]        | yes        | no     | no    | no         | no      | yes
[Safari (iOS)][4.1]        | [*partial*][4.2]   | no         | yes    | no    | no         | no      | no
[Microsoft Edge][5.1]      | [*partial*][5.2]   | yes        | yes    | no    | no         | no      | yes

¹ Not available on [Chrome for Android][chrome-mobile-protocol].

[chrome-mobile-protocol]: https://bugs.chromium.org/p/chromium/issues/detail?id=824626#c4

[1.1]: #chromechromium
[1.2]: https://chromedevtools.github.io/devtools-protocol/tot/

[2.1]: #opera
[2.2]: https://chromedevtools.github.io/devtools-protocol/tot/

[3.1]: #nodejs
[3.2]: https://chromedevtools.github.io/devtools-protocol/v8/

[4.1]: #safari-ios
[4.2]: http://trac.webkit.org/browser/trunk/Source/JavaScriptCore/inspector/protocol

[5.1]: #edge
[5.2]: https://docs.microsoft.com/en-us/microsoft-edge/devtools-protocol/0.1/domains/

[Protocol]: #cdpprotocoloptions-callback
[List]: #cdplistoptions-callback
[New]: #cdpnewoptions-callback
[Activate]: #cdpactivateoptions-callback
[Close]: #cdpcloseoptions-callback
[Version]: #cdpversionoptions-callback

API
---

The API consists of three parts:

- *DevTools* methods (for those [implementations](#implementations) that support
  them, e.g., [List](#cdplistoptions-callback), [New](#cdpnewoptions-callback),
  etc.);

- [connection](#cdpoptions-callback) establishment;

- the actual [protocol interaction](#class-cdp).

### connect([**kwargs])

Connects to a remote instance using the [Chrome Debugging Protocol](https://chromedevtools.github.io/devtools-protocol/).

`kwargs`:
- `url: str`: URL or WS URL to use for making the CDP connection. Defaults to http://localhost:9222
- `loop: AbstractEventLoop`: The event loop instance to use. Defaults to asyncio.get_event_loop
- `remote: bool`: Boolean indicating if the protocol should be fetched from the remote instance or
    to use the local one. Defaults to False (use local)
    
Returns:
- `client: Client`: A CDP client connected to the remote browser instance



### CDP.Protocol([**kwargs])

Fetch the [Chrome Debugging Protocol] descriptor.

`kwargs`:
- `frontend_url: str`: Base HTTP endpoint url to use (e.g. http(s)://localhost:9222)
- `host: str`: HTTP frontend host. Defaults to `localhost` (ignored if frontend_url is supplied)
- `port: Union[str, int]`: HTTP frontend port. Defaults to `9222` (ignored if frontend_url is supplied)
- `secure: bool`: HTTPS/WSS frontend. Defaults to `false` 

Returns:
- `protocol`: the [Chrome Debugging Protocol] descriptor.

Example:

```python3
from cripy import Client

async def list_targets() -> None:
    protocol_descriptor = await Client.Protocol()
    print(protocol_descriptor)
```

### Client.List([**kwargs])

Request the list of the available open targets/tabs of the remote instance.

`kwargs`:
- `frontend_url: str`: Base HTTP endpoint url to use (e.g. http(s)://localhost:9222)
- `host: str`: HTTP frontend host. Defaults to `localhost` (ignored if frontend_url is supplied)
- `port: Union[str, int]`: HTTP frontend port. Defaults to `9222` (ignored if frontend_url is supplied)
- `secure: bool`: HTTPS/WSS frontend. Defaults to `false` 

Returns:
- `Awaitable[List[Dict[str,str]]]`: the array returned by `http://host:port/json/list` containing the
  target list.

Example:

```python3
from cripy import Client

async def list_targets() -> None:
    for target in await Client.List():
        print(target)
```

### CDP.New(url, [**kwargs])

Request the list of the available open targets/tabs of the remote instance.

- `url: str`: The URL for the new tab. Defaults to about:blank

`kwargs`:
- `frontend_url: str`: Base HTTP endpoint url to use (e.g. http(s)://localhost:9222)
- `host: str`: HTTP frontend host. Defaults to `localhost` (ignored if frontend_url is supplied)
- `port: Union[str, int]`: HTTP frontend port. Defaults to `9222` (ignored if frontend_url is supplied)
- `secure: bool`: HTTPS/WSS frontend. Defaults to `false` 

Returns:
- `Awaitable[Dict[str,str]]`: the object returned by `http://host:port/json/new` containing the
  target.

Example:

```python3
from cripy import Client

async def list_targets() -> None:
    new_target = await Client.New("https://example.com")
    print(new_target)
```

### CDP.Activate(target_id, [**kwargs])

Activate an open target/tab of the remote instance.
- `target_id: str`: Target id. Required, no default.

`kwargs`:
- `frontend_url: str`: Base HTTP endpoint url to use (e.g. http(s)://localhost:9222)
- `host: str`: HTTP frontend host. Defaults to `localhost` (ignored if frontend_url is supplied)
- `port: Union[str, int]`: HTTP frontend port. Defaults to `9222` (ignored if frontend_url is supplied)
- `secure: bool`: HTTPS/WSS frontend. Defaults to `false` 

Returns: 
- `Awaitable[Tuple[int, str]]`: results of activating the target

Example:

```python3
from cripy import Client

async def list_targets() -> None:
    new_target = await Client.New("https://example.com")
    status_code, info = await Client.Activate(new_target["id"])
    print(f"{status_code}, {info}")
```


### CDP.Close(target_id, [**kwargs])

Close an open target/tab of the remote instance.
- `target_id: str`: Target id. Required, no default.

`kwargs`:
- `frontend_url: str`: Base HTTP endpoint url to use (e.g. http(s)://localhost:9222)
- `host: str`: HTTP frontend host. Defaults to `localhost` (ignored if frontend_url is supplied)
- `port: Union[str, int]`: HTTP frontend port. Defaults to `9222` (ignored if frontend_url is supplied)
- `secure: bool`: HTTPS/WSS frontend. Defaults to `false` 

Returns: 
- `Awaitable[Tuple[int, str]]`: results of activating the target

Example:

```python3
from cripy import Client

async def list_targets() -> None:
    new_target = await Client.New("https://example.com")
    status_code, info = await Client.close(new_target["id"])
    print(f"{status_code}, {info}")
```

### CDP.Version([**kwargs])

Request version information from the remote instance.

`kwargs`:
- `frontend_url: str`: Base HTTP endpoint url to use (e.g. http(s)://localhost:9222)
- `host: str`: HTTP frontend host. Defaults to `localhost` (ignored if frontend_url is supplied)
- `port: Union[str, int]`: HTTP frontend port. Defaults to `9222` (ignored if frontend_url is supplied)
- `secure: bool`: HTTPS/WSS frontend. Defaults to `false` 

Returns:
- `Dict[str, str]`: a JSON object returned by `http://host:port/json/version` containing
  the version information.


Example:

```python3
from cripy import Client

async def list_targets() -> None:
    version_info = await Client.Version()
    print(version_info)
```
