## Sword Upgrader

### Requesting Data

First, make sure the main and sword_upgrader processes are running

#### Main Program Request Example
```
context = zmq.Context()                 # Set up environment to create sockets
socket = context.socket(zmq.REQ)        # Create request socket
socket.connect("tcp://localhost:5555")  # Connect to the respective network port

socket.send_string(coin_count)  # Send a coin amount to the microservice
```

#### Main Program Receive Example
```
message = socket.recv()  # Receive the string that is returned from the microservice
print(message.decode())  # Print the string by decoding the message
```

#### Terminating the Microservice
```
socket.send_string('Q')  # This breaks the microservice loop and destroys the context
```

### UML Sequence Diagram
![UML_Diagram](https://github.com/user-attachments/assets/a44869db-496b-4ced-9753-7f4ff7d17323)
