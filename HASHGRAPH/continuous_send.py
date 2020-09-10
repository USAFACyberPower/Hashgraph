#!/usr/bin/env python3

import socket
import random

HOST = ['192.168.20.182', '192.168.20.230']  	# The server's hostname or IP address
PORT = 65432        	 	# The port used by the server

while True:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s_host = 0
		s_send = str(random.random())
		try:
		    s.connect((HOST[s_host], PORT))
		    s.sendall(s_send.encode('ascii'))
		    data = s.recv(1024)
		    print("sent!")
		    #print('Data sent successfully:', repr(data))
		except:
			print("Invalid input \n")
