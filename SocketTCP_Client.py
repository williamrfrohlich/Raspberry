#-------------------------------------------------------------------------
#
#		Name: 		Eng. William R. Fröhlich
#
#		Project: 	Socket TCP Client
#
#		Date: 		2019.01.19
#
#-------------------------------------------------------------------------

# Import Library
import socket

# Define Server
HOST = '10.0.0.103'     # Server IP Address
PORT = 5000            	# Server Port

# Define the type of communication
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)

# Open the Socket
tcp.connect(dest)

#-------------------------------------------------------------------------

# Message
print 'Para sair use CTRL+X\n'
msg = input()

# Loop Function
while msg <> '\x18':
    tcp.send ("Bom dia")
    msg = input()
tcp.close()

#----------------------------- OR ----------------------------------------

# Message
print 'Para sair use CTRL+X\n'
msg = raw_input()

# Loop Function
while msg <> '\x18':
    tcp.send (msg)
    msg = raw_input()
tcp.close()

#-------------------------------------------------------------------------