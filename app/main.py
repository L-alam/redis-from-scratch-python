import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment the code below to pass the first stage
    #
    
    # TCP server that listens on port 6379. Just like redis
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    connection, client_address = server_socket.accept()
    connection.send(bytes("+PONG\r\n", "utf-8"))


    


if __name__ == "__main__":
    main()
