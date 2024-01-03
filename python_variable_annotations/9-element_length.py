#!/usr/bin/env python3

"""Annotate a given funct and return the values with type"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """ return the values and appropriate type"""
    return[(i, len(i)) for i in lst]
