import socket

c=socket.socket()
c.connect(('localhost',9999))  # Connects to port/socket on PC

name=input('Enter your Name:')  # Asking Client to enter there name so that it can be sent to server
c.send(bytes(name,'utf-8')) # sending name to server

print(c.recv(1024).decode()) # receiving data from server
