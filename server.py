#!/usr/bin/python
# -*- coding: utf-8 -*-

# *******************************************************************
# Trang Nguyen trang_nguyen@csu.fullerton.edu CWID:802816165
# Insert your name here
#
# CPSC 471 - Section 2
# *******************************************************************

import socket
import sys
import os

bufferSize = 4096
request_queue = 10


# *******************************************************************
# ............................FUNCTIONS
# We need to write these functions:
# a) Receives the specified number of bytes from a specified socket
# b) Gets size of a file in bytes
# c) Send a file to client
# d) Receive a file from client
# e) List file from the server
# f) quit (disconnect/exit)
# *******************************************************************

def recvAll(sock, numBytes):

    # The buffer

    recvBuff = ''

    # Keep receiving till all is received

    while len(recvBuff) < numBytes:

        # Attempt to receive bytes

        tmpBuff = sock.recv(numBytes)

        # The other side has closed the socket

        if not tmpBuff:
            break

        # Add the received bytes to the buffer

        recvBuff += tmpBuff

    return recvBuff


def sizeOfFile(fileName):
    return os.path.getSize(fileName)


# Function to connect to a temporary client socket

def connectTempSocket(client):

    # Create a socket

    tempSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to port 0
    try:
    	tempSocket.bind(('', 0))
    except socket.error, msg:
    	print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' \
        + msg[1])
  	sys.exit()

    # Retreive the ephemeral port number

    tempPortNum = tempSocket.getsockname()[1]
    print ('Ephermeral port # is', tempPortNum)

    # Send tempPortNum to clientSocket

    client.send(str(tempPortNum))

    # Listen on tempSocket  
    # allow only one connection
    tempSocket.listen(1)

    # Accept incoming connections to tempCliSock

    (tempCliSock, addr) = tempSocket.accept()

    # Close listening tempSocket

    tempSocket.close()

    return tempCliSock


# Function to accept a file from client

def receiveFile(filename, tempSocket):

    # Receive the first 10 bytes indicating the
    # size of the file

    fileSizeBuff = recvAll(tempSocket, 10)

    # Get the file size

    if fileSizeBuff == '':
        print ('Nothing received.')
        return 0
    else:
        fileSize = int(fileSizeBuff)

    print ('The file size is', fileSize)

    # Get the file data

    fileData = recvAll(tempSocket, fileSize)

    # Open file to write to

    fileWriter = open(filename, 'w+')

    # Write received data to file

    fileWriter.write(fileData)

    # Close the file

    fileWriter.close()


# *******************************************************************
# ............................MAIN PROGRAM
# *******************************************************************

# if command line has 3 args. For ex: python server.py 1234

if len(sys.argv) < 2:
    print ('python ' + sys.argv[0] + '<port_number>')

serverPort = int(sys.argv[1])

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print ('Socket created')

# bind socket to host and port

try:
    serverSocket.bind(('', serverPort))
except socket.error, msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' \
        + msg[1])
    sys.exit()
print ('Socket bind complete')

# threads = []
# start listening

serverSocket.listen(request_queue)
print ('Socket now listening')

quit = False

# now keep talking with the client

while True:
    if quit == True:
        break

    print ('waiting for connection')
    (clientSocket,add) = serverSocket.accept()
    print ('Connected with client',add, '@', serverPort)
    while not quit:
         command = clientSocket.recv(bufferSize)
         if command[:3] == 'put':
            print ('Put command received. Prepare to receive file')
            fileName = rest
            tempSock = connectTempSocket(clientSocket)

                # Receive the file from client

            print ('Receive ' + fileName + ' from client...')
            success = receiveFile(fileName, tempSock)
            if success == 0:
                print ('Does not receive.' + fileName)
            else:
                print ('Successfully uploaded!')

                    # Close temporary socket

            tempSock.close()
         elif command == 'quit':
             print ('Quit command received.Closing socket now')
             clientSocket.close()
             quit = True
         else:
             print ("Not a valid command")






			
