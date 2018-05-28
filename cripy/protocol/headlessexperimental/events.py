from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class NeedsBeginFramesChangedEvent(BaseEvent):
    """Issued when the target starts or stops needing BeginFrames."""

    event: str = "HeadlessExperimental.needsBeginFramesChanged"

    def __init__(self) -> None:
        """
        :param needsBeginFrames: True if BeginFrames are needed, false otherwise.
        :type bool:
        """
        super().__init__()


EVENT_TO_CLASS = {
   "HeadlessExperimental.needsBeginFramesChanged": NeedsBeginFramesChangedEvent,
}

