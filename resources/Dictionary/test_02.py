"""
socket communication with client ESP32
"""

#socket module
import socket

#creating socket module
s = socket.socket()

#binding socket to ip as a string and a port number to connect to
s.bind(('0.0.0.0', 8090 ))

s.listen(0)

while True:
    #accept is a blocking method and waits until a new client connects to the server
    client,addr = s.accept()

    while True:
        #recv waits for the client to send some data or disconnect
        content = client.recv(32)

        if len(content) == 0:
            break
        else:
            print(content)

    print("Closing connection")
    client.close()
