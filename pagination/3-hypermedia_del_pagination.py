#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        dataset = self.indexed_dataset()

        if index is None:
            return {'index': None, 'data': [], 'page_size': page_size}

        if index >= len(dataset):
            return {'index': None, 'data': [], 'page_size': page_size}

        next_index = min(index + page_size, len(dataset))
        page_data = [dataset[i] for i in range(index, next_index)]

        return {
            'index': index,
            'data': page_data,
            'page_size': page_size,
        }
