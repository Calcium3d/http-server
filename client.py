import socket

s = socket.socket()

port = 3000
ip = '127.0.0.1'

s.connect((ip, port))

print(s.recv(1024))

s.close()
