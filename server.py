import socket
import sys
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
    auth(c)
def auth(c):
    c.send("Enter Username:".encode())
    usr = c.recv(10).decode("ascii")[:-1]
    print(usr)
    c.send("Enter Password:".encode())
    psd = c.recv(10).decode("ascii")[:-1]
    print(psd)
    valid(usr, psd, c)

def valid(u, p, c):
    if u == "admin" and p == "admin":
        conn(c)
    else:
        c.send("Server: Wrong Username/Password".encode())
        c.close()

def conn(c):
    c.send("Server: Successfully Validated\n".encode())
    while True:
        data = input("Server: ")
        data = "Server: " + data + "\n" + "Client: "
        c.send(data.encode())
        msg_rev=c.recv(10).decode("ascii")[:-1]
        msg_rev = "Client: " + msg_rev
        print(msg_rev)
if __name__ == "__main__":
    create()
