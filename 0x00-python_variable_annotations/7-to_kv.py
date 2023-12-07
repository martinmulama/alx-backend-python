#!/usr/bin/env python3
""" 7. Complex types - string and int/float to tuple
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string 'k' and an int or float 'v' as arguments and returns tuple.
    The first element of the tuple is the string 'k'.
    second element the square of int/float 'v' and is annotated as a float.

    Parameters:
    - k (str): The string key.
    - v (Union[int, float]): The int or float value.

    Returns:
    Tuple[str, float]: A tuple containing the string 'k' and the square of 'v'.
    """
    result = float(v) ** 2
    return k, result
