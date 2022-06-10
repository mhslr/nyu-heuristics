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
    name = msg["name"]
    if len(name) < 4:
        return {"status": "error", "msg": "badbad, too short"}
    if len(name) > 10:
        return {"status": "error", "msg": "badbad, too long"}
    # otherwise we know 4 <= len(name) <= 10
    return {"status": "ok", "msg": "cool, this name is of the right length"}



print("server ready, listening on port", PORT)
while True:
    request_msg = socket.recv_json()
    answer_msg = answer(request_msg)
    socket.send_json(answer_msg)
