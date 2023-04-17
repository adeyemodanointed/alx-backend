#!/usr/bin/env python3
"""Simple pagination"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """returns tuple containing start and end index"""
    start = page_size * (page - 1)
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get_page that takes two integer arguments page with
        default value 1 and page_size with default value 10."""
        try:
            assert page > 0 and page_size > 0
        except Exception:
            raise AssertionError
        index = index_range(page, page_size)
        return self.dataset()[index[0]:index[1]]
