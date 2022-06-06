from typing import List, Dict
from dataclasses import dataclass


def counter(elements: List):
    """
    returns a dictionary counting the number of occurences of each distinct element
    >>> counter(["hey", "ho", "hey"])
    {"hey": 2, "ho": 1}
    """
    res = {}  # TODO
    return res


def invert(k_to_v: Dict):
    """
    returns a dictionary mapping the values to the keys
    we assume all values are distinct
    >>> invert({1: 3, 24: 4})
    {3: 1, 4: 24}
    """
    v_to_k = {}  # TODO
    return v_to_k


def keyof(k_to_v: Dict, val):
    """
    without constructing another dict,
    returns the key corresponding to val
    if key is not in k_to_v, return None
    we assume all values are distinct
    >>> keyof({1: 3, 24: 4}, 4)
    24
    """
    return None
