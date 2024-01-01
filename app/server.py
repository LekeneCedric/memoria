import socket
from app.protocol import deserialize_message

def respond(client_socket: socket):
        while True:
            data = client_socket.recv(512)

            if not data:
                break

            decoded_data = data.decode()
            response = deserialize_message(decoded_data)
            client_socket.sendall(response)

def main():

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)

    while True:
        client_socket , address = server_socket.accept()
        respond(client_socket)

    client_socket.close()
    server_socket.close()



if __name__ == "__main__":
    main()
