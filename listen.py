import socket

s = socket.socket()
print("socket done")
port = 4545

s.bind(('', port))
print("listening on port: "+str(port))

s.listen(10)
print("listening")

while True:
    c, address = s.accept() #c is client
    print("got a connection from"+str(address))

    c.send("i got ur connection")
    c.close()
