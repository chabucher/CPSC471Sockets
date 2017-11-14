# *******************************************************************
# Trang Nguyen trang_nguyen@csu.fullerton.edu CWID:802816165
# Insert your name here
# 
# CPSC 471 - Section 2
# *******************************************************************

import sys
import os
import subprocess
import socket

bufferSize = 4096
serverName = "localhost"

# *******************************************************************
#							FUNCTIONS
# We need to write these functions:
# a) Receives the specified number of bytes from a specified socket
# b) Gets size of a file in bytes
# c) Upload a file to server
# d) Download a file from server
# e) List file from the server
# f) quit (disconnect/exit)
# *******************************************************************


def recvAll(sock, numBytes):

	# The buffer
	recvBuff = ""
	
	# Keep receiving till all is received
	while len(recvBuff) < numBytes:
		# temporary buffer
		# Attempt to receive bytes
		tmpBuff =  sock.recv(numBytes)
		
		# The other side has closed the socket
		if not tmpBuff:
			break
		
		# Add the received bytes to the buffer
		recvBuff += tmpBuff
	
	return recvBuff

# Function to create a socket using a provided port number
def createSocket(portNum):

	# Create a TCP socket
	connSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	# Connect to server
	connSock.connect((serverName, int (portNum)))
	print ("Connected to port #", portNum)
	
	# Return a socket
	return connSock

	
def sizeOfFile (fileName):
	statinfo = os.stat(fileName)
	size = statinfo.st_size
	return size

def uploadFileToServer(fileName, portNumb):

	#generate an emphemeral port
	tempSocket=createSocket(portNumb)

	#open file 
	try:
		file_object=open(fileName,'r')
	except OSError:
		print ("can not open file %s to read", fileName)
		tempSocket.close()

	fileSize=sizeOfFile(fileName)
	print ("Uploading", fileName,"to server")

	while True:
		# Read  data
		fileData = file_object.read(fileSize)
	
		# Make sure we did not hit EOF
		if fileData:
		
			
			# Get the size of the data read
			# and convert it to string
			dataSizeStr = str(len(fileData))
		
			# Prepend 0's to the size string
			# until the size is 10 bytes
			while len(dataSizeStr) < 10:
				dataSizeStr = "0" + dataSizeStr
	
	
			# Prepend the size of the data to the
			# file data.
			fileData = dataSizeStr + fileData	
		
			# The number of bytes sent
			numSent = 0
		
			# Send the data!
			while len(fileData) > numSent:
				numSent += tempSocket.send(fileData[numSent:])
	
		# The file has been read. We are done
		else:
			break

		print ("Sent ", numSent, " bytes.")
	
	# Close the socket and the file
	file_object.close()
	tempSocket.close()
	
	

#def downloadFileFromServer(socket,fileName):





# *******************************************************************
#							MAIN PROGRAM
# *******************************************************************


#if client command line has 3 args. for ex: python client.py localhost 1234

if len(sys.argv) < 3:
	print ("python " + sys.argv[0]+"<server_machine>"+"<server_port>")

serverName=sys.argv[1]
serverPort=int (sys.argv[2])

primarySocket= createSocket(serverPort)

ans = ""
fileName = ""
success = ""

ans =raw_input("ftp> ")
while (ans != "quit"):
	(command, rest) = ans.split()
	if command == "put":
		fileName = rest
		primarySocket.send(ans)
		tempPort=primarySocket.recv(bufferSize)
		print ("Ephermeral port # ",tempPort)
		success = uploadFileToServer(fileName,tempPort)
		if success == 0:
			print ("fail to upload")
		else:
			print("successfully uploaded")
	elif command == "get":
		fileName = rest

	else:
		print ("not a valid command")

if (ans == "quit"):
	primarySocket.send(ans)
	print ("closing now")
	primarySocket.close()
		







