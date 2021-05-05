"""
socket communication with client ESP32
prints word meaning
and sends it back to the client
"""
import socket
from PyDictionary import PyDictionary
import time
from threading import Thread

s = socket.socket()
dictionary = PyDictionary()

def handle_connection(client,addr):
    # while True:
    #recv waits for the client to send some data or disconnect
    content = client.recv(1024)

    if len(content) > 0:
        print(content)
        means=content + ":" + str(dictionary.meaning(content))
        print(means)
        client.sendall(means)

    time.sleep(0.5)
    print("Connection closed from client with address:"+str(addr))
    client.close()

#binding socket to ip as a string and a port number to connect to
s.bind(('0.0.0.0', 8090))
s.listen(0)

while True:
    #accept is a blocking method and waits until a new client connects to the server
    client,addr = s.accept()
    print("connection successful from client with address:"+str(addr))
    Thread(target=handle_connection,args=(client,addr)).start()
