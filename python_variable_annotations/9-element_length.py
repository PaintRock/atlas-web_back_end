#!/usr/bin/env python3

"""Annotate a given funct and return the values with type"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]: 
    """return the tuple and something else is what is req"""
    return [(i, len(i)) for i in lst]
