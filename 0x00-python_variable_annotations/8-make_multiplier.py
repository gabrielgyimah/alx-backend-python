#!/usr/bin/python3
"""Multiplier Module"""


from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by the specified multiplier."""
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
