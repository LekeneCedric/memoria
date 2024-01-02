import socket
import _thread
import app.protocol
from app.database import Database
from app.action import Action


def respond(client_socket: socket, db: Database):
        while True:
            data = client_socket.recv(512)

            if not data:
                break

            response = app.protocol.deserialize_message(data)

            result = None

            if response["action"] == Action.MESSAGE:
                print(response)
                result = response["message"]

            if response["action"] == Action.GET:
                print(response)
                key = response["key"]
                result = db.get(key)

            if response["action"] == Action.SET:
                print(response)
                db.set(response["key"], response["value"])
                result = response["message"]

            if response["error"] == True:
                result = app.protocol.serialized_error_message(result)
            if response["error"] == False:
                result = app.protocol.serialize_simple_string(result)
                
            client_socket.sendall(result)

        client_socket.close()

def main():

    db = Database({})

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)

    while True:
        try:
            client_socket , address = server_socket.accept()
            _thread.start_new_thread(respond, (client_socket, db,))
        except KeyboardInterrupt:
            server_socket.close()



if __name__ == "__main__":
    main()
