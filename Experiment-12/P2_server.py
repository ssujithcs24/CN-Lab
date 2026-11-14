import socket
import os
HOST = '127.0.0.1' # localhost
PORT = 65432 # arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server listening on {HOST}:{PORT}")
    
    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")
        filename = conn.recv(1024).decode()
        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                content = f.read()
            conn.sendall(content.encode())
        else:
            conn.sendall(b"File not found.")