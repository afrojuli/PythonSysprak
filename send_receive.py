from socket import *
import sys
from constants import *

def receive_Line(sock):
    data = ""
    while True:
        data += sock.recv(BUFSIZE).decode()
        if data == '':
            raise RuntimeError("socket connection broken")
        elif data[len(data)-1] == "\n":
            return data

def send_Line(sock, data):
    totalsent = 0
    while True:
        sent = sock.send(data[totalsent:].encode())
        totalsent += sent
        if totalsent >= len(data):
            break
