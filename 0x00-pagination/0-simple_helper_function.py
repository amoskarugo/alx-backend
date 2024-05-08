#!/usr/bin/env python3
"""pagination basics"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """a simple function that implements a simple pagination concept by
        returning a start and end index
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end,)
