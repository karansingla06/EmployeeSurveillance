import os
import socket
PORT = 8082
HOST = ''
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST,PORT))
socket.listen(5)
conn, addr = socket.accept()
arr=[]
print '-------------------------File Sender--------------------------------'
def selection_path():
	PATH = raw_input('Select the Path (./ by default)').strip('n')
	if PATH == '':
		PATH = os.getcwd()+'/'	 
	print PATH
	show_files = raw_input('Press(S/N)\n\tS: to show list of files in '+PATH+'\n\tN: to change directory\n').lower().strip(' ')
	if show_files == 's':
		return PATH
	else:
		return selection_path()
def filesDir(path):
	files = os.listdir(PATH)
	for fl in files:
		i = int(files.index(fl))+1
		arr.append(str(i)+ ')' + fl)
	return files
def select_file():
        return int(raw_input('Select a file with the number').strip(' ').lower())
        

PATH = selection_path()
print 'Files in :-', PATH,' _____________'
filesDir(PATH)
for i in range(0,len(arr)):
        print arr[i]
fileSelected = select_file()
if fileSelected > len(arr):
        print 'Out of index, Try Again\n'
        fileSelected = select_file()
filepath = PATH + filesDir(PATH)[fileSelected-1]
print filepath
conn.send(filepath)
qLines = len(open(filepath, 'rb').readlines())
fileToSend = open(filepath, 'rb')
while True:
	data = fileToSend.readline()
	if data:
		conn.send(data)
	else:
		break
fileToSend.close()
conn.sendall('')
conn.close()
print 'File sent'
exit()
