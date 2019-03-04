import socket
import sys
import time
from threading import Thread

class RecvThread(Thread):

    def __init__(self,c,ip, port):
        Thread.__init__(self)
        self.c = c
        self.ip = ip
        self.port = port
        print("Socket thread created for client.."+ip+" port: "+str(port))

    def run(self):
        while True:
            rdata = self.c.recv(1024).decode("ascii")
            print("[+]Client: "+rdata)

class SendingThread(Thread):

    def __init__(self,c,ip, port):
        Thread.__init__(self)
        self.c = c
        self.ip = ip
        self.port = port
        print("Socket thread created for sending data to client.."+ip+" port: "+str(port))

    def run(self):
        print("hi")
        while True:
            sdata = input()
            self.c.send(sdata.encode())

def create():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as e:
        print("Socket not created properly"+str(e))
        sys.exit()
    var = sys.argv[1]

    port = int(var)

    s.bind(("",port))
    s.listen(5)
    c, addr = s.accept()
    print("Welcome to alpha-chat")
    ip = str(addr)
    ip = ip[2:11]
    print("Connection from:"+ip)
    auth(c,ip,port)

def auth(c,ip,port):
    # c.send("Enter Username:".encode())
    usr = c.recv(10).decode("ascii")
    print(usr)
    # c.send("Enter Password:".encode())
    psd = c.recv(10).decode("ascii")
    print(psd)
    valid(usr, psd, c,ip,port)

def valid(u, p, c,ip,port):
    if u == "admin" and p == "admin":
        conn(c,ip,port)
    else:
        c.send("Server: Wrong Username/Password".encode())
        c.close()

def conn(c,ip,port):
    print("Server: Successfully Validated\n")
    newCT = RecvThread(c,ip,port)
    newCT.start()
    newST = SendingThread(c,ip,port)
    newST.start()

    # while True:
    #     data = input("Server: ")
    #     data = "Server: " + data + "\n" + "Client: "
    #     c.send(data.encode())
    #     msg_rev=c.recv(10).decode("ascii")[:-1]
    #     msg_rev = "Client: " + msg_rev
    #     print(msg_rev)
if __name__ == "__main__":
    create()
