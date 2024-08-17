#!/usr/bin/env python3
"""Implements a simple pagination for a data of popular baby names"""
import csv
import math
from typing import Tuple
from typing import List


class Server:
    """server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[list]:
        """cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """paginates a cached dataset and returns the appropriate page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        page_start, page_end = index_range(page, page_size)
        try:
            page = self.dataset()[page_start:page_end]
            return page
        except IndexError:
            return []


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple containing a start index and an end index"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
