import socket
import threading

HEADER = 64
FORMAT = "utf-8"

PORT = 12345
SERVER = "0.0.0.0"   # listen on all interfaces
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = [];#List to keep track of connected clients, so we can broadcast messages to all clients if needed
def broadcast(message):
    for client in clients:
        try:
            msg_length = str(len(message)).encode(FORMAT)
            msg_length += b' ' * (HEADER - len(msg_length))

            client.sendall(msg_length)
            client.sendall(message)
        except:
            clients.remove(client)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    clients.append(conn)

    connected = True
    while connected:
        try:
            msg_length = conn.recv(HEADER).decode(FORMAT)

            if msg_length:
                msg_length = int(msg_length.strip())
                msg = conn.recv(msg_length).decode(FORMAT)
                broadcast(msg.encode(FORMAT))
            else:
                connected = False

        except (ConnectionResetError, ConnectionAbortedError):
            connected = False

    print(f"[DISCONNECTED] {addr} disconnected.")

    if conn in clients:
        clients.remove(conn)

    conn.close()

def start():
    server.listen();
    print(f"[LISTENING] Server is listening on {SERVER}:{PORT}");
    while True:
        conn, addr = server.accept(); #blocking call, waits until a client connects
        thread = threading.Thread(target=handle_client, args=(conn, addr));
        thread.start();
        #print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}");

print("[STARTING] Server is starting...");
start();