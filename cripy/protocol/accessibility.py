"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["Accessibility"]


class Accessibility:
    """
    Domain Dependencies: 
      * DOM
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/Accessibility`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of Accessibility

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def disable(self) -> Awaitable[Dict]:
        """
        Disables the accessibility domain.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Accessibility#method-disable`

        :return: The results of the command
        """
        return self.client.send("Accessibility.disable", {})

    def enable(self) -> Awaitable[Dict]:
        """
        Enables the accessibility domain which causes `AXNodeId`s to remain consistent between method calls.
        This turns on accessibility for the page, which can impact performance until accessibility is disabled.

        See `https://chromedevtools.github.io/devtools-protocol/tot/Accessibility#method-enable`

        :return: The results of the command
        """
        return self.client.send("Accessibility.enable", {})

    def getPartialAXTree(
        self,
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectId: Optional[str] = None,
        fetchRelatives: Optional[bool] = None,
    ) -> Awaitable[Dict]:
        """
        Fetches the accessibility node and partial accessibility tree for this DOM node, if it exists.

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Accessibility#method-getPartialAXTree`

        :param nodeId: Identifier of the node to get the partial accessibility tree for.
        :param backendNodeId: Identifier of the backend node to get the partial accessibility tree for.
        :param objectId: JavaScript object id of the node wrapper to get the partial accessibility tree for.
        :param fetchRelatives: Whether to fetch this nodes ancestors, siblings and children. Defaults to true.
        :return: The results of the command
        """
        msg = {}
        if nodeId is not None:
            msg["nodeId"] = nodeId
        if backendNodeId is not None:
            msg["backendNodeId"] = backendNodeId
        if objectId is not None:
            msg["objectId"] = objectId
        if fetchRelatives is not None:
            msg["fetchRelatives"] = fetchRelatives
        return self.client.send("Accessibility.getPartialAXTree", msg)

    def getFullAXTree(self) -> Awaitable[Dict]:
        """
        Fetches the entire accessibility tree

        Status: Experimental

        See `https://chromedevtools.github.io/devtools-protocol/tot/Accessibility#method-getFullAXTree`

        :return: The results of the command
        """
        return self.client.send("Accessibility.getFullAXTree", {})
