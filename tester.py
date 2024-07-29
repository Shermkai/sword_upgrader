import zmq
import subprocess

# Run microservices in background
subprocess.Popen(["python", "sword_upgrader.py"])

# Set up ZeroMQ to communicate between files
context = zmq.Context()  # Set up environment to create sockets
socket = context.socket(zmq.REQ)  # Create request socket
socket.connect("tcp://localhost:5555")

socket.send_string("49")
message = socket.recv().decode()
print(message + "\n")

socket.send_string("50")
message = socket.recv().decode()
print(message + "\n")

socket.send_string("75")
message = socket.recv().decode()
print(message + "\n")

socket.send_string("-25")
message = socket.recv().decode()
print(message + "\n")

socket.send_string("text")
message = socket.recv().decode()
print(message + "\n")

socket.send_string('Q')
