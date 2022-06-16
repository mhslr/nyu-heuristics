# Testing with pytest
# pip install pytest

# file: mystuff.py


def double(x):
    return x * 2


# file: test_mystuff.py

# TODO uncomment line below
# import mystuff
def test_myfn_10():
    for i in range(10):
        i2 = double(i)
        assert i2 == i * 2


"""
pytest will run all functions named test_XXX

# inside of test_mystuff
pytest test_mystuff.py

# or all files named test_YYY
pytest

# if you need more info about error
pytest -svv test_mystuff.py
# s: show print from your code
# vv: very verbose about why assertion failed
"""
