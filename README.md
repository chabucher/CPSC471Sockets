# 471FinalProject

+ Team Members:
	1/ trang_nguyen@csu.fullerton.edu
	2/ jcoberly@csu.fullerton.edu

+ Project Assignment - FTP Server and Client applications
	a) Programming Language used: Python version 3 and above
	b) Files included in this submission:
		1/ FTP Client program		cli.py
		2/ FTP Server program		serv.py
		3/ will add some more later on		


+ How to execute this program:
	In my case, I'm using Ubuntu terminal and python 3.6
	 Steps to execute:
		1/ On a terminal, navigate to where server.py is
		2/ Type "python server.py <port_number>" to run the server
		  	 e.g. $ python server.py 1234
		3/ On a separate terminal, navigate to where client.py is
		4/ Type "python client.py <server_machine> <port_number>" to run the client
		   To test on the same computer, use $ python client.py localhost 1234
		  	 e.g. $ python client.py ecs.fullerton.edu 1234
		5/ Start using the program
