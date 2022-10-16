import socket
import select
from _thread import *



# socket server

host = '0.0.0.0'
port = 1233
clients = []


def client_handler(connection,inclients):
    connection.send(str.encode('connected to server'))
    # do this https://stackoverflow.com/questions/17386487/python-detect-when-a-socket-disconnects-for-any-reason
    while True:
        try:
            ready_to_read, ready_to_write, in_error = select.select([connection,], [connection,], [], 5)
        except select.error as e:
            print(e)
            inclients.remove(connection)
            break
        try:
            data = connection.recv(2048)
            message = data.decode()
            print(data)
            for c in inclients : 
                print(c)
                c.sendall(data)
        except socket.error as e:
            # TODO unify client and connection wording
            # remove client from broadcast list
            # this is catching target but not camera
            print(e)
            inclients.remove(connection)
            break

def accept_connections(ServerSocket):
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    data = Client.recv(2048)
    clients.append(Client)
    start_new_thread(client_handler, (Client, clients))

def start_server(host, port):
    ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
        # TODO port busy. Wait and repeat
    print(f'Server is listing on port {port}...')
    ServerSocket.listen()

    while True:
        accept_connections(ServerSocket)

print("trying to start socket server right now..")
start_server(host, port)
