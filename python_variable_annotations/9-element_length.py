#!/usr/bin/env python3

"""Annotate a funct and return the values with type"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]: 
    """return the tuple with value type"""
    return [(i, len(i)) for i in lst]
