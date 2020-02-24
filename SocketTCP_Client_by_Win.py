#-------------------------------------------------------------------------
#
#		Name: 		Eng. William R. Fröhlich
#
#		Project: 	Socket TCP Client by Windows
#
#		Date: 		2019.01.19
#
#-------------------------------------------------------------------------

import socket														# Import Library

server = '10.0.0.106'												# IP of the Server
port = 5000															# Port of the Server
address = (server, port)											# Server

# Address familly (default is socket.AF_INET)
# If is stream (socket.SOCK_STREAM) or datagram (socket.SOCK_DGRAM)
# AF_INIT == Protocol IP Address
# SOCK_STREAM == Protocol TCP
# SOCK_DGRAM == Protocol UDP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Open the Socket
tcp.connect(address)

# Receive the Information
msg = input()

# Loop Function
while True:

    tcp.send (msg.encode('utf-8'))

tcp.close()