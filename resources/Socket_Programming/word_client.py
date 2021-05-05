import socket

HOST = '127.0.0.1' #Standard loop back interface address
PORT = 65433  #port to listen on (non priviliged ports are > 80)

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    word =  raw_input("Enter the word for its meaning:")
    s.sendall(word)
    meaning = s.recv(1024)
    print(meaning)
