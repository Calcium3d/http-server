import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

port = 3000

s.bind(('', port))

s.listen(5)
print("socket is listening")

dictionary = {
    "aim": "to direct at something"
}
found = False
while True:
    client, address = s.accept()
    print("Got a connection from: ", address)
    enter = client.recv(4096).decode('ascii')

    enter = enter.split()

    if enter[0] == "GET":
        for word in dictionary:
            if word == enter[1]:
                client.send((dictionary.get("aim")).encode('ascii'))
                found = True
            else:
                found = False

        if not found:
            client.send("Word not found".encode('ascii'))

    

    client.close()

