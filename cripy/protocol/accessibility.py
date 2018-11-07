# -*- coding: utf-8 -*-
"""This is an auto-generated file. Modify at your own risk"""
from typing import Awaitable, ClassVar, List, Optional, Union, TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from cripy.types import ConnectionType, SessionType

__all__ = ["Accessibility"]


@attr.dataclass(slots=True)
class Accessibility(object):
    client: Union["ConnectionType", "SessionType"] = attr.ib()

    dependencies: ClassVar[List[str]] = ["DOM"]

    def disable(self) -> Awaitable[Optional[dict]]:
        """
        Disables the accessibility domain.
        """
        return self.client.send("Accessibility.disable")

    def enable(self) -> Awaitable[Optional[dict]]:
        """
        Enables the accessibility domain which causes `AXNodeId`s to remain consistent between method calls.
This turns on accessibility for the page, which can impact performance until accessibility is disabled.
        """
        return self.client.send("Accessibility.enable")

    def getPartialAXTree(
        self,
        nodeId: Optional[int] = None,
        backendNodeId: Optional[int] = None,
        objectId: Optional[str] = None,
        fetchRelatives: Optional[bool] = None,
    ) -> Awaitable[Optional[dict]]:
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
        return self.client.send("Accessibility.getPartialAXTree", msg_dict)

    def getFullAXTree(self) -> Awaitable[Optional[dict]]:
        """
        Fetches the entire accessibility tree
        """
        return self.client.send("Accessibility.getFullAXTree")
