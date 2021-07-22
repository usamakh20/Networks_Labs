from socket import *

import time

serverIP = "10.3.33.136"

serverPort = 12001

sentence = input("Input lowercase sentence:")

count=0

for i in range(0,15):
    start = time.perf_counter()
    clientSocket = socket(AF_INET, SOCK_STREAM)

    clientSocket.connect((serverIP,serverPort))

    clientSocket.send(sentence.encode())

    modifiedSentence = clientSocket.recv(1024)
    end = (time.perf_counter() - start) * 1000
    print("Time Taken: " + str(end) + " milliseconds")
    count += end

    print ("From Server:", modifiedSentence.decode())

    clientSocket.close()

print("Average RTT: "+str(count/15))