#-------------------------------------------------------------------------
#
#		Name: 		Eng. William R. Fröhlich
#
#		Project: 	Socket UDP Server by Raspberry Pi
#
#		Date: 		2019.01.13
#
#-------------------------------------------------------------------------

import socket                                               # Import the Library

# Address familly (default is socket.AF_INET)
# If is stream (socket.SOCK_STREAM) or datagram (socket.SOCK_DGRAM)
# AF_INIT == Protocol IP Address
# SOCK_STREAM == Protocol TCP
# SOCK_DGRAM == Protocol UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

address =('',5000)											# IP and Port of the Server
sock.bind(address)                                          # Open the Socket

while True:													# Loop Function
    data, addr= sock.recvfrom(1024)							# Accept the connection
    print (data)											# Send String
    print (addr)											# Client Address
