import math
import random


def simulate_walk(desired_walk, p_flip):
    """
    returns whether we reached E
    >>> simulate_walk([-1, 1, -1, 1], 0.1)
    True
    """
    n = len(desired_walk)
    pos = [0] + [None] * n
    for i in range(n):
        rd = random.random()  # uniform over [0,1)
        step = (-1 if rd < p_flip else 1) * desired_walk[i]
        pos[i + 1] = pos[i] + step
    last = pos[n]
    outcome = last == 0
    return outcome


def get_prob_E(desired_walk, p_flip, n_samples):
    """
    want to get the prob of getting to E,
    starting from S
    after talking the steps of desired_walk
    and prob of flip p_flip: (step[i] or -step[i])
    >>> get_prob_E([-1, 1, -1, 1], 0.1, 5000)
    0.9
    """
    outcomes = [simulate_walk(desired_walk, p_flip) for i in range(n_samples)]
    return sum(outcomes) / len(outcomes)


def math_prob_E(desired_walk, p_flip):
    steps = len(desired_walk)
    assert steps % 2 == 0  # has to be even
    # goal is to make obj steps in each dir
    obj = steps // 2
    pos = sum(s > 0 for s in desired_walk)
    neg = steps - pos
    # true positive + flipped negatives = obj
    ans = 0
    p1 = 1 - p_flip
    p2 = p_flip
    for Tpos in range(pos + 1):  # 0 .. pos
        Fpos = pos - Tpos
        Fneg = obj - Tpos  # they must sum to obj
        Tneg = neg - Fneg
        if 0 <= Fneg <= neg:
            ans = ans + (
                p1 ** (Tpos + Tneg)
                * p2 ** (Fpos + Fneg)
                * math.comb(pos, Tpos)
                * math.comb(neg, Tneg)
            )
    return ans


p_flip = 0.1
print(" sim_prob_E 2 2", get_prob_E([1, 1, -1, -1], p_flip, 100000))
print("math_prob_E 2 2", math_prob_E([1, 1, -1, -1], p_flip))
print(" sim_prob_E 3 1", get_prob_E([1, 1, 1, -1], p_flip, 100000))
print("math_prob_E 3 1", math_prob_E([1, 1, 1, -1], p_flip))
print(" sim_prob_E 4 0", get_prob_E([1, 1, 1, 1], p_flip, 100000))
print("math_prob_E 4 0", math_prob_E([1, 1, 1, 1], p_flip))


def interactive_walk(n_steps, p_flip):
    """
    returns whether we reached E
    our algorithm will try to steer back to middle
    >>> interactive_walk(4, 0.1)
    True
    """
    pos = 0
    for i in range(n_steps):
        intent = +1 if pos < 0 else -1
        rd = random.random()
        step = (-1 if rd < p_flip else 1) * intent
        pos = pos + step
    outcome = pos == 0
    return outcome


def get_prob_interactive(n_steps, p_flip, n_samples):
    """
    want to get the prob of getting to E,
    starting from S
    after talking the steps of desired_walk
    and prob p_flip: (step[i] or -step[i])
    >>> get_prob_interactive(4, 0.1, 5000)
    0.9
    """
    outcomes = [interactive_walk(n_steps, p_flip) for i in range(n_samples)]
    return sum(outcomes) / len(outcomes)


def math_prob_interactive(n_steps, pos, p_flip):
    """
    returns expected score
    - n_steps remaining
    - start offset: pos
    """
    if n_steps == 0:
        return float(pos == 0)
    lscore = math_prob_interactive(n_steps - 1, pos - 1, p_flip)
    rscore = math_prob_interactive(n_steps - 1, pos + 1, p_flip)
    return max(
        (1 - p_flip) * lscore + p_flip * rscore,
        (1 - p_flip) * rscore + p_flip * lscore
    )


print()
print('interact sim: ', get_prob_interactive(4, p_flip, 100000))
print('interact math:', math_prob_interactive(4, 0, p_flip))
