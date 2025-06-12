import threading
import sys
import socket
host = '127.0.0.1'
port = 59000
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()