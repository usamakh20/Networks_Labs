from socket import * # import socket module
serverIP = '10.3.31.220' # replace with IP address of the server
serverPort = 12600 #port where server is listening
clientSocket = socket(AF_INET, SOCK_DGRAM) 
message = input('Input lowercase sentence:') 
clientSocket.sendto(message.encode(),(serverIP, serverPort)) 
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) 
print (modifiedMessage.decode()) # print the received message
clientSocket.close() # Close the socket
