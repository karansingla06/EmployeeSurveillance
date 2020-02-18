import os
import socket
PORT = 8082
HOST = 'localhost'
print   '---------------File Receiver--------------:'
extn = raw_input('enter path with file name with its extension to store (eg:- foo:/foo.txt)\n').strip(' ')
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))
filename = socket.recv(1024)
fname = open(extn, 'wb')

while True:
	strng = socket.recv(1024)
	if strng:
		fname.write(strng)
	else:
		fname.close()
		break
socket.close()
print 'Data received correctly'	
exit()
