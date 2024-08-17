#!/usr/bin/env python3
"""Implements hypermedia pagination for a dataset of popular baby names"""
import csv
import math
from typing import Tuple
from typing import List
from typing import Mapping


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
        """paginates cached dataset and returns the requested page contents"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        page_start, page_end = index_range(page, page_size)
        try:
            page_data = self.dataset()[page_start:page_end]
            return page_data
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Mapping:
        """implements hypermedia pagination for cached dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None
        hyper = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages,
        }
        return hyper


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple containing page start/end indexes"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
