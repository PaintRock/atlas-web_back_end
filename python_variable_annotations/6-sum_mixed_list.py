#!/usr/bin/env python3

"""Functionsum_mixed_list that takes a mxd_lst and returns the sum"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """mixed list of intergers and floats"""
    return sum(mxd_lst)
