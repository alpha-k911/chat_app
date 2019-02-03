    import socket
    import sys
    import getpass
    from threading import Thread
    import time

    class RecvThread(Thread):

        def __init__(self,c,ip, port):
            Thread.__init__(self)
            self.c = c
            self.ip = ip
            self.port = port
            print("Socket thread created for Server.."+ip+" port: "+str(port))

        def run(self):
            while True:
                rdata = self.c.recv(1024).decode("ascii")
                print("[+]Server: "+rdata)

    class SendingThread(Thread):

        def __init__(self,c,ip, port):
            Thread.__init__(self)
            self.c = c
            self.ip = ip
            self.port = port
            print("Socket thread created for sending data to Server.."+ip+" port: "+str(port))

        def run(self):
            print("hi")
            while True:
                sdata = input()
                self.c.send(sdata.encode())

    if __name__ == "__main__":
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = int(sys.argv[1])
        ip = '127.0.0.1'
        s.connect((ip,port))
        usr = input("[+] Enter Username: ")
        s.send(usr.encode())
        psd = getpass.getpass("[+] Enter Password: ")
        s.send(psd.encode())
        newCT = RecvThread(s,ip,port)
        newCT.start()
        newST = SendingThread(s,ip,port)
        newST.start()

    # while True:
    # # time.sleep(1)
    # # s.recv(1024).decode("ascii")
    #     msg = input("\n[+]Client: ")
    #     s.send((msg).encode())