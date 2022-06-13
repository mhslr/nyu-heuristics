from pprint import pprint
import zmq
import time
import random


happy_bot = [
    "Why aren't you cheering louder?",
    "Aren't you proud of me?",
    "Damn I'm good, and I don't even have a brain!",
]
sad_bot = [
    "I'm doing my best, okay?",
    "And do you think you could do any better?",
    "I feel like it's me doing all the work, you're just chilling in your chair",
    "If I lose this it's your fault not mine... I'm doing EXACTLY what you told me to do!",
]


def show_done_msg(my_name, winner):
    if my_name == winner:
        print(f"Congrats {winner}, you won!")
    else:
        print(f"Too bad, you lost to {winner}.")


def show_pre_bid_msg(info):
    if info["history"]:
        last = info["history"][-1]
        print("auction won by %s at $%d" % (last["player"], last["bid"]))
        print()
    else:
        print("Let's go!")
        print()


def show_post_bid_msg(info, bid):
    rd = info["cur_round"]
    item = info["items"][rd]
    print(f"round {rd}: bidding ${bid} for a {item}")


def play(my_name, server_url, strategy):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(server_url)
    while True:
        # send info request
        request = {"type": "info", "name": my_name}
        socket.send_json(request)
        response = socket.recv_json()

        if response["type"] == "info":
            # we recieved the latest info, we should compute and place our bid
            info = response.copy()
            show_pre_bid_msg(info)
            bid = int(strategy(info))
            show_post_bid_msg(info, bid)

            bid_request = {"type": "bid", "name": my_name, "bid": bid}
            socket.send_json(bid_request)
            bid_response = socket.recv_json()
            # check that there was no error
            assert bid_response["type"] == "bid"

        elif response["type"] == "wait":
            time.sleep(0.1)

        elif response["type"] == "done":
            show_done_msg(my_name, response["winner"])
            return

        else:
            print("ERROR:", response)
