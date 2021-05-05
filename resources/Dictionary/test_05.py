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
import numpy as np
from PIL import Image
import cv2


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

def ocr(imageScan):
    pass

def show_image():
    image = cv2.imread("img.png",1)
    image = cv2.flip(image,1)
    image = cv2.flip(image,0)
    image = cv2.flip(image,1)
    cv2.imshow("qw",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def process_scan(scanData):
    try:
        print(len(scanData))
        img = np.reshape(scanData,((int(len(scanData)/128)),128))
        print(img.shape)
        image = Image.new("L", np.shape(img))
        pixels = image.load()
        for i in range(len(img)):
            for j in range(len(img[0])):
                pixels[i, j] = img[i][j]
        image.save("img.png")
        show_image()

    except:
        print("Empty scan")

def handle_connection(client,addr):
    buffer = ""
    while True:
        try:
            content = client.recv(128)
            if len(content) > 0:
                if(content=="EndScan"):
                    print("End of scan")
                    break
                else:
                    buffer+=content
            else:
                break
        except Exception, exc:
            print(exc)
    scan_buffer = [ord(i) for i in buffer]
    process_scan(scan_buffer)
    client.sendall("word meaning")
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
