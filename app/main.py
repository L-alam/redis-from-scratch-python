import socket  # noqa: F401
import asyncio


async def main():
    # You can use print statements as folloc v cws for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")
        
    # TCP server that listens on port 6379. Just like redis
    # server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    # connection, client_address = server_socket.accept()
    
    
    server = await asyncio.start_server(handle_echo, "localhost", 6379)
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

    
async def handle_echo(reader, writer):
    while not writer.is_closing():
        data = await reader.read(100)
        if not data:
            break
        writer.write(b"+PONG\r\n")
        await writer.drain()
    writer.close()
    await writer.wait_closed()
    

if __name__ == "__main__":
    asyncio.run(main())
