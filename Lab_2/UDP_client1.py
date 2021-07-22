from socket import * # import socket module

import time

serverIP = "10.3.33.136" # replace with IP address of the server

serverPort = 12000 #port where server is listening

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input("Input lowercase sentence:")
count=0

for i in range(0,15):
    start = time.perf_counter()

    clientSocket.sendto((message+" "+str(i)).encode(),(serverIP, serverPort))

    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

    print (modifiedMessage.decode()) # print the received message
    end = (time.perf_counter()-start)*1000
    print("Time Taken: "+str(end)+" milliseconds")
    count+=end

clientSocket.close() # Close the socket
print("Average RTT: "+str(count/15))