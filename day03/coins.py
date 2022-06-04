"""
Assignment: 
You are in charge of designing the denominations of coins.
However, we're going to do this for old English pounds which were worth 240 pence.
You have made a study of the subpound prices and have determined that each multiple
of 5 cents price is N times as likely as a non-multiple of 5 pence.
For example, if N = 4, then 15 pence is four times as likely to be the price as 43 pence.
But any 5 pence multiple is equally likely as any other 5 pence multiple
and ditto for the non-5 pence multiples.
The N will be given in class and your programs will have 2 minutes
to solve the following problem:
(N will be 1 or greater but may not be an integer.)

Your first job is to design a set of 4 coin denominations such that
the expected number of coins required to give
exact change for a purchase is minimized given these constraints.
This is called the Exact Change Number.
Using the U.S. denominations, the Exact Change Number for
43 pence can be realized by one quarter, one dime, one nickel,
and three pennies, thus giving a total of 6.
"""

from functools import lru_cache

tqdm = list
## to see a pretty progressbar, you need to install tqdm
## by running
## python -m pip install tqdm
## then, uncomment the line below
# from tqdm import tqdm


# Task 1: Computing best exact change

## sol 1: greedy, incorrect
def change_greedy(total, denos):
    # denos: coins values, increasing
    coins = []  # how many coins of each denomination
    tot_coins = 0  # total number of coins

    for value in denos[::-1]:  # decreasing order
        k = total // value
        total = total % value  # = total - k * value
        coins.append(k)
        tot_coins += k
    coins = coins[::-1]  # reversed

    # assert total == 0  # exact change
    # assert tot_coins == sum(coins)

    return tot_coins


## sol 2: recursive, correct but slow
infty = 1000000


def change_recursive(total, denos):
    if denos == (1,):
        return total

    ans = infty  # default answer: not possible
    value = denos[-1]
    for k in range(total // value + 1):
        # compute remainder
        rem_total = total - value * k
        rem_denos = denos[:-1]

        rest = change_recursive(rem_total, rem_denos)
        ans = min(ans, k + rest)

    return ans


## sol 3: efficient, dynamic programming
def change_dp(max_total, denos):
    ans = [infty] * (max_total + 1)  # ans[0]=infty .. ans[max_tot]=infty
    ans[0] = 0
    for tot in range(1, max_total + 1):
        for den in denos:
            if den <= tot:
                # add 1 den coin
                ans[tot] = min(ans[tot], ans[tot - den] + 1)
    # return ans[max_total]
    return ans


# Given number of required coins, computes the score
def score(req_coins, N):
    req_coins_5k = req_coins[::5]
    num = sum(req_coins) + (N - 1) * sum(req_coins_5k)
    den = len(req_coins) + (N - 1) * len(req_coins_5k)
    return num / den


# Expected nb of coins for a given set of denominations
# over change amounts in range 0..max_change-1
def expected_ncoins(max_change, N, denos, method="greedy"):
    if method == "greedy":
        req_coins = []
        # req_coins[change] = min nb of coins to get change
        for change in range(max_change):
            n_coins = change_greedy(change, denos)
            req_coins.append(n_coins)
    elif method == "rec":
        req_coins = []
        # req_coins[change] = min nb of coins to get change
        for change in range(max_change):
            n_coins = change_recursive(change, denos)
            req_coins.append(n_coins)
    else:  #  method == 'dp':
        req_coins = change_dp(max_change, denos)

    return score(req_coins, N)


# find the best set of coins
def solve(max_change, N, method):
    best_score = infty
    best_denos = None
    c1 = 1
    # for c2 in range(c1+1, max_change+1):
    for c2 in tqdm(range(c1 + 1, max_change)):
        for c3 in range(c2 + 1, max_change):
            for c4 in range(c3 + 1, max_change):
                denos = (c1, c2, c3, c4)
                new_score = expected_ncoins(max_change, N, denos, method)
                # print(denos, new_score)
                if new_score < best_score:
                    best_score = new_score
                    best_denos = denos
    print(best_score, best_denos, method)
    return (best_score, best_denos)


# without cache
solve(60, 5, "rec")
# w/o cache: 10s
# lru_cache: 3s
solve(100, 5, "rec")
# w/o cache: 1:36
# lru_cache: 44s

solve(60, 5, "dp")  # took 1s
solve(100, 5, "greedy")  # took 12s
solve(100, 5, "dp")  # took 10s

solve(240, 5, "greedy")  # took 8:00
solve(240, 5, "dp")  # took 6:00
