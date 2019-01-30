import socket

s = socket.socket()
print "socket done"
port = 4545

s.bind(('127.0.0.1', port))
print "listening on port: "+str(port)

s.listen(4)
print "listening"

#s.connect((address, port))
c, address = s.accept() #c is client
while True:

    print "got a connection from"+str(address)

    c.send("i got ur connection")
    data = c.recv(1024).decode("ascii")[:-1]
    print data
    #c.close()
    #c.open()
    #c.recv(1024)

#
