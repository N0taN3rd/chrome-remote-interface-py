import sys
from .gevent import *

exported = gevent.__all__

if sys.version_info.major == 3 and sys.version_info.minor >= 6:
    from .asyncio import *
    exported.extend(asyncio.__all__)

__all__ = exported
