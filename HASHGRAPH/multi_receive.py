#!/usr/bin/env python3

import socket

HOST = '192.168.20.183'     # Server IPV4 address
PORT = 65432                # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while(1):
        conn, addr = s.accept()
        with conn:
            print('New connection!\n Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    print("End connection\n\n")
                    break
                print('Received', repr(data))
                conn.sendall(data)
