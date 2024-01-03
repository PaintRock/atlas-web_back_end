#!/usr/bin/env python3

"""function that takes a string and returns a tuple"""
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns the first element of the tuple as the string
    and the square root of the float"""
    return (k, float(v ** 2))
