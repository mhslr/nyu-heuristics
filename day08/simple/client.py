import zmq

PORT = 51023

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:%d" % PORT)

print("client ready")
# import time
# time.sleep(1)
while True:
    # pls input name
    input("continue ?")
    msg1 = {"name": "Matthias", "type": "hello"}
    socket.send_json(msg1)
    msg2 = socket.recv_json()
    print(msg2)
