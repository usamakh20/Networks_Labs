from socket import *
serverIP="127.0.0.1"
serverPort=12000
msg = "No file found"
requested = ""

while True:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverIP, serverPort))
    if msg is not "No file found":
        prompt = input("Enter file No.")
        prompt=prompt.encode()

    else :
        prompt=input('Enter file to find: ')
        requested = prompt
        prompt = prompt.encode()

    clientSocket.send(prompt)

    if msg is not "No file found":
        print ("Receiving...")
        f = open(requested, 'wb')                 #https://stackoverflow.com/questions/27241804/sending-a-file-over-tcp-sockets-in-python
        l = clientSocket.recv(1024)
        while (l):
            f.write(l)
            l = clientSocket.recv(1024)
        f.close()
        print ("Done Receiving")
    else:
        msg = clientSocket.recv(1024)
        msg = msg.decode()
        print('From Server:',msg)
    clientSocket.close()