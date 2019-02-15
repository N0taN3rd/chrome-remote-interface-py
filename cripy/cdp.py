import asyncio
import re
import ujson
from asyncio import AbstractEventLoop
from typing import Any, Callable, Dict, List, Pattern, Optional, Tuple, Union
from urllib.parse import urljoin, urlparse

from aiohttp import ClientSession, TCPConnector, AsyncResolver

from .client import Client
from .connection import Connection
from .errors import ClientError
from .protogen.generate import dynamically_generate_domains

__all__ = [
    "DEFAULT_HOST",
    "DEFAULT_PORT",
    "DEFAULT_URL",
    "CDP",
    "connect",
    "ensure_cdp_url_endswith",
    "fetch_ws_url",
    "fetch_and_gen_proto_classes",
    "front_end_url",
    "get_wsurl_callable_target",
    "get_connectable_target_wsurl",
]

DEFAULT_HOST: str = "localhost"
DEFAULT_PORT: int = 9222
DEFAULT_URL: str = "http://localhost:9222"

ProtocolDef = Dict[str, Union[List[Dict], Dict]]
TargetArgT = Union[str, Callable[[List[Dict]], Union[str, Dict]], Dict]

WS_TEST: Pattern = re.compile(r"^wss?:", re.IGNORECASE)
HTTP_TEST: Pattern = re.compile(r"^https?:", re.IGNORECASE)


def make_http_session(loop: Optional[AbstractEventLoop] = None) -> ClientSession:
    """Creates and returns a new aiohttp.ClientSession that uses AsyncResolver

    :param loop: Optional asyncio event loop to use. Defaults to asyncio.get_event_loop()
    :return: An instance of aiohttp.ClientSession
    """
    if loop is None:
        loop = asyncio.get_event_loop()
    return ClientSession(
        connector=TCPConnector(resolver=AsyncResolver(loop=loop), loop=loop),
        json_serialize=ujson.dumps,
        loop=loop,
    )


async def fetch_and_gen_proto_classes(
    url: str, loop: Optional[AbstractEventLoop] = None
) -> Dict[str, Any]:
    purl = urlparse(url)
    host, port = purl.netloc.split(":")
    is_https = purl.scheme.startswith("wss") or purl.scheme.startswith("https")
    raw_proto = await CDP.Protocol(host=host, port=port, secure=is_https, loop=loop)
    proto_def = await dynamically_generate_domains(raw_proto, loop=loop)
    return proto_def


async def connect(
    url: Optional[str] = DEFAULT_URL,
    protocol: Optional[ProtocolDef] = None,
    remote: bool = False,
    flatten_sessions: bool = False,
    loop: Optional[AbstractEventLoop] = None,
) -> Client:
    """Convince function for creating an instance of the ChromeRemoteInterface and connecting it
    to the remote instance.

    :param url: URL or WS URL to use for making the CDP connection. Defaults to
    http://localhost:9222
    :param protocol: Chrome Debugging Protocol descriptor. Defaults to the protocol chosen according to the
    remote option
    :param remote: a boolean indicating whether the protocol must be fetched remotely or if the local
    version should be used. It has no effect if the protocol option is set. Defaults to false
    :param flatten_sessions: a boolean indicating whether to enables the "flat" access to the session
    via specifying sessionId attribute in the commands when targets are connected to via either TargetSession
    or CDPSession
    :param loop: The event loop instance to use. Defaults to asyncio.get_event_loop
    :return: Client instance connected to the browser
    """
    if loop is None:
        loop = asyncio.get_event_loop()
    ws_url = None
    if HTTP_TEST.match(url) is not None:
        tabs = await CDP.List(frontend_url=url, loop=loop)
        for tab in tabs:
            if tab["type"] == "page":
                ws_url = tab["webSocketDebuggerUrl"]
                break
    elif WS_TEST.match(url) is not None:
        ws_url = url
    else:
        raise ClientError(f"The supplied URL was not a WS or HTTP url: url = {url}")
    if protocol is not None:
        proto_def = await dynamically_generate_domains(protocol, loop=loop)
    elif remote:
        proto_def = await fetch_and_gen_proto_classes(ws_url, loop=loop)
    else:
        proto_def = None
    client = Client(
        ws_url, flatten_sessions=flatten_sessions, proto_def=proto_def, loop=loop
    )
    await client.connect()
    return client


def front_end_url(
    host: Optional[str] = DEFAULT_HOST,
    port: Optional[Union[int, str]] = DEFAULT_PORT,
    secure: Optional[bool] = False,
) -> str:
    """Constructs the CDP frontend URL from the supplied host and port.

    :param host: HTTP frontend host. Defaults to localhost
    :param port: HTTP frontend port. Defaults to 9222
    :param secure: Is the frontend endpoint using HTTPS?. Defaults to false
    :return: The frontend URL
    """
    return f"{'https:' if secure else 'http:'}//{host}:{port}"


async def get_wsurl_callable_target(
    fn: Callable[[List[Dict]], Union[str, Dict]],
    host: Optional[str] = DEFAULT_HOST,
    port: Optional[Union[int, str]] = DEFAULT_PORT,
    secure: Optional[bool] = False,
    loop: Optional[AbstractEventLoop] = None,
) -> str:
    """Retrieves the webSocketDebuggerUrl of the target to be connected to using the supplied
    target selection function.

    Uses CDP.List to retrieve the list of targets and then calls the target selection
    function with the returned list.

    :param fn: The target selection function that returns either the target dictionary
    (representing the target to be connected to) directly, a string (the
    webSocketDebuggerUrl of the target to be connected to), or an integer indicating
    the index of the target to connect to
    :param host: HTTP frontend host. Defaults to localhost
    :param port: HTTP frontend port. Defaults to 9222
    :param secure: HTTPS frontend. Defaults to false
    :param loop: The event loop instance to use. Defaults to asyncio.get_event_loop
    :return: The webSocketDebuggerUrl of the target to be connected to
    :raises ClientError: When the target selection function does not return a target
    or the return value is not allowed
    """
    if loop is None:
        loop = asyncio.get_event_loop()
    targets = await CDP.List(host=host, port=port, secure=secure, loop=loop)
    result = fn(targets)
    if result is None:
        raise ClientError(
            "The target selection function did not return a target for us to connect to"
        )
    if isinstance(result, dict):
        return result["webSocketDebuggerUrl"]
    elif isinstance(result, str):
        return result
    elif isinstance(result, int):
        return targets[result]["webSocketDebuggerUrl"]

    raise ClientError(
        f"The supplied target function did not return a target for us to connect to. "
        f"The returned target is {result}"
    )


async def fetch_ws_url(
    frontend_url: Optional[str] = None,
    host: Optional[str] = DEFAULT_HOST,
    port: Optional[Union[int, str]] = DEFAULT_PORT,
    secure: Optional[bool] = False,
    loop: Optional[AbstractEventLoop] = None,
) -> str:
    """Fetches and attempts to find the webSocketDebuggerUrl of a connectable target.

    Uses CDP.List to retrieve the list of targets and if a page target is found returns its
    webSocketDebuggerUrl otherwise the webSocketDebuggerUrl of another target if any.

    :param frontend_url: Optional base HTTP endpoint url to use (e.g. http(s)://localhost:9222)
    :param host: HTTP frontend host. Defaults to localhost
    :param port: HTTP frontend port. Defaults to 9222
    :param secure: HTTPS frontend. Defaults to false
    :param loop: The event loop instance to use. Defaults to asyncio.get_event_loop
    :return: The webSocketDebuggerUrl of the target to be connected to
    :raises ClientError: If an inspectable target could not be found
    """
    if loop is None:
        loop = asyncio.get_event_loop()
    furl = (
        frontend_url
        if frontend_url is not None
        else front_end_url(host=host, port=port, secure=secure)
    )
    targets = await CDP.List(frontend_url=furl, loop=loop)
    backup = None
    for target in targets:
        if target.get("webSocketDebuggerUrl") is not None:
            backup = backup or target
            if target["type"] == "page":
                return target.get("webSocketDebuggerUrl")
    if (
        backup is not None and backup.get("webSocketDebuggerUrl") is not None
    ):  # pragma: no cover
        return backup.get("webSocketDebuggerUrl")  # pragma: no cover
    raise ClientError(
        f"Could not find a inspectable target to connect to: frontend url = {furl}, targets = {targets}"
    )


async def get_connectable_target_wsurl(
    host: Optional[str] = DEFAULT_HOST,
    port: Optional[Union[int, str]] = DEFAULT_PORT,
    secure: Optional[bool] = False,
    target: Optional[TargetArgT] = None,
    loop: Optional[AbstractEventLoop] = None,
) -> str:
    """Retrieves the webSocketDebuggerUrl for the target to be connected to.

    The target param determines which target this client should attach to.

    The behavior changes according to the type:
     - a function that takes the list returned by the List method and returns a target or its numeric index
       relative to the list or the WebSocket URL of the target

     - a target object like those returned by the New and List methods

     - a string representing the raw WebSocket URL, in this case host and port are not used to fetch the
       target list, unless the URL is relative

     - a string representing the target id

     - a string representing the HTTP(s) URL of the debugging frontend

    :param host: HTTP frontend host. Defaults to localhost
    :param port: HTTP frontend port. Defaults to 9222
    :param secure: HTTPS frontend. Defaults to false
    :param target: Determines which target this client should attach to
    :param loop: The event loop instance to use. Defaults to asyncio.get_event_loop
    :return: The webSocketDebuggerUrl of the target to be connected to
    """
    if loop is None:
        loop = asyncio.get_event_loop()  # pragma: no cover
    if target is not None:
        if callable(target):
            return await get_wsurl_callable_target(
                fn=target, host=host, port=port, secure=secure, loop=loop
            )
        elif isinstance(target, dict):
            return target["webSocketDebuggerUrl"]
        elif isinstance(target, str):
            if target.startswith("/"):
                target = f"ws{'s' if secure else ''}://{host}:{port}{target}"
            if WS_TEST.match(target) is not None:
                return target
            elif HTTP_TEST.match(target) is not None:
                return await fetch_ws_url(frontend_url=target, loop=loop)
            else:

                def find_target_by_id(targets: List[Dict[str, str]]) -> Optional[str]:
                    for t in targets:
                        if t["id"] == target:
                            return t["webSocketDebuggerUrl"]
                    return None  # pragma: no cover

                return await get_wsurl_callable_target(
                    fn=find_target_by_id, host=host, port=port, secure=secure, loop=loop
                )
        raise ClientError(
            f"The supplied target ({target}) is not a type ({type(target)}) we know how to handle"
        )

    return await fetch_ws_url(host=host, port=port, secure=secure, loop=loop)


class CDP(object):
    @staticmethod
    async def client(
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[Union[int, str]] = DEFAULT_PORT,
        secure: Optional[bool] = False,
        target: Optional[TargetArgT] = None,
        protocol: Optional[ProtocolDef] = None,
        remote: bool = False,
        flatten_sessions: bool = False,
        loop: Optional[AbstractEventLoop] = None,
    ) -> Client:
        """Returns a cripy.Client instance connected to the desired target.

        The target param determines which target this client should attach to.

        The behavior changes according to the type:
          - a function that takes the list returned by the List method and returns a target or its numeric index
            relative to the list or the WebSocket URL of the target

          - a target object like those returned by the New and List methods

          - a string representing the raw WebSocket URL, in this case host and port are not used to fetch the
            target list, unless the URL is relative

          - a string representing the target id

          - a string representing the HTTP(s) URL of the debugging frontend

        :param host: HTTP frontend host. Defaults to localhost
        :param port: HTTP frontend port. Defaults to 9222
        :param secure: HTTPS frontend. Defaults to false
        :param target: Determines which target this client should attach to
        :param protocol: Chrome Debugging Protocol descriptor. Defaults to the protocol chosen according to the
        remote option
        :param remote: a boolean indicating whether the protocol must be fetched remotely or if the local
        version should be used. It has no effect if the protocol option is set. Defaults to false
        :param flatten_sessions: a boolean indicating whether to enables the "flat" access to the session
        via specifying sessionId attribute in the commands when targets are connected to via either TargetSession
        or CDPSession
        :param loop: The event loop instance to use. Defaults to asyncio.get_event_loop
        :return: A cripy.Client instance connected to the desired target
        """
        if loop is None:
            loop = asyncio.get_event_loop()  # pragma: no cover
        ws_url = await get_connectable_target_wsurl(
            host=host, port=port, secure=secure, target=target, loop=loop
        )
        if protocol is not None:
            proto_def = await dynamically_generate_domains(protocol, loop=loop)
        elif remote:
            proto_def = await fetch_and_gen_proto_classes(ws_url, loop=loop)
        else:
            proto_def = None
        client: Client = Client(
            ws_url, flatten_sessions=flatten_sessions, proto_def=proto_def, loop=loop
        )
        await client.connect()
        return client

    @staticmethod
    async def ws_connection(
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[Union[int, str]] = DEFAULT_PORT,
        secure: Optional[bool] = False,
        target: Optional[TargetArgT] = None,
        flatten_sessions: bool = False,
        loop: Optional[AbstractEventLoop] = None,
    ) -> Connection:
        """Returns a cripy.Connection instance connected to the desired target.

        The target param determines which target this client should attach to.

        The behavior changes according to the type:
          - a function that takes the list returned by the List method and returns a target or its numeric index
            relative to the list or the WebSocket URL of the target

          - a target object like those returned by the New and List methods

          - a string representing the raw WebSocket URL, in this case host and port are not used to fetch the
            target list, unless the URL is relative

          - a string representing the target id

          - a string representing the HTTP(s) URL of the debugging frontend

        :param host: HTTP frontend host. Defaults to localhost
        :param port: HTTP frontend port. Defaults to 9222
        :param secure: HTTPS frontend. Defaults to false
        :param target: Determines which target this client should attach to
        :param flatten_sessions: a boolean indicating whether to enables the "flat" access to the session
        via specifying sessionId attribute in the commands when targets are connected to via either TargetSession
        or CDPSession
        :param loop: The event loop instance to use. Defaults to asyncio.get_event_loop
        :return: A cripy.Connection instance connected to the desired target
        """
        if loop is None:
            loop = asyncio.get_event_loop()
        ws_url = await get_connectable_target_wsurl(
            host=host, port=port, secure=secure, target=target, loop=loop
        )
        conn: Connection = Connection(
            ws_url, flatten_sessions=flatten_sessions, loop=loop
        )
        await conn.connect()
        return conn

    @staticmethod
    async def Close(
        target_id: str,
        frontend_url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[Union[int, str]] = DEFAULT_PORT,
        secure: Optional[bool] = False,
        loop: Optional[AbstractEventLoop] = None,
    ) -> Tuple[int, str]:
        """Close an open target/tab of the remote instance.

        :param target_id: Target id. Required, no default
        :param frontend_url: Base HTTP endpoint url to use (e.g. http(s)://localhost:9222)
        :param host: HTTP frontend host. Defaults to localhost
        :param port: HTTP frontend port. Defaults to 9222
        :param secure: HTTPS/WSS frontend. Defaults to false
        :param loop: Optional asyncio Loop to use, defaults to asyncio.get_event_loop()
        """
        if loop is None:
            loop = asyncio.get_event_loop()
        if frontend_url is None:
            frontend_url = (
                f"{front_end_url(host=host, port=port, secure=secure)}/json/close/"
            )
        else:
            frontend_url = frontend_url.lower()
        async with make_http_session(loop=loop) as session:
            async with session.get(
                urljoin(ensure_cdp_url_endswith(frontend_url, "json/close/"), target_id)
            ) as res:
                return res.status, await res.text()

    @staticmethod
    async def Activate(
        target_id: str,
        frontend_url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[Union[int, str]] = DEFAULT_PORT,
        secure: Optional[bool] = False,
        loop: Optional[AbstractEventLoop] = None,
    ) -> Tuple[int, str]:
        """Activate an open target/tab of the remote instance.

        :param target_id: Target id. Required, no default
        :param frontend_url: Base HTTP endpoint url to use (e.g. http(s)://localhost:9222)
        :param host: HTTP frontend host. Defaults to localhost
        :param port: HTTP frontend port. Defaults to 9222
        :param secure: HTTPS/WSS frontend. Defaults to false
        :param loop: Optional asyncio Loop to use, defaults to asyncio.get_event_loop()
        """
        if loop is None:
            loop = asyncio.get_event_loop()
        if frontend_url is None:
            frontend_url = (
                f"{front_end_url(host=host, port=port, secure=secure)}/json/activate/"
            )
        else:
            frontend_url = frontend_url.lower()
        async with make_http_session(loop=loop) as session:
            async with session.get(
                urljoin(
                    ensure_cdp_url_endswith(frontend_url, "json/activate/"), target_id
                )
            ) as res:
                return res.status, await res.text()

    @staticmethod
    async def Protocol(
        frontend_url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[Union[int, str]] = DEFAULT_PORT,
        secure: Optional[bool] = False,
        loop: Optional[AbstractEventLoop] = None,
    ) -> Dict[str, Union[List[Dict], Dict]]:
        """Fetch the Chrome DevTools Protocol descriptor.

        :param frontend_url: Base HTTP endpoint url to use (e.g. http(s)://localhost:9222)
        :param host: HTTP frontend host. Defaults to localhost
        :param port: HTTP frontend port. Defaults to 9222
        :param secure: HTTPS/WSS frontend. Defaults to false
        :param loop: Optional asyncio Loop to use, defaults to asyncio.get_event_loop()
        """
        if loop is None:
            loop = asyncio.get_event_loop()
        if frontend_url is None:
            frontend_url = (
                f"{front_end_url(host=host, port=port, secure=secure)}/json/protocol"
            )
        else:
            frontend_url = frontend_url.lower()
        async with make_http_session(loop=loop) as session:
            async with session.get(
                ensure_cdp_url_endswith(frontend_url, "json/protocol")
            ) as res:
                return await res.json()

    @staticmethod
    async def List(
        frontend_url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[Union[int, str]] = DEFAULT_PORT,
        secure: Optional[bool] = False,
        loop: Optional[AbstractEventLoop] = None,
    ) -> List[Dict[str, str]]:
        """Request a list of the available open targets/tabs of the remote instance.

        :param frontend_url: Base HTTP endpoint url to use (e.g. http(s)://localhost:9222)
        :param host: HTTP frontend host. Defaults to localhost
        :param port: HTTP frontend port. Defaults to 9222
        :param secure: HTTPS/WSS frontend. Defaults to false
        :param loop: Optional asyncio Loop to use, defaults to asyncio.get_event_loop()
        """
        if loop is None:
            loop = asyncio.get_event_loop()
        if frontend_url is None:
            frontend_url = (
                f"{front_end_url(host=host, port=port, secure=secure)}/json/list"
            )
        else:
            frontend_url = frontend_url.lower()
        async with make_http_session(loop=loop) as session:
            async with session.get(
                ensure_cdp_url_endswith(frontend_url, "json/list")
            ) as res:
                return await res.json()

    @staticmethod
    async def New(
        url: Optional[str] = None,
        frontend_url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[Union[int, str]] = DEFAULT_PORT,
        secure: Optional[bool] = False,
        loop: Optional[AbstractEventLoop] = None,
    ) -> Dict[str, str]:
        """Create a new target/tab in the remote instance.

        :param url: The URL for the new tab. Defaults to about:blank
        :param frontend_url: Base HTTP endpoint url to use (e.g. http(s)://localhost:9222)
        :param host: HTTP frontend host. Defaults to localhost
        :param port: HTTP frontend port. Defaults to 9222
        :param secure: HTTPS/WSS frontend. Defaults to false
        :param loop: Optional asyncio Loop to use, defaults to asyncio.get_event_loop()
        """
        if loop is None:
            loop = asyncio.get_event_loop()
        if frontend_url is None:
            frontend_url = (
                f"{front_end_url(host=host, port=port, secure=secure)}/json/new"
            )
        else:
            frontend_url = frontend_url.lower()
        frontend_url = ensure_cdp_url_endswith(frontend_url, "json/new")
        if url is not None:
            frontend_url = f"{frontend_url}?{url}"
        async with make_http_session(loop=loop) as session:
            async with session.get(frontend_url) as res:
                return await res.json()

    @staticmethod
    async def Version(
        frontend_url: Optional[str] = None,
        host: Optional[str] = DEFAULT_HOST,
        port: Optional[Union[int, str]] = DEFAULT_PORT,
        secure: Optional[bool] = False,
        loop: Optional[AbstractEventLoop] = None,
    ) -> Dict[str, str]:
        """Request version information from the remote instance.

        :param frontend_url: Base HTTP endpoint url to use (e.g. http(s)://localhost:9222)
        :param host: HTTP frontend host. Defaults to localhost
        :param port: HTTP frontend port. Defaults to 9222
        :param secure: HTTPS/WSS frontend. Defaults to false
        :param loop: Optional asyncio Loop to use, defaults to asyncio.get_event_loop()
        """
        if loop is None:
            loop = asyncio.get_event_loop()
        if frontend_url is None:
            frontend_url = (
                f"{front_end_url(host=host, port=port, secure=secure)}/json/version"
            )
        else:
            frontend_url = frontend_url.lower()
        async with make_http_session(loop=loop) as session:
            async with session.get(
                ensure_cdp_url_endswith(frontend_url, "json/version")
            ) as data:
                return await data.json()


def ensure_cdp_url_endswith(url: str, path: str) -> str:
    """Ensures the supplied CDP URL ends with path. If the supplied
    URL does end with the path it is returned unmodified otherwise
    it is returned with the path added

    :param url: A CDP URL that maybe ends with the expected path
    :param path: The path the URL should end with
    :return: The ensured URL
    """
    if not url.endswith(path):
        return urljoin(url if url.endswith("/") else f"{url}/", path)
    return url
