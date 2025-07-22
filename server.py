from socket import *

def connect_client():
    while True:
        client_socket,client_address = server.accept()
        client_socket.send(b"Send your Name!")
        client_msg = client_socket.recv(BUFFER_SIZE).decode()
        clients_sockets.append(client_socket)
        clients_names.append(client_msg)
        client_socket.send(f"{client_msg}, Congrats you're connected the the server!".encode(ENCODE_DECODER))

def broad_cast(msg):
    pass

def receive_msg(client_socket):
    pass

# -- Constants -- #
HOST_IP = gethostbyname(gethostname())
HOST_PORT = 12345
ENCODE_DECODER = "utf-8"
BUFFER_SIZE = 1024

# -- Clients Info -- #
clients_names = list()
clients_sockets = list()

# -- Creating and Setting up Server -- #
server = socket(AF_INET,SOCK_STREAM)
server.bind((HOST_IP,HOST_PORT))

server.listen()
print("Server Listening.....")

connect_client()