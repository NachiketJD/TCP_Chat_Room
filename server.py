import threading
import sys
import socket
host = '127.0.0.1'
port = 59000
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()

clients =[]
aliases=[]

def broadcast(message):
    for client in clients:
        client.send(message)
    
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client) #index method, searches for a specified value in our case, the index and returns it index
            clients.remove(client)
            client.close()
            alias= aliases[index]
            broadcast(f'{alias} left the chat!'.encode())
            aliases.remove(alias)
