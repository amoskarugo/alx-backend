#!/usr/bin/env python3

"""pagination basics"""

import csv
import math
from typing import List


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
        """a function that returns a page"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start = (page - 1) * page_size
        end = start + page_size
        if not self.__dataset:
            dataset = self.dataset()
            return dataset[start:end]
        return self.__dataset[start:end]

    def get_hyper(self, page: int, page_size: int) -> dict:
        """ return dictionary containing data returned"""
        data = self.get_page(page, page_size)
        size_all_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page + 1 < size_all_pages else None
        prev_page = page - 1 if page > 1 else None

        hyper_data = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": size_all_pages,
        }

        return hyper_data
