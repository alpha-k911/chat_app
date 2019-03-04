creating a node  => s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

conneting to a domain => host_ip = socket.gethostbyname("name of the host :google.com")

port=80

connecting to server s.connect((host_ip, port))
