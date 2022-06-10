import zmq

PORT = 51023

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:%d" % PORT)

print("client ready")
import time
for i in range(1000000):
    time.sleep(1)
    socket.send_json({"name": "Matthias", "type": "hello"})
    msg = socket.recv_json()
    print(msg)
