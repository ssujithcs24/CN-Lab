import socket

HOST = "127.0.0.1"
PORT = 5005

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

filename = input("Enter filename to request: ")
client_socket.sendto(filename.encode(), (HOST, PORT))

data, _ = client_socket.recvfrom(4096)
print("\n--- File Content ---")
print(data.decode())

client_socket.close() 