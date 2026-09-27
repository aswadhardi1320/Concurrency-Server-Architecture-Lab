import socket
import threading


Host='127.0.0.1'
Port=23494

Fixed_Server_Address = (Host,Port)

def handle_client(client_socket,client_addr):

    print("Client connected from:", client_addr)
    while True:
        client_data = client_socket.recv(1024)
        
        if not client_data:
            break
        print(f'{client_data.decode()}')

        client_socket.send(b'Welcome on board!')
        print('== ENDS ==')



def main():
    with socket.create_server(Fixed_Server_Address) as server:
        print('The server is running!')
        server.listen()

        while True:
            client_socket,client_addr = server.accept()

            print()
            client_thread = threading.Thread(target=handle_client,args=(client_socket,client_addr))
            client_thread.start()
            
        server.close()


if __name__=='__main__':
    main()