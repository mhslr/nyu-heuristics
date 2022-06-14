import random
from client_runner import play
from uuid import uuid4


# for concurrent runs, dont use global state
def compute_bid_state(info, prev_state=None):
    if prev_state is None:
        prev_state = 0
    next_state = prev_state + 1
    bid = 0
    return bid, next_state


# memorize state between rounds
store = None


def compute_bid(info):
    global store
    if info["cur_round"] == 0:
        # first round, we init the store
        store = {}
        store["mysecret"] = 3
    # update store
    store["mysecret"] += 1
    return round(info["self"]["budget"] * random.random())


if __name__ == "__main__":
    my_name = "matt-" + uuid4().hex[:6]
    server = "tcp://localhost:50018"
    print(my_name)
    play(my_name, server, compute_bid)
