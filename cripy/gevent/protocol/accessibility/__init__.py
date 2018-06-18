from cripy.gevent.protocol.dom import types as DOM
from cripy.gevent.protocol.runtime import types as Runtime
from cripy.gevent.protocol.accessibility import types as Types

__all__ = ["Accessibility"] + Types.__all__


class Accessibility(object):
    dependencies = ["DOM"]

    def __init__(self, chrome):
        self.chrome = chrome

    def getPartialAXTree(
        self, nodeId=None, backendNodeId=None, objectId=None, fetchRelatives=None
    ):
        """
        :param nodeId: Identifier of the node to get the partial accessibility tree for.
        :type nodeId: Optional[int]
        :param backendNodeId: Identifier of the backend node to get the partial accessibility tree for.
        :type backendNodeId: Optional[int]
        :param objectId: JavaScript object id of the node wrapper to get the partial accessibility tree for.
        :type objectId: Optional[str]
        :param fetchRelatives: Whether to fetch this nodes ancestors, siblings and children. Defaults to true.
        :type fetchRelatives: Optional[bool]
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        if backendNodeId is not None:
            msg_dict["backendNodeId"] = backendNodeId
        if objectId is not None:
            msg_dict["objectId"] = objectId
        if fetchRelatives is not None:
            msg_dict["fetchRelatives"] = fetchRelatives
        wres = self.chrome.send("Accessibility.getPartialAXTree", msg_dict)
        res = wres.get()
        res["nodes"] = Types.AXNode.safe_create_from_list(res["nodes"])
        return res

    @staticmethod
    def get_event_classes():
        return None
