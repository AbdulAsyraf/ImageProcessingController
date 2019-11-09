import socket
import time

HOST = 'localhost'
PORT = 5556

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

run = True
j = 0
while j <= 10:
    print(j)
    sock.send(bytes([j]))

    len = ord(sock.recv(16))
    i = 0
    mess = ""

    while i < len:
        mess = mess + sock.recv(1).decode('UTF-8')
        i = i + 1
    print(mess)

    if mess != "next":
        break

    j = j + 1