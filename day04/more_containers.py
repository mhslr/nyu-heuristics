from typing import List, Dict
from dataclasses import dataclass


def counter_ab(elements: List):
    # elements == ["a","a","a", "b", "a"]
    assert all(e in ["a", "b"] for e in elements)
    count_a = 0
    count_b = 0
    for elem in elements:
        if elem == "a":
            count_a += 1
        else:
            count_b += 1
    return {"a": count_a, "b": count_b}


def counter(elements: List):
    """
    returns a dictionary counting the number
    of occurences of each distinct element
    >>> counter(["hey", "ho", "hey"])
    {"hey": 2, "ho": 1}
    """
    count_of = {}  # empty dict

    for e in elements:

        if e not in count_of:  # seeing e for the first time
            count_of[e] = 1  # insert into counter

        else:  # seeing another e
            count_of[e] += 1  # increment counter
            # count_of[e] = count_of[e] + 1  # alternative

    return count_of


def invert(person_to_dog: Dict):
    """
    returns a dictionary mapping the values to the keys
    we assume all values are distinct
    >>> invert({1: 3, 24: 4})
    {3: 1, 4: 24}
    """
    return {
        dog: person
        for person, dog in person_to_dog.items()
    }

    dog_to_person = {}  # starts empty
    for person, dog in person_to_dog.items():
        dog_to_person[dog] = person

    return dog_to_person



        


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
