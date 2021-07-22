from socket import*
import os

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):              #https://stackoverflow.com/questions/1724693/find-a-file-in-python
        if name in files:
            result.append(os.path.join(root, name))
    return result


def prepare_list(files):
    data = ""
    for (i,file) in enumerate(files):
        data += "\n"+str(i+1)+". "+file
    return data

serverPort=12000
serverSocket=socket(AF_INET,SOCK_STREAM)

print("The server is ready to receive")

serverSocket.bind(('',serverPort))
serverSocket.listen(14)
count=0
files = []
error = "No file found".encode()
while True:
    connectionSocket,addr=serverSocket.accept()
    msg=connectionSocket.recv(1024)
    msg=msg.decode()
    if msg is "exit":
        break
    elif str(msg).isdigit():
        msg =int(msg)
        if len(files)<msg:
            connectionSocket.send(error)
            continue

        f = open(files[msg-1], 'rb')   #https://stackoverflow.com/questions/27241804/sending-a-file-over-tcp-sockets-in-python
        print( 'Sending...')
        l = f.read(1024)
        while (l):
            connectionSocket.send(l)
            l = f.read(1024)
        f.close()
        print ("File Sent")
    else:
        print("File name requested: "+msg)
        files = find_all(msg,"G:\Downloads")
        if files: tosend = prepare_list(files).encode()
        else: tosend = error
        connectionSocket.send(tosend)
    connectionSocket.close()



