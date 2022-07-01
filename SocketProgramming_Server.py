# this server socket we will make for accepting the connections

import socket
s = socket.socket()
# in bracket it can take two arguments 1. type of address IPV4 or IPV6 etc
# 2. Type of network connection TCP or UDP by default it is IPV4 and TCP
# TCP - Transmission control protocol- Connection oriented protocol in which you have to first create a
# connection only then it can communicate
# UDP - User Datagram Protocol -  In this we do not need to create connection you just need to send packets
# The drawback of UDP is that you will not know if the package has reached or not as there is no confirmation
# bit send back
print('Socket created')

s.bind(('localhost',9999)) # Helps to assign a socket number from PC/Local host to socket number 9999

s.listen(3) # Helps to listen to clients and you can specify the number of clients you want to
# listen to, here 3 clients
print("Waiting for clients")

while True:
    c,ipadrCli=s.accept() # accepting a client
    name=c.recv(1024).decode() # getting data about user entered name in client
    print('connected to IP address',ipadrCli, name) # Printing IP address of client and user name entered
    c.send(bytes('Welcome to Tulesko','utf-8'))
    c.close()





