import socket
import os

HOST = "127.0.0.1" # localhost
PORT = 5005

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind((HOST, PORT))
print(f"UDP Server listening on {HOST}:{PORT}")

while True:
    filename, client_addr = server_socket.recvfrom(1024)
    filename = filename.decode()
    
    print(f"Client requested file: {filename}")
    
    if os.path.isfile(filename):
        with open(filename, "r") as f:
            data = f.read()
        server_socket.sendto(data.encode(), client_addr)
    else:
        server_socket.sendto(b"ERROR: File not found", client_addr)