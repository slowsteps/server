import socket
import sys

# HOST = "localhost"  # The server's hostname or IP address
# HOST = "34.147.68.23"  # The server's hostname or IP address
HOST = "0.0.0.0"
PORT = 1233  # The port used by the server

print("trying to connect..	")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
    	s.connect((HOST, PORT))
    except:
    	print("unknow host or port")
    	sys.exit()
    s.sendall(b"target")
    while True:
        str = input("-->")
        s.sendall(str.encode())
    s.close()
