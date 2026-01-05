import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5555))
server.listen()

clients = []

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)

def handle_client(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg, client)
        except:
            clients.remove(client)
            client.close()
            break

print("Server started...")
while True:
    client, addr = server.accept()
    print("Connected:", addr)
    clients.append(client)
    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()
