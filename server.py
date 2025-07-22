from socket import *
from threading import *

def connect_clients():
    while True:
        client_socket,client_address = server.accept()
        client_socket.send(b"Send your Name!")
        client_msg = client_socket.recv(BUFFER_SIZE).decode(ENCODE_DECODER).strip()
        clients_sockets.append(client_socket)
        clients_names.append(client_msg)
        broad_cast(f"# --- {client_msg} has joined the chat! --- #") # 3-C -- Broad Cast Message To Every Client of New Connection of Another Client
        client_socket.send(f"{client_msg}, Congrats you're connected the the server!\n".encode(ENCODE_DECODER)) # 4-C Send Welcome Msg to currently connected Client

        rec_msg = Thread(target=receive_msg,args=(client_socket,))
        rec_msg.start()

def broad_cast(msg,sender_socket=None):
    if not msg.startswith("# ---"):
        for client in clients_sockets:
            if client != sender_socket:
                try:
                    client.send(msg.encode(ENCODE_DECODER))
                except:
                    pass
    else:
        for client in clients_sockets:
            if client!=sender_socket:
                try:
                    client.send(f"{msg}\n".encode(ENCODE_DECODER))
                except:
                    pass

def receive_msg(client_socket):
    while True:
        try:
            client_msg = client_socket.recv(BUFFER_SIZE).decode(ENCODE_DECODER).strip()
            if not client_msg:
                break
            broad_cast(client_msg,sender_socket=client_socket)
        except:
            if client_socket in clients_sockets:
                broad_cast(f"# --- {clients_names[clients_sockets.index(client_socket)]} left the chat! --- #")
                clients_names.pop(clients_sockets.index(client_socket))
                clients_sockets.remove(client_socket)
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

connect_clients() #Start The server to receive clients