# -*- coding: utf-8 -*-
"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, ClassVar, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy.types import ConnectionType, SessionType

__all__ = ["DOMSnapshot"]


@attr.dataclass(slots=True)
class DOMSnapshot(object):
    """
    This domain facilitates obtaining document snapshots with DOM, layout, and style information.
    """

    client: Union["ConnectionType", "SessionType"] = attr.ib()

    dependencies: ClassVar[List[str]] = ["CSS", "DOM", "DOMDebugger", "Page"]

    def disable(self) -> Awaitable[Optional[dict]]:
        """
        Disables DOM snapshot agent for the given page.
        """
        return self.client.send("DOMSnapshot.disable")

    def enable(self) -> Awaitable[Optional[dict]]:
        """
        Enables DOM snapshot agent for the given page.
        """
        return self.client.send("DOMSnapshot.enable")

    def getSnapshot(
        self,
        computedStyleWhitelist: List[str],
        includeEventListeners: Optional[bool] = None,
        includePaintOrder: Optional[bool] = None,
        includeUserAgentShadowTree: Optional[bool] = None,
    ) -> Awaitable[Optional[dict]]:
        """
        Returns a document snapshot, including the full DOM tree of the root node (including iframes,
template contents, and imported documents) in a flattened array, as well as layout and
white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is
flattened.

        :param computedStyleWhitelist: Whitelist of computed styles to return.
        :type computedStyleWhitelist: List[str]
        :param includeEventListeners: Whether or not to retrieve details of DOM listeners (default false).
        :type includeEventListeners: Optional[bool]
        :param includePaintOrder: Whether to determine and include the paint order index of LayoutTreeNodes (default false).
        :type includePaintOrder: Optional[bool]
        :param includeUserAgentShadowTree: Whether to include UA shadow tree in the snapshot (default false).
        :type includeUserAgentShadowTree: Optional[bool]
        """
        msg_dict = dict()
        if computedStyleWhitelist is not None:
            msg_dict["computedStyleWhitelist"] = computedStyleWhitelist
        if includeEventListeners is not None:
            msg_dict["includeEventListeners"] = includeEventListeners
        if includePaintOrder is not None:
            msg_dict["includePaintOrder"] = includePaintOrder
        if includeUserAgentShadowTree is not None:
            msg_dict["includeUserAgentShadowTree"] = includeUserAgentShadowTree
        return self.client.send("DOMSnapshot.getSnapshot", msg_dict)

    def captureSnapshot(self, computedStyles: List[str]) -> Awaitable[Optional[dict]]:
        """
        Returns a document snapshot, including the full DOM tree of the root node (including iframes,
template contents, and imported documents) in a flattened array, as well as layout and
white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is
flattened.

        :param computedStyles: Whitelist of computed styles to return.
        :type computedStyles: List[str]
        """
        msg_dict = dict()
        if computedStyles is not None:
            msg_dict["computedStyles"] = computedStyles
        return self.client.send("DOMSnapshot.captureSnapshot", msg_dict)
