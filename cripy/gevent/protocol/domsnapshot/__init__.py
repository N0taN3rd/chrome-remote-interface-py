from cripy.gevent.protocol.domsnapshot import types as Types

__all__ = ["DOMSnapshot"] + Types.__all__


class DOMSnapshot(object):
    """
    This domain facilitates obtaining document snapshots with DOM, layout, and style information.
    """

    dependencies = ["CSS", "DOM", "DOMDebugger", "Page"]

    def __init__(self, chrome):
        self.chrome = chrome

    def disable(self):
        wres = self.chrome.send("DOMSnapshot.disable")
        return wres.get()

    def enable(self):
        wres = self.chrome.send("DOMSnapshot.enable")
        return wres.get()

    def getSnapshot(
        self,
        computedStyleWhitelist,
        includeEventListeners=None,
        includePaintOrder=None,
        includeUserAgentShadowTree=None,
    ):
        """
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
        wres = self.chrome.send("DOMSnapshot.getSnapshot", msg_dict)
        res = wres.get()
        res["domNodes"] = Types.DOMNode.safe_create_from_list(res["domNodes"])
        res["layoutTreeNodes"] = Types.LayoutTreeNode.safe_create_from_list(
            res["layoutTreeNodes"]
        )
        res["computedStyles"] = Types.ComputedStyle.safe_create_from_list(
            res["computedStyles"]
        )
        return res

    @staticmethod
    def get_event_classes():
        return None
