from cripy.sync.protocol.domsnapshot import types as Types

__all__ = ["DOMSnapshot"]+ Types.__all__ 


class DOMSnapshot(object):
    """
    This domain facilitates obtaining document snapshots with DOM, layout, and style information.
    """

    dependencies = ['CSS', 'DOM', 'DOMDebugger', 'Page']

    def __init__(self, chrome):
        self.chrome = chrome

    def disable(self):
        self.chrome.send('DOMSnapshot.disable')


    def enable(self):
        self.chrome.send('DOMSnapshot.enable')


    def getSnapshot(self, computedStyleWhitelist, includeEventListeners, includePaintOrder, includeUserAgentShadowTree):
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
        def cb(res):
            res['domNodes'] = Types.DOMNode.safe_create_from_list(res['domNodes'])
            res['layoutTreeNodes'] = Types.LayoutTreeNode.safe_create_from_list(res['layoutTreeNodes'])
            res['computedStyles'] = Types.ComputedStyle.safe_create_from_list(res['computedStyles'])
            self.chrome.emit('DOMSnapshot.getSnapshot', res)
        msg_dict = dict()
        if computedStyleWhitelist is not None:
            msg_dict['computedStyleWhitelist'] = computedStyleWhitelist
        if includeEventListeners is not None:
            msg_dict['includeEventListeners'] = includeEventListeners
        if includePaintOrder is not None:
            msg_dict['includePaintOrder'] = includePaintOrder
        if includeUserAgentShadowTree is not None:
            msg_dict['includeUserAgentShadowTree'] = includeUserAgentShadowTree
        self.chrome.send('DOMSnapshot.getSnapshot', params=msg_dict, cb=cb)


    @staticmethod
    def get_event_classes():
        return None

