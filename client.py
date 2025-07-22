from socket import *

def send_msg():
    msg = input("Enter your Message Client: ").encode(ENCODE_DECODER)
    client.send(msg)

def receive_msg():
    try:
        msg_recv = client.recv(BUFFER_SIZE).decode(ENCODE_DECODER)
        print(f"Server: {msg_recv}") if (msg_recv.__len__()) else None
    except:
        return


# -- Constants -- #
DES_IP = gethostbyname(gethostname())
DES_PORT = 12345
ENCODE_DECODER = "utf-8"
BUFFER_SIZE = 1024

# -- Creating and Setting up Server -- #
client = socket(AF_INET,SOCK_STREAM)
client.connect((DES_IP,DES_PORT))

while True:
    receive_msg()
    send_msg()