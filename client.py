import threading
import socket

alias = input('Chhose an alias>>')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59000))