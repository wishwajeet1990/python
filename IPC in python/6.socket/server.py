import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to an address (IP, port)
server_socket.bind(('localhost', 9000))
server_socket.listen(1)

print("Server listening on port 12345...")

# Accept client connection
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data or data.lower() == "quit":
        print("Client disconnected.")
        break
    print("Client says:", data)
    reply = input("Server reply: ")
    conn.send(reply.encode())

conn.close()
