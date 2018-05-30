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
    def safe_create(init: Optional[dict]) -> Optional['NeedsBeginFramesChangedEvent']:
        if init is not None:
            return NeedsBeginFramesChangedEvent(**init)
        else:
            return init

    @staticmethod
    def safe_create_from_list(init: Optional[List[dict]]) -> Optional[List['NeedsBeginFramesChangedEvent']]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(NeedsBeginFramesChangedEvent(**it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "HeadlessExperimental.needsBeginFramesChanged": NeedsBeginFramesChangedEvent,
}

