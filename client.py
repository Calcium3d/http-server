import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 3000
ip = '127.0.0.1'

s.connect((ip, port))

s.send("lmao lmao \n".encode('ascii'))
print(s.recv(4096).decode('ascii'))

s.close()
