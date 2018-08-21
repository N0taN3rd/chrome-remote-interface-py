from typing import Any, Callable, ClassVar, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from .client import Client

__all__ = ["Accessibility"]


@attr.dataclass(slots=True)
class Accessibility(object):
    client: "Client" = attr.ib(repr=False)
    dependencies: ClassVar[List[str]] = ["DOM"]

    async def getPartialAXTree(
        self,
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectId: Optional[str] = None,
        fetchRelatives: Optional[bool] = None,
    ) -> Optional[dict]:
        """
        Fetches the accessibility node and partial accessibility tree for this DOM node, if it exists.

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
        res = await self.client.send("Accessibility.getPartialAXTree", msg_dict)
        return res
