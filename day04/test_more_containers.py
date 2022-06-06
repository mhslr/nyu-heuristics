from collections import Counter
import random

from more_containers import counter, invert, keyof


def test_counter():
    choices = ["hey", 1.2, (1, 2, 4), "you", "", 0]
    for test in range(30):
        elems = [random.choice(choices) for i in range(random.randint(0, 20))]
        res = counter(elems)
        expected = dict(Counter(elems))
        assert res == expected


invert_samples = [
    (
        {"name": "John", "age": 30, "car": None},
        {None: "car", 30: "age", "John": "name"},
    ),
    ({1: 2, 3: 6, 2: 3}, {2: 1, 6: 3, 3: 2}),
    ({"a": "b", "b": "c", "c": "a"}, {"a": "c", "b": "a", "c": "b"}),
]


def test_invert():
    for d1, d2 in invert_samples:
        assert invert(d1) == d2


def test_keyof():
    for d1, d2 in invert_samples:
        for k in d1:
            assert keyof(d2, k) == d1[k]
        assert keyof(d2, "missing thing") == None
