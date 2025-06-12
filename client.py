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

def clinet_send():
    while True:
        message = f'{alias}: {input("")}'    # get message from user and send it to server 
        client.send(message.encode('utf-8')) #this line, sends the message to the server and the server will send it to all connected clients this is done using the broadcast function in the server side 
        