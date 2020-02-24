#-------------------------------------------------------------------------
#
#		Name: 		Eng. William R. Fröhlich
#
#		Project: 	Socket TCP Server
#
#		Date: 		2019.01.19
#
#-------------------------------------------------------------------------

# Import Library
import socket
HOST = ''              # Server IP Address
PORT = 5000            # Server Port

# Define Type of Communication
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)

# Open the Socket
tcp.bind(orig)
tcp.listen(1)

# Loop Function
while True:
    con, cliente = tcp.accept()
    print 'Concetado por', cliente
    while True:
        msg = con.recv(1024)
        if not msg: break
        print cliente, msg
    print 'Finalizando conexao do cliente', cliente
    con.close()