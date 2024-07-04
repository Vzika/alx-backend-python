#!/usr/bin/env python3
"""Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a given float by the provided multiplier.
    Args:
    - multiplier: The float value to multiply by.

    Returns:
    - A function that takes a float argument and returns the product of
    the argument and the multiplier.
    """
    return lambda x: x * multiplier


# fun = make_multiplier(2.22)
# print("{}".format(fun(2.22)))
