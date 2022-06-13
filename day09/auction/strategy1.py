import random
from client_runner import play
from uuid import uuid4


def compute_bid(info):
    return round(info["self"]["budget"] * random.random())


if __name__ == "__main__":
    my_name = "matt-" + uuid4().hex[:6]
    server = "tcp://localhost:50018"
    print(my_name)
    play(my_name, server, compute_bid)
