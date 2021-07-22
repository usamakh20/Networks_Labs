from socket import *
serverPort=12000
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print('UDP Server is ready to receive:')
while(1):
    message,clientAddress=serverSocket.recvfrom(2048)
    modifiedMessage=message.upper()
    print(message.decode())
    serverSocket.sendto(modifiedMessage,clientAddress)
