import os
import zmq
from datetime import datetime

PORT = 51023

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%d" % PORT)

def answer(msg):
    print(msg)
    if msg["type"] == "hello":
        return {"msg": "hello " + msg["name"]}


print("server ready, listening on port", PORT)
while True:
    msg = socket.recv_json()
    socket.send_json(answer(msg))
