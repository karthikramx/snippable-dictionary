import socket
from PyDictionary import PyDictionary

HOST = '127.0.0.1' #Standard loop back interface address
PORT = 65432 #port to listen on (non priviliged ports are > 80)

dictionary = PyDictionary()

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by',addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            client.sendall(dictionary.meaning(data))
