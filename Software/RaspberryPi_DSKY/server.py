import socket
import select
import pickle

HEADER_LENGTH = 10

IP = "192.168.178.82"
PORT = 1234

# https://pythonprogramming.net/server-chatroom-sockets-tutorial-python-3/

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen()

sockets_list = [server_socket]
clients = {}

HEADERSIZE = 10

print(f'Listening for connections on {IP}:{PORT}...')

