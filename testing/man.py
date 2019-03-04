import socket
try:
    pass
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket created succesfully")
except Exception as e:
    raise
    print("Failed in creation")
port = 80

try:
    host_ip = socket.gethostbyname("www.google.com")
except Exception as e:
    raise
    print("error in connecting to the domain")
s.connect((host_ip, port))
print("connected to google: "+host_ip)
