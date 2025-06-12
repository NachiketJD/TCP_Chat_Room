import threading
import socket

alias = input('Chhose an alias>>')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59000))

def client_recieve():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')# 1024 is the buffer size
            if message == 'alias?':
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            print('An error occurred')
            break