import os
import zmq
from datetime import datetime

PORT = 51023

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%d" % PORT)

def answer(msg):
    """
    should respond whether the name is
    - too short <4
    - too long >10 or
    - the right size 
    >>> answer({"type": "hello", "name": "Matthias"})
    {"status": "ok", "msg": "cool, this name is of the right length"}
    """
    print(msg)
    if msg["type"] == "hello":
        return {"msg": "hello " + msg["name"]}


print("server ready, listening on port", PORT)
while True:
    msg = socket.recv_json()
    socket.send_json(answer(msg))
