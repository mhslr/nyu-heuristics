import random

def compute_bid_state(info, prev_state):
    bid = random.random() * info["self"]['budget']
    bid = round(bid)
    next_state = (prev_state or 0) + 1
    return bid, next_state

