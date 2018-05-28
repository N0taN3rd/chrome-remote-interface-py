from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class NeedsBeginFramesChangedEvent(BaseEvent):
    """Issued when the target starts or stops needing BeginFrames."""

    event: str = "HeadlessExperimental.needsBeginFramesChanged"

    def __init__(self, needsBeginFrames: bool) -> None:
        """
        :param needsBeginFrames: True if BeginFrames are needed, false otherwise.
        :type needsBeginFrames: bool
        """
        super().__init__()
        self.needsBeginFrames: bool = needsBeginFrames


EVENT_TO_CLASS = {
   "HeadlessExperimental.needsBeginFramesChanged": NeedsBeginFramesChangedEvent,
}

