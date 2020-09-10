#!/usr/bin/env python

__author__ = "Brett Martin"

"""
===========================================================
 Name: ECE 463, Fall 2019/Spring 2020
 Created by: C1C Brett Martin
 Section: M3/4
 Project: Cyber Power Capstone
 Purpose: Sockets data transmission Script, Client Side
 Documentation: See the Github README journal for all references. 
    I referenced the sockets python document and 
    RealPython.com for help with setting up sockets.
===========================================================
"""

import socket

s = socket.socket()

port = 6969

s.connect(('192.168.20.249', port))

print(s.recv(1024))
s.close()
