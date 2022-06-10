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
    name = input("whats your name? ")
    request_msg = {"name": name, "type": "hello"}
    socket.send_json(request_msg)
    answer_msg = socket.recv_json()
    print(answer_msg)
    if answer_msg["status"] == "ok":
        print("good")
        break
    else:
        print("give it another shot")
