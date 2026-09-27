import threading
from socket import *

Host='127.0.0.1'
Port=23494

Fixed_Server_Address = (Host,Port)
def client_main():
    with socket(AF_INET, SOCK_STREAM) as client_socket:
        client_socket.connect(Fixed_Server_Address)
        print("Connected to server:", client_socket.getpeername())

        message ='Hey there'
        client_socket.sendall(message.encode())

        server_data = client_socket.recv(1024)
        print(f'{server_data}')

    client_socket.close()


if __name__ =="__main__":
    client_main()