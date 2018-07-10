from typing import Any, List, Optional, Union


__all__ = ["DOMSnapshot"]


class DOMSnapshot(object):
    """
    This domain facilitates obtaining document snapshots with DOM, layout, and style information.
    """

    dependencies = ['CSS', 'DOM', 'DOMDebugger', 'Page']


    def __init__(self, chrome):
        """
        Construct a new DOMSnapshot object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def disable(self) -> Optional[dict]:
        """
        Disables DOM snapshot agent for the given page.
        """
        res = await self.chrome.send('DOMSnapshot.disable')
        return res

    async def enable(self) -> Optional[dict]:
        """
        Enables DOM snapshot agent for the given page.
        """
        res = await self.chrome.send('DOMSnapshot.enable')
        return res

    async def getSnapshot(self, computedStyleWhitelist: List[str], includeEventListeners: Optional[bool] = None, includePaintOrder: Optional[bool] = None, includeUserAgentShadowTree: Optional[bool] = None) -> Optional[dict]:
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
            msg_dict['computedStyleWhitelist'] = computedStyleWhitelist
        if includeEventListeners is not None:
            msg_dict['includeEventListeners'] = includeEventListeners
        if includePaintOrder is not None:
            msg_dict['includePaintOrder'] = includePaintOrder
        if includeUserAgentShadowTree is not None:
            msg_dict['includeUserAgentShadowTree'] = includeUserAgentShadowTree
        res = await self.chrome.send('DOMSnapshot.getSnapshot', msg_dict)
        return res

    async def captureSnapshot(self, computedStyles: List[str]) -> Optional[dict]:
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
            msg_dict['computedStyles'] = computedStyles
        res = await self.chrome.send('DOMSnapshot.captureSnapshot', msg_dict)
        return res



