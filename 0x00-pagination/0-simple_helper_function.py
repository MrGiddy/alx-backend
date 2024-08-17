#!/usr/bin/env python3
"""Contains the definition of `index` helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple containing a start index and an end index"""
    total_size = page * page_size
    offset = total_size - page_size
    return (offset, total_size)
