import logging
import socket
from _thread import *

# host = '127.0.0.1'
host = '0.0.0.0'
port = 1233
clients = []


def client_handler(connection,inclients):
    connection.send(str.encode('connected to server'))
    while True:
        data = connection.recv(2048)
        message = data.decode()
        for c in inclients : c.sendall(data)
    connection.close()

def accept_connections(ServerSocket):
    Client, address = ServerSocket.accept()
    logger.debug('Connected to: ' + address[0] + ':' + str(address[1]))
    data = Client.recv(2048)
    clients.append(Client)
    start_new_thread(client_handler, (Client, clients))

def start_server(host, port):
    ServerSocket = socket.socket()
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        logger.debug(str(e))
    logger.debug(f'Server is listing on port {port}...')
    ServerSocket.listen()

    while True:
        accept_connections(ServerSocket)



logging.basicConfig(filename="newfile.log",format='%(asctime)s %(message)s',filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

start_server(host, port)