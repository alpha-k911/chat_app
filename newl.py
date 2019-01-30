import socket
import sys
import optparse

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	print("Socket created successfully\n")

except 	Exception as err:
	print("Error:"+str(err))
	sys.exit()

#parser=optparse.OptionParser('Usage'+'-H <Host to connect> -p <port to connect>')
#parser.add_option('-H',dest='ip_addr',type='string',help='specify host')
#parser.add_option('-p',dest='port',dest='port',type='string',help='Port to listen and connect')

#(options,args) = parser.parse_args()
#host=str(options.ip_addr).split(',')
#port=options.port
#redirect=options.redirect

#if host == None or redirect == None:
#	print parser.usage
#	exit(0)
s.bind(('',int(sys.argv[1])))
print("Welcome to Chatting Server\n")
s.listen(5)
c,addr = s.accept()
addr=str(addr)[2:11]

#def Authentication(client):
c.send("Enter your username\n>>")
usr=c.recv(1024)
c.send("Username entered:"+str(usr))
s.send("Enter your password:)\n>>")
pas=c.recv(1024)

#def Validation(username,password):
#	if(usr == "admin" and )

