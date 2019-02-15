"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Cast"]


@attr.dataclass(slots=True, cmp=False)
class Cast(object):
    """
    A domain for interacting with Cast, Presentation API, and Remote Playback API
functionalities.
    """

    client: Union["ConnectionType", "SessionType"] = attr.ib()

    def enable(self, presentationUrl: Optional[str] = None) -> Awaitable[Dict]:
        """
        Starts observing for sinks that can be used for tab mirroring, and if set,
sinks compatible with |presentationUrl| as well. When sinks are found, a
|sinksUpdated| event is fired.
Also starts observing for issue messages. When an issue is added or removed,
an |issueUpdated| event is fired.

        :param presentationUrl: The presentationUrl
        :type presentationUrl: Optional[str]
        """
        msg_dict = dict()
        if presentationUrl is not None:
            msg_dict["presentationUrl"] = presentationUrl
        return self.client.send("Cast.enable", msg_dict)

    def disable(self) -> Awaitable[Dict]:
        """
        Stops observing for sinks and issues.
        """
        return self.client.send("Cast.disable")

    def setSinkToUse(self, sinkName: str) -> Awaitable[Dict]:
        """
        Sets a sink to be used when the web page requests the browser to choose a
sink via Presentation API, Remote Playback API, or Cast SDK.

        :param sinkName: The sinkName
        :type sinkName: str
        """
        msg_dict = dict()
        if sinkName is not None:
            msg_dict["sinkName"] = sinkName
        return self.client.send("Cast.setSinkToUse", msg_dict)

    def startTabMirroring(self, sinkName: str) -> Awaitable[Dict]:
        """
        Starts mirroring the tab to the sink.

        :param sinkName: The sinkName
        :type sinkName: str
        """
        msg_dict = dict()
        if sinkName is not None:
            msg_dict["sinkName"] = sinkName
        return self.client.send("Cast.startTabMirroring", msg_dict)

    def stopCasting(self, sinkName: str) -> Awaitable[Dict]:
        """
        Stops the active Cast session on the sink.

        :param sinkName: The sinkName
        :type sinkName: str
        """
        msg_dict = dict()
        if sinkName is not None:
            msg_dict["sinkName"] = sinkName
        return self.client.send("Cast.stopCasting", msg_dict)

    def sinksUpdated(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        This is fired whenever the list of available sinks changes. A sink is a
        device or a software surface that you can cast to.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("Cast.sinksUpdated", _cb)

            return future

        self.client.on("Cast.sinksUpdated", cb)
        return lambda: self.client.remove_listener("Cast.sinksUpdated", cb)

    def issueUpdated(self, cb: Optional[Callable[..., Any]] = None) -> Any:
        """
        This is fired whenever the outstanding issue/error message changes.
        |issueMessage| is empty if there is no issue.
        """
        if cb is None:
            future = self.client.loop.create_future()

            def _cb(msg: Optional[Any] = None) -> None:
                future.set_result(msg)

            self.client.once("Cast.issueUpdated", _cb)

            return future

        self.client.on("Cast.issueUpdated", cb)
        return lambda: self.client.remove_listener("Cast.issueUpdated", cb)
