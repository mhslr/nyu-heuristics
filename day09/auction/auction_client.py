from pprint import pprint
import zmq
import time
import random

PORT = 50018
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:%d" % PORT)
# socket.connect("tcp://2.tcp.ngrok.io:17918")
name = input("what's your name? ")
bot = "n" not in input("are you a bot? (Y/n) ").lower()

sample_info = {
    "type": "info",
    "cur_round": 5,
    "item_types": ["Picasso", "Van_Gogh", "Rembrandt", "Da_Vinci"],
    "items": [
        "Rembrandt",
        "Rembrandt",
        "Picasso",
        "Van_Gogh",
        "Rembrandt",
        "Van_Gogh",
        "Van_Gogh",
        "Da_Vinci",
        "Van_Gogh",
        "Picasso",
        "Da_Vinci",
        "Da_Vinci",
    ],
    "self": {
        "budget": 11,
        "item_count": {"Da_Vinci": 0, "Picasso": 0, "Rembrandt": 1, "Van_Gogh": 0},
        "name": "alice",
    },
    "others": [
        {
            "budget": 16,
            "item_count": {"Da_Vinci": 0, "Picasso": 0, "Rembrandt": 2, "Van_Gogh": 0},
            "name": "bob",
        },
        {
            "budget": 21,
            "item_count": {"Da_Vinci": 0, "Picasso": 1, "Rembrandt": 0, "Van_Gogh": 1},
            "name": "charlie",
        },
    ],
}


def compute_bid(info):
    """
    >>> compute_bid(sample_info)
    5
    """
    i = info["cur_round"]
    bid = info["self"]["budget"] * random.random()
    print(f"bidding ${bid} for a", info["items"][i])
    return round(bid)


def ask_bid(info):
    """
    >>> ask_bid(sample_info)
    5
    """
    rd = info["cur_round"]
    info["items"] = info["items"][rd : rd + 10]  # too long to print
    pprint(info)
    return int(input("place your bid (integer): "))


def done_msg(player, winner):
    if player == winner:
        return f"Congrats {player}, you won!"
    else:
        return f"Too bad, you lost to {winner}."


while True:
    request = {"type": "info", "name": name}
    socket.send_json(request)
    response = socket.recv_json()

    if response["type"] == "info":
        info = response.copy()
        # we recieved the latest info, we can compute and place our bid
        if bot:
            bid = int(compute_bid(info))
        else:
            bid = ask_bid(info)

        bid_request = {"type": "bid", "name": name, "bid": bid}
        socket.send_json(bid_request)
        bid_response = socket.recv_json()
        # check that there was no error
        assert bid_response["type"] == "bid"

    elif response["type"] == "wait":
        time.sleep(0.1)

    elif response["type"] == "done":
        print(done_msg(name, response["winner"]))
        break

    else:
        print("ERROR: unrecognized type", response)
