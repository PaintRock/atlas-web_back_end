#!/usr/bin/env python3

"""Functionsum_mixed_list that takes a mxd_lst 
of integers and floats and returns the sum as a 
float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return sum(mxd_lst)
