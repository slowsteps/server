import socket

# HOST = "https://surftracker-365018.ew.r.appspot.com"  # The server's hostname or IP address
HOST = "0.0.0.0"
PORT = 1233  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"camera")
    while True :
        data = s.recv(1024)
        # if data: print(f"Received {data!r}")
        if data: print(data.decode())
    s.close()
