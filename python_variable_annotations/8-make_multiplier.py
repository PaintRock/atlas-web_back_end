#!/usr/bin/env python3

"""Function that takes a float and returns a multipied float"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float adn returns a function"""
    def multiplier_func(num: float) -> float:
        """makes the func into the float"""
        return num * multiplier
    return multiplier_func
