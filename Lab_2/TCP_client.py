import time
from socket import *
serverIP="10.99.28.121"
serverPort=12000
sum=0.0
average=0.0
for i in range(0,15):
    x = time.time()
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverIP, serverPort))
    sentence=input('Input lowercase sentence:')
    clientSocket.send(sentence.encode())
    modifiedSentence=clientSocket.recv(1024)
    y=time.time()
    print (x-y)
    sum+=x-y
    print('From Server:',modifiedSentence.decode())
average=sum/15
print ("Average RTT: ",average)
clientSocket.close()
