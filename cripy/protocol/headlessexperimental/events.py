from typing import Any, List, Optional, Union
from cripy.helpers import BaseEvent
try:
    from cripy.protocol.headlessexperimental.types import *
except ImportError:
    pass


class NeedsBeginFramesChangedEvent(BaseEvent):
    """
    Issued when the target starts or stops needing BeginFrames.
    """

    event = "HeadlessExperimental.needsBeginFramesChanged"

    def __init__(self, needsBeginFrames: bool) -> None:
        """
        :param needsBeginFrames: True if BeginFrames are needed, false otherwise.
        :type needsBeginFrames: bool
        """
        super().__init__()
        self.needsBeginFrames = needsBeginFrames

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union['NeedsBeginFramesChangedEvent', dict]]:
        if init is not None:
            try:
                ourselves = NeedsBeginFramesChangedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List[Union['NeedsBeginFramesChangedEvent', dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(NeedsBeginFramesChangedEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "HeadlessExperimental.needsBeginFramesChanged": NeedsBeginFramesChangedEvent,
}

