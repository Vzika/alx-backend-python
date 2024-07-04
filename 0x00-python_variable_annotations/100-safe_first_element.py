#!/usr/bin/env python3
"""Duck typing - first element of a sequence
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Get the first element of a sequence safely.

    Args:
    - lst: A sequence of elements of any type.

    Returns:
    - The first element of the sequence if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None


# print(safe_first_element.__annotations__)
