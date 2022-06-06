from hypothesis import given, strategies as st
from sort import *


@given(st.lists(st.integers()))
def test_bubble_sort(arr):
    assert bubble_sort(arr) == sorted(arr)


@given(st.lists(st.integers()))
def test_merge_sort(arr):
    assert merge_sort(arr) == sorted(arr)


@given(st.lists(st.integers()))
def test_quicksort(arr):
    assert quicksort(arr) == sorted(arr)


@given(st.lists(st.integers()))
def test_heapsort(arr):
    assert heapsort(arr) == sorted(arr)
