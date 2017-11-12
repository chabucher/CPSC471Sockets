# *******************************************************************
# Trang Nguyen trang_nguyen@csu.fullerton.edu CWID:802816165
# Insert your name here
# 
# CPSC 471 - Section 2
# *******************************************************************

import sys
import subprocess
import socket



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
	
	# The temporary buffer
	tmpBuff = ""
	
	# Keep receiving till all is received
	while len(recvBuff) < numBytes:
		
		# Attempt to receive bytes
		tmpBuff =  sock.recv(numBytes)
		
		# The other side has closed the socket
		if not tmpBuff:
			break
		
		# Add the received bytes to the buffer
		recvBuff += tmpBuff
	
	return recvBuff

def createSocket(portNumb):
	import socket
	#create an INET, STREAMing socket
	clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	#bind the socket to a port
	clientSocket.connect((serverName,portNumb))
	print("Connected to port #:",portNumb)

	return clientSocket

	
def sizeOfFile (fileName):
	import os
	return os.path.getSize(fileName)
	
def uploadFileToServer(fileName):

	#generate an emphemeral port
	tempSocket=createSocket(portNumb)

	#open file 
	try:
		file_object=open(fileName,'r')
	except OSError:
		print ("can not open file %s to read", fileName)
		tempSocket.close()

	fileSize=sizeOfFile(fileName)

	while True:
		# Read  data
		fileData = file_object.read(fileName)
	
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
def sendFile(serverAddr, serverPort, fileName):
	# Open the file
	fileObj = open(fileName, "r")

	# Create a TCP socket
	connSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Connect to the server
	connSock.connect((serverAddr, serverPort))

	# The number of bytes sent
	numSent = 0

	# The file data
	fileData = None

	# Keep sending until all is sent
	while True:
		
		# Read 65536 bytes of data
		fileData = fileObj.read(65536)
		# Make sure we did not hit EOF
		if fileData:
			
				
			# Get the size of the data read
			# and convert it to string
			dataSizeStr = str(len(fileData))
			print("Printing Data Size: ", dataSizeStr)
			
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
				numSent += connSock.send(fileData[numSent:].encode('utf-8'))
		
		# The file has been read. We are done
		else:
			break


	print("Sent ", numSent, " bytes.")
		
	# Close the socket and the file
	connSock.close()
	fileObj.close()

def sendCommand(clientSocket, serverAddr, serverPort, commandName):
	

	# The number of bytes sent
	numSent = 0

	# Keep sending until all is sent
	while True:	
		
		dataSize = str(len(commandName))
		while len(dataSize) < 10:
			dataSize = "0" + dataSize

		commandData = dataSize + commandName

		# The number of bytes sent
		numSent = 0
			
		# Send the data!
		while len(commandData) > numSent:
			numSent += clientSocket.send(commandData[numSent:].encode('utf-8'))
		
		# The file has been read. We are done
		else:
			break


	print("Sent ", numSent, " bytes.")
		

def recvAll(sock, numBytes):
	# The buffer
	recvBuff = ""
	
	# The temporary buffer
	tmpBuff = ""
	
	# Keep receiving till all is received
	while len(recvBuff) < numBytes:
		
		# Attempt to receive bytes
		tmpBuff =  sock.recv(numBytes)
		
		# The other side has closed the socket
		if not tmpBuff:
			break
		
		# Add the received bytes to the buffer
		recvBuff += tmpBuff.decode('UTF-8')
	
	return recvBuff



# *******************************************************************
#							MAIN PROGRAM
# *******************************************************************


#if client command line has 3 args. for ex: python client.py localhost 1234

if len(sys.argv) < 3:
	print ("python " + sys.argv[0]+"<server_machine>"+"<server_port>")

serverName=sys.argv[1]
serverPort=int(sys.argv[2])
print(serverName)

clientSocket= createSocket(serverPort)

ans = ""

while (ans != "quit"): 
	ans = input("ftp> ")
	command = ans.split()
	print(command[0])
	if command[0] == "put":
		fileName = command[1]
		sendCommand(clientSocket, serverName, serverPort, command[0])
		dataBuff = recvAll(clientSocket, 10)
		portNum = recvAll(clientSocket, int(dataBuff))
		sendCommand(clientSocket, serverName, portNum, command[1])


		
		


clientSocket.close()
	






