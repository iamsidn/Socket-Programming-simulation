#### Sender (Server) ####        

import socket               

# Creating a socket object
s = socket.socket()        
host = socket.gethostname() 
# This is the port number on which the communication takes place.
port = 6796  
# This method binds address (hostname, port number pair) to socket.             
s.bind((host, port))   
# This method sets up and start TCP listener.     
s.listen(5)                 
while True:
    # This passively accept TCP client connection, waiting until connection arrives (blocking).
    c, addr = s.accept()     
    print 'Got connection from', addr
    # This method transmits TCP message
    c.send('Connection Established!!')
    # Closes the socket
    c.close()                