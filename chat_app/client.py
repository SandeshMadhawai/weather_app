import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            client.close()
            break

def send():
    while True:
        msg = input()
        client.send(msg.encode())

threading.Thread(target=receive).start()
threading.Thread(target=send).start()
