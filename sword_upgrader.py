import zmq


def coin_checker(coins):
    """Checks if there are enough coins to afford a sword and deducts the cost if so.
    Returns the remaining amount of coins."""

    if coins >= 50:
        return coins - 50

    return coins


# Set up ZeroMQ
context = zmq.Context()           # Set up environment to create sockets
socket = context.socket(zmq.REP)  # Create reply socket
socket.bind("tcp://*:5555")       # This is where the socket will listen on the network port

while True:
    message = socket.recv().decode()           # Message from client
    print(f"Received from client: {message}")  # Debug text. Can be safely removed.

    if len(message) > 0:
        if message == 'Q':
            socket.send_string("Closed")
            break

        # If we receive a number, call the above function
        if message.isdigit():
            remaining_coins = coin_checker(int(message))
            if remaining_coins != int(message):  # If the coin count changed, a sword is purchasable
                socket.send_string("(True, " + str(remaining_coins) + ")")
            else:  # If the coin count is the same, a sword is not purchasable
                socket.send_string("(False, " + str(remaining_coins) + ")")

        # If we receive anything other than a number, a sword is not purchasable.
        # The '-1' is there to illustrate that invalid input was entered.
        else:
            socket.send_string("(False, -1)")

context.destroy()
