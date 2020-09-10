#!/usr/bin/env python

__author__ = "Brett Martin"

"""
===========================================================
 Name: ECE 463, Fall 2019/Spring 2020
 Created by: C1C Brett Martin
 Section: M3/4
 Project: Cyber Power Capstone
 Purpose: Telnet Relay Metering and Data Aggregation Script
 Documentation: See the Github README journal for all references. 
    I referenced the telnetlib python document for help with
    setting up telnetlib.
===========================================================
"""

import telnetlib
import time

"""Telnet Test for use with the modified Hashgraph algorithm on RaspPi"""


def telnet_connect(ip_addr, port, timeout, debug):

	tn = telnetlib.Telnet()
	tn.open(ip_addr, port)

	if debug:
		tn.set_debuglevel(100)
	else:
		tn.set_debuglevel(0)

	tn.read_until(b'TERMINAL SERVER:\r\n=')
	tn.write("ACCESS".encode('ascii') + b"\r\n")
	tn.read_until(b"Password: ?")
	tn.write("OTTER".encode('ascii') + b"\r\n")
	tn.read_until(b"=>")
	tn.write("2AC".encode('ascii') + b"\r\n")
	tn.read_until(b"Password: ?")
	tn.write("TAIL".encode('ascii') + b"\r\n")
	tn.read_until(b"=>>")

	return tn


def meter_data(tn):

	tn.write("MET".encode('ascii') + b"\r\n")
	relay_met_data = tn.read_until(b"=>>").decode('ascii')
	print(relay_met_data)

	return relay_met_data


def telnet_close(tn):

	tn.close()

	return


def main():

	TEST_CYCLES = 10

	HOST = "192.168.20.14"
	PORT = 23
	DEBUG_MODE = False
	TIMEOUT = 1
	relay_met_arr = []

	tn = telnet_connect(HOST, PORT, TIMEOUT, DEBUG_MODE)

	start = time.process_time()

	for _ in range(1,TEST_CYCLES):
		relay_met_arr.append(meter_data(tn))
		# print(relay_met_data[-1])

	try:
		print("Sample rate: {} Samples/second".format(TEST_CYCLES/(time.process_time() - start)))
	except:
		print("Sample rate exceeds 640 Samples/second")

	telnet_close(tn)


main()

# https://wiki.python.org/moin/TcpCommunication