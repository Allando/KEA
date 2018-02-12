import socket


HOST = "127.0.0.1"
PORT = 8888
BUFF = 1024

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (HOST, PORT)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    # Send data
    message = "f83ba57450ed0fd8ac9a472b847e830e"
    print('sending "%s"' % message)
    sock.sendall(message.encode())

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(1024)
        amount_received += len(data)
        print('received "%s"' % data)

finally:
    print('closing socket')
    sock.close()

