#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """returns tuple containing start and end index"""
    start = page_size * (page - 1)
    end = start + page_size
    return (start, end)
