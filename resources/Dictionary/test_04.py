"""
socket communication with client ESP32
prints word meaning
and sends it back to the client
"""

import socket
from PyDictionary import PyDictionary
import time
import signal
from threading import Thread

s = socket.socket()
dictionary = PyDictionary()

def handler(signum,frame):
    print("Time Out!")

def get_word_meaning(content):
    meaning = dictionary.meaning(content)
    print(meaning)
    meanings = ""
    for words in meaning.values()[0]:
        meanings = str(words) + ","
        means=content + " (" + str(meaning.keys()[0]) +")" + ":" + str(meaning.values()[0][:])
    print(means)
    return means

def handle_connection(client,addr):
    # while True:
    #recv waits for the client to send some data or disconnect
    content = client.recv(1024)
    try:
        if len(content) > 0:
            print(content)
            #signal.signal(signal.SIGALRM,handler)
            # signal.alarm(5)
            client.sendall(get_word_meaning(content))
    except Exception, exc:
        print(exc)
        client.sendall("Sorry...try again!")


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
