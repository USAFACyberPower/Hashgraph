#!/usr/bin/env python3

import socket

HOST = ['192.168.20.182', '192.168.20.230']  	# The server's hostname or IP address
PORT = 65432        	 	# The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s_host = int(input("Which host? (0 or 1): "))
	s_send = input("Enter message to send: ")
	try:
	    s.connect((HOST[s_host], PORT))
	    s.sendall(s_send.encode('ascii'))
	    data = s.recv(1024)
	except:
		print("Invalid input \n")

print('Data sent successfully:', repr(data))