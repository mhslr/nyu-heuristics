from pprint import pprint
import zmq
import time
import random
from sample_strat import compute_bid_state

context = zmq.Context()
socket = context.socket(zmq.REQ)
# socket.connect("tcp://localhost:50018")
socket.connect("tcp://4.tcp.ngrok.io:19796")
my_name = input("what's your name? ")


def round_msg(info):
    if info["history"]:
        last = info["history"][-1]
        # print("auction won by %s at $%d" % (last["player"], last["bid"]))


while True:
    request = {"type": "info", "name": my_name}
    socket.send_json(request)
    response = socket.recv_json()

    if response["type"] == "info":
        info = response.copy()
        if info['cur_round'] == 0:
            state = None
        round_msg(info)
        # we recieved the latest info, we can compute and place our bid
        bid, state = compute_bid_state(info, state)
        bid = int(bid)

        bid_request = {"type": "bid", "name": my_name, "bid": bid}
        socket.send_json(bid_request)
        bid_response = socket.recv_json()
        # check that there was no error
        assert bid_response["type"] == "bid"

    elif response["type"] == "wait":
        time.sleep(0.1)

    elif response["type"] == "done":
        print('done', response)
        break

    else:
        print("ERROR:", response)
