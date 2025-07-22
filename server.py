from socket import *
from threading import *

def connect_client():
    while True:
        client_socket,client_address = server.accept()
        client_socket.send(b"Send your Name!")
        client_msg = client_socket.recv(BUFFER_SIZE).decode(ENCODE_DECODER)
        clients_sockets.append(client_socket)
        clients_names.append(client_msg)
        client_socket.send(f"{client_msg}, Congrats you're connected the the server!".encode(ENCODE_DECODER))
        broad_cast(f"# --- {client_msg} has joined the chat! --- #")

        rec_msg = Thread(target=receive_msg,args=(client_socket,))
        rec_msg.start()

def broad_cast(msg,*args):
    for client in clients_sockets:
        client_nam = clients_names[clients_sockets.index(client)]
        client.send(f"{client_nam}: {msg}")

def receive_msg(client_socket):
    try:
        client_msg = client_socket.recv(BUFFER_SIZE).decode(ENCODE_DECODER)
        broad_cast(client_msg)
    except:
        broad_cast(f"# --- {clients_names[clients_sockets.index(client_socket)]} left the chat! --- #")
        clients_sockets.remove(client_socket)
        clients_names.pop(clients_sockets.index(client_socket))
        client_socket.close()

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

while True:
    connect_client()