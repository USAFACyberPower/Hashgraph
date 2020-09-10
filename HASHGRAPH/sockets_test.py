#!/usr/bin/env python

__author__ = "Brett Martin"

"""
===========================================================
 Name: ECE 463, Fall 2019/Spring 2020
 Created by: C1C Brett Martin
 Section: M3/4
 Project: Cyber Power Capstone
 Purpose: Sockets data transmission Script
 Documentation: See the Github README journal for all references. 
    I referenced the sockets python document for help with
    setting up sockets.
===========================================================
"""

import socket			 

s = socket.socket()		 
print("Socket successfully created")

port = 6969				

s.bind(('', port))		 
print("socket binded to ", port)

s.listen(5)	 
print("socket is listening")		

while True: 

	c, addr = s.accept()	 
	print('Got connection from', addr)

	c.send('Thank you for connecting'.encode('ascii')) 

	c.close() 
