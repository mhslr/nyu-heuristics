from itertools import permutations
from hypothesis import given, example, strategies as st


def compute_greedy(exact_change, a, b, c, d):
    assert a == 1
    nd = exact_change // d  # integer division
    exact_change %= d  # remainder modulo d
    nc = exact_change // c
    exact_change %= c
    nb = exact_change // b
    exact_change %= b
    na = exact_change
    return na, nb, nc, nd


def compute_greedy_perm_value(exact_change, a, b, c, d):
    assert a == 1
    return min(
        sum(compute_greedy(exact_change, a, *denom))
        # here we lose track of which coin is b,c,d
        for denom in permutations((b, c, d))
    )


def compute_greedy_perm(exact_change, a, b, c, d):
    assert a == 1

    def check(x):
        idx, bcd = zip(*x)  # zip(*x) transposes the 2D array x
        na, *n_bcd = compute_greedy(exact_change, a, *bcd)
        nb, nc, nd = n_bcd[idx[0]], n_bcd[idx[1]], n_bcd[idx[2]]
        return na, nb, nc, nd

    indexed_bcd = list(zip(range(3), (b, c, d)))
    assert indexed_bcd == [(0, b), (1, c), (2, d)]
    return min((check(x) for x in permutations(indexed_bcd)), key=sum)


# @example(32, 1, 3, 4, 5)
@given(
    exact_change=st.integers(0, 100),
    a=st.integers(1, 1),
    b=st.integers(1, 100),
    c=st.integers(1, 100),
    d=st.integers(1, 100),
)
def test_bruteforce_greedy(exact_change, a, b, c, d):
    assert a == 1
    a, b, c, d = sorted((a, b, c, d))
    denom = (a, b, c, d)

    def compute_na_nb(nc, nd):
        # optimal when nb is maximal
        rest = exact_change - nc * c - nd * d
        nb = rest // b
        na = rest % b
        assert exact_change == na * a + nb * b + nc * c + nd * d
        return na, nb, nc, nd

    # min(..., key=sum) == argmin_x(sum(x) for x in ...)
    brute = min(
        (
            compute_na_nb(nc, nd)
            for nc in range(100)
            for nd in range(100)
            if exact_change >= nc * c + nd * d
        ),
        key=sum,
    )
    ### star notation flattens arguments: *denom -> a, b, c, d
    # greedy = compute_greedy(exact_change, *denom)
    greedy = compute_greedy_perm(exact_change, *denom)
    msg = f"\n\n{exact_change=} {denom=} {brute=} {greedy=}\n"
    assert sum(brute) == sum(greedy), msg
