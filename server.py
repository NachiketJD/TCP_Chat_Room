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
            broadcast(f'{alias} left the chat!'.encode()) #encode is used to convert the string into bytes
            aliases.remove(alias)
            break

#Main function to recieve the clients connection

def receive():
    while True:
        print('Server is running and listening for incoming connections...')
        client, address = s.accept() # accept() is a blocking call, it will wait until a client connects to the server, it returns a new socket object representing the connection and the address of the client.
        print(f'connection is established with {str(address)}') #str() is used to convert the address into a string since address is an integer form
        client.send('alias?'.encode('utf-8'))
         #here, we are sending a message to the client asking for an alias. the encode() function is used to convert the string into bytes this is done to send the message over the network it is a requirement for the socket library.
         #The 'utf-8' is the encoding type, it is the most common encoding type used in the world. It can encode all the characters in the Unicode character set. It is a variable-length encoding, which means that it can encode characters in a single byte or in multiple bytes.
         #It is a good choice for encoding text data because it is efficient and can encode all the characters in the Unicode character set.
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client) 
        print(f'alias is {alias}'.encode('utf-8'))
        client.send('You are nw Connecte'.encode('utf-8'))
        