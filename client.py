#### Receiver (Client) ####

import socket               

# Creating a socket object
s = socket.socket()   
# Specify the server IP address      
server = "192.168.0.115"     
# Port number on which the communication takes place.
port = 6796                 
# This method actively initiates TCP server connection.
s.connect((server, port))
#This method receives TCP message
print s.recv(1024)
# Closes the socket.
s.close()                   