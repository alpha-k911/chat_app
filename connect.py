import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = int(sys.argv[1])
s.connect(('127.0.0.1',port))
s.send("hi".encode())
