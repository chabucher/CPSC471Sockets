# *******************************************************************
# Trang Nguyen trang_nguyen@csu.fullerton.edu CWID:802816165
# Insert your name here
# 
# CPSC 471 - Section 2
# *******************************************************************




import socket
import sys

bufferSize = 4096
request_queue=10



# *******************************************************************
#							FUNCTIONS
# We need to write these functions:
# a) Receives the specified number of bytes from a specified socket
# b) Gets size of a file in bytes
# c) Send a file to client
# d) Receive a file from client
# e) List file from the server
# f) quit (disconnect/exit)
# *******************************************************************




# *******************************************************************
#							MAIN PROGRAM
# *******************************************************************

#if command line has 3 args. For ex: python server.py 1234
if len(sys.argv) < 2:
	print ("python " + sys.argv[0]+"<port_number>")

serverPort=int(sys.argv[1])

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print ('Socket created')

#bind socket to host and port
try:
	serverSocket.bind(('', serverPort))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
print ('Socket bind complete')

#threads = []
#start listening
serverSocket.listen(request_queue)
print ('Socket now listening')

#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = serverSocket.accept()
    print ('Connected with ' , addr , '@' , serverPort)
    


