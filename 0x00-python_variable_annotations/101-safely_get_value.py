#!/usr/bin/env python3
"""More involved type annotations
"""
from email.policy import default
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')
defaults = Union[T, None]
returns = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: defaults) -> returns:
    """Get value from dictionary safely
    """
    if key in dct:
        return dct[key]
    else:
        return default


# annotations = safely_get_value.__annotations__
#
# print("Here's what the mappings should look like")
# for k, v in annotations.items():
#     print( ("{}: {}".format(k, v)))
