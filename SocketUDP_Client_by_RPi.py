#-------------------------------------------------------------------------
#
#		Name: 		Eng. William R. Fröhlich
#
#		Project: 	Socket UDP Client by Raspberry Pi
#
#		Date: 		2019.01.13
#
#-------------------------------------------------------------------------

# Import Library
import socket

server = '10.0.0.103'												# IP of the Server
port = 5000															# Port of the Server
address = (server, port)											# Server

# Address familly (default is socket.AF_INET)
# If is stream (socket.SOCK_STREAM) or datagram (socket.SOCK_DGRAM)
# AF_INIT == Protocol IP Address
# SOCK_STREAM == Protocol TCP
# SOCK_DGRAM == Protocol UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = raw_input()													# Receive the Message

sock.sendto(msg,address)											# Send the Message