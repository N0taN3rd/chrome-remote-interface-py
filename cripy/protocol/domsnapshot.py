"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, Any, Dict, List, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cripy import ConnectionType, SessionType

__all__ = ["DOMSnapshot"]


class DOMSnapshot:
    """
    This domain facilitates obtaining document snapshots with DOM, layout, and style information.
     
    Domain Dependencies: 
      * CSS
      * DOM
      * DOMDebugger
      * Page
    Status: Experimental
     
    See `https://chromedevtools.github.io/devtools-protocol/tot/DOMSnapshot`
    """

    __slots__ = ["client"]

    def __init__(self, client: Union["ConnectionType", "SessionType"]) -> None:
        """Initialize a new instance of DOMSnapshot

        :param client: The client instance to be used to communicate with the remote browser instance
        """
        self.client: Union["ConnectionType", "SessionType"] = client

    def disable(self) -> Awaitable[Dict]:
        """
        Disables DOM snapshot agent for the given page.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOMSnapshot#method-disable`

        :return: The results of the command
        """
        return self.client.send("DOMSnapshot.disable", {})

    def enable(self) -> Awaitable[Dict]:
        """
        Enables DOM snapshot agent for the given page.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOMSnapshot#method-enable`

        :return: The results of the command
        """
        return self.client.send("DOMSnapshot.enable", {})

    def getSnapshot(
        self,
        computedStyleWhitelist: List[str],
        includeEventListeners: Optional[bool] = None,
        includePaintOrder: Optional[bool] = None,
        includeUserAgentShadowTree: Optional[bool] = None,
    ) -> Awaitable[Dict]:
        """
        Returns a document snapshot, including the full DOM tree of the root node (including iframes,
        template contents, and imported documents) in a flattened array, as well as layout and
        white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is
        flattened.

        Status: Deprecated

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOMSnapshot#method-getSnapshot`

        :param computedStyleWhitelist: Whitelist of computed styles to return.
        :param includeEventListeners: Whether or not to retrieve details of DOM listeners (default false).
        :param includePaintOrder: Whether to determine and include the paint order index of LayoutTreeNodes (default false).
        :param includeUserAgentShadowTree: Whether to include UA shadow tree in the snapshot (default false).
        :return: The results of the command
        """
        msg = {"computedStyleWhitelist": computedStyleWhitelist}
        if includeEventListeners is not None:
            msg["includeEventListeners"] = includeEventListeners
        if includePaintOrder is not None:
            msg["includePaintOrder"] = includePaintOrder
        if includeUserAgentShadowTree is not None:
            msg["includeUserAgentShadowTree"] = includeUserAgentShadowTree
        return self.client.send("DOMSnapshot.getSnapshot", msg)

    def captureSnapshot(self, computedStyles: List[str]) -> Awaitable[Dict]:
        """
        Returns a document snapshot, including the full DOM tree of the root node (including iframes,
        template contents, and imported documents) in a flattened array, as well as layout and
        white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is
        flattened.

        See `https://chromedevtools.github.io/devtools-protocol/tot/DOMSnapshot#method-captureSnapshot`

        :param computedStyles: Whitelist of computed styles to return.
        :return: The results of the command
        """
        return self.client.send(
            "DOMSnapshot.captureSnapshot", {"computedStyles": computedStyles}
        )
