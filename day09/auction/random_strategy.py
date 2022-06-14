import random
from copy import deepcopy

# how to convert from glob vars to prev/next_state

# our glob vars here
want = None
b = 1
c = 1
d = 1
e = 1

# first put them together
init_state = a, b, c, d, e

# for concurrent runs, dont use global state
def compute_bid_state(info, prev_state=None):
    if prev_state is None:
        prev_state = deepcopy(init_state)
        want, b, c, d, e = prev_state
        # on the first round, commit to one
        want = info['items'][0]
    else:
        # retrieve our glob vars
        want, b, c, d, e = prev_state

    rd = info['cur_round']

    # only bid if it is the right one
    if info['items'][rd] == want:
        bid = random.random() * info['self']['budget']
    else:
        bid = 0

    # put them back in next_state
    next_state = want, b, c, d, e
    return bid, next_state
