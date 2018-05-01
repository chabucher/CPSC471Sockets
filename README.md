# 471FinalProject

# Team Members:

	1) Trang Nguyen: trang_nguyen@csu.fullerton.edu
	2) Justin Coberly: jcoberly@csu.fullerton.edu
	3) Charles Bucher: chabucher@csu.fullerton.edu
	4) Andre Victoria: andreappstuff@csu.fullerton.edu

# Instructions

	Using Ubuntu terminal and Python 3.6
	
	 Steps to execute:
	 
		1) On a terminal, navigate to server.py directory
		2) Type "python3 server.py <port_number>" to run the server
		  	 e.g. $ python server.py 1234
		3) On a separate terminal, navigate to where client.py is
		4) Type "python3 client.py <server_machine> <port_number>" to run the client
                 To test on the same computer:
                    $ python3 client.py localhost 1234
                 To test on an actual server
		  	      $ python3 client.py ecs.fullerton.edu 1234
		5) Start using the program
