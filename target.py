import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 1233  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"target")
    while True:
        str = input("-->")
        s.sendall(str.encode())
    s.close()
