#!/usr/bin/env python3

"""function that takes a string, int, or float and returns a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns the first element of the tuple as the string
    and the square root of the float
    
    Args:
        k: a string
        
        v: a union of integers and floats
    
    Returns: 
        a tuple of strings and floats   
    
    """
    return (k, float(v ** 2))
