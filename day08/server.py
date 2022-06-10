import os
import zmq
from datetime import datetime

PORT = 51023

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%d" % PORT)

users = {}


def user_fsm():
    ans = None
    while True:
        msg = yield ans


def answer(msg):
    if "name" not in msg:
        return {"status": "ERROR", "detail": "missing name field"}
    name = msg["name"]
    if name not in users:
        g = user_fsm()
        next(g)
        users[name] = {"last": 0, "msg_count": 0}
    users[name]["last"] = str(datetime.now())
    users[name]["msg_count"] += 1
    if "type" not in msg:
        return {"status": "ERROR", "detail": "missing type field"}
    if msg["type"] == "hello":
        return {"status": "OK", "msg": "Hello " + name}
    if msg["type"] == "play":
        return {"status": "OK", "msg": "Hello " + name}


def show_status():
    os.system("clear")
    print("name        msg_count")
    for user, state in users.items():
        cnt = state["msg_count"]
        print(f"{user:12s}{cnt:9d}")



print("server ready, listening on port", PORT)
while False:
    msg = socket.recv_json()
    socket.send_json(answer(msg))
    show_status()
