import socket 

s = socket.socket()
print("Socket created")

port = 3000

s.bind(('', port))

s.listen(5)
print("socket is listening")

while True:
    client, address = s.accept()
    print("Got a connection from: ", address)

    client.send(b'thanks for connecting')

    client.close

