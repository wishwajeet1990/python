import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(('localhost', 9000))

while True:
    msg = input("Client: ")
    client_socket.send(msg.encode())
    if msg.lower() == "quit":
        break
    reply = client_socket.recv(1024).decode()
    print("Server says:", reply)

client_socket.close()
