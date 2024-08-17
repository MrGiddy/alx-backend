#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination"""
import csv
from typing import Dict, List


class Server:
    """server class to paginate a database of popular names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """implements deletion-resilient hypermedia pagination"""
        assert index is not None

        indexed_data = self.indexed_dataset()
        highest_index = max(indexed_data.keys())
        assert index >= 0 and index < highest_index

        page_data = []

        next_index = index
        while len(page_data) < page_size and next_index < highest_index:
            if next_index in indexed_data:
                row = indexed_data.get(next_index)
                page_data.append(row)
            next_index += 1

        hyper_index = {
            'index': index,
            'next_index': next_index if next_index < highest_index else None,
            'page_size': page_size,
            'data': page_data
        }
        return hyper_index
