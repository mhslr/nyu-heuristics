# From http://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/client_server.html

import zmq
import sys

port = "51023"


context = zmq.Context()
print("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:%s" % port)

#  Do 10 requests, waiting each time for a response
for request in range(1, 10):
    print("Sending request " + str(request) + "...")
    socket.send(b"Hello")
    #  Get the reply.
    message = socket.recv()
    messagestr = message.decode("utf-8")  # creates a string from bytes
    print("Received reply " + str(request) + "[" + messagestr + "]")
