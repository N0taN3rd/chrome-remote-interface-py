# -*- coding: utf-8 -*-

import gc
import socket

from typing import Dict, Optional, Any

__all__ = ["get_free_port", "merge_dict"]


def get_free_port() -> int:
    """Get free port."""
    sock = socket.socket()
    sock.bind(("localhost", 0))
    port = sock.getsockname()[1]
    sock.close()
    del sock
    gc.collect()
    return port


def merge_dict(dict1: Optional[Dict], dict2: Optional[Dict]) -> Dict:
    """

    :param dict1: Optional[Dict]: 
    :param dict2: Optional[Dict]: 

    """
    new_dict = {}
    if dict1:
        new_dict.update(dict1)
    if dict2:
        new_dict.update(dict2)
    return new_dict
