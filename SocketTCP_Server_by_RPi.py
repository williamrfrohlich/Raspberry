#-------------------------------------------------------------------------
#
#		Name: 		Eng. William R. Fröhlich
#
#		Project: 	Socket TCP Server by Raspberry Pi
#
#		Date: 		2019.01.19
#
#-------------------------------------------------------------------------

# Import Library
import socket

# Address familly (default is socket.AF_INET)
# If is stream (socket.SOCK_STREAM) or datagram (socket.SOCK_DGRAM)
# AF_INIT == Protocol IP Address
# SOCK_STREAM == Protocol TCP
# SOCK_DGRAM == Protocol UDP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address =('',5000)		# IP and Port of the Server
tcp.bind(address)		# Open the Socket

tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    print 'Concetado por', cliente
    while True:
        msg = con.recvfrom(1024)
        if not msg: break
        print cliente, msg
		arquivo = open('ESP32.txt', 'a')						# Creat / Open the file "ESP32"
		arquivo.write(msg + "\n")								# Write the information in a new line
		print("Informação Recebida")							# Show the information
		arquivo.close()											# Close the file
    print 'Finalizando conexao do cliente', cliente
    con.close()