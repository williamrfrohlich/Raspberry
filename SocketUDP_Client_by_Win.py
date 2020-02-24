#-------------------------------------------------------------------------
#
#		Name: 		Eng. William R. Fröhlich
#
#		Project: 	Socket UDP Client by Windows
#
#		Date: 		2019.01.13
#
#-------------------------------------------------------------------------


import socket														# Import the Library

server = '10.0.0.103'												# IP of the Server
port = 5000															# Port of the Server
address = (server, port)											# Address of the Connection

# Address familly (default is socket.AF_INET)
# If is stream (socket.SOCK_STREAM) or datagram (socket.SOCK_DGRAM)
# AF_INIT == Protocol IP Address
# SOCK_STREAM == Protocol TCP
# SOCK_DGRAM == Protocol UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)				

msg = input()														# Receive the String


#-------------------------------------------------------------------------

sock.sendto(msg.encode('utf-8'),address)							# Send the Message

#-------------------------- Or -------------------------------------------

# Loop Function
while True:

    tcp.send (msg.encode('utf-8'))									# Send the Message

tcp.close()

#-------------------------------------------------------------------------