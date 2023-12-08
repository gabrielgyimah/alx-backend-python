#!/usr/bin/env python3
"""safe_first_element Module"""
from typing import Optional, Any


def safe_first_element(lst: list) -> Optional[Any]:
    """Returns the first element of the list, otherwise returns None."""
    if lst:
        return lst[0]
    else:
        return None
