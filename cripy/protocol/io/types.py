from typing import Any, List, Optional, Set, Union, TypeVar
from cripy.helpers import ProtocolType

StreamHandle = TypeVar("StreamHandle", str, str)
"""This is either obtained from another method or specifed as `blob:&lt;uuid&gt;` where `&lt;uuid&gt` is an UUID of a Blob."""
