from socket import *
import sys
from multiprocessing import Process
import os

SERVER_NAME = "sysprak.priv.lab.nm.ifi.lmu.de"
SERVER_PORT = 1357
BUFSIZE = 256
GAMEKINDNAME = "Reversi"

def thinker(title):
    info(title)



def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def connector(title):
    info(title)
    gameId = sys.argv[1]

    sock = getConnection()
    data = receive_Line(sock)
    print "Daten: %s" % (data)

    data = 'VERSION 1.0\n'
    send_Line(sock, data)

    data = receive_Line(sock)
    print "Daten: %s" % (data)

    sock.close()


def main():
    p = Process(target=connector, args=('Connector',))
    p.start()
    thinker("Thinker")
    p.join()


def getConnection():
    try:
        while True:
            print "Serveradresse: ", SERVER_NAME
            sock = socket(AF_INET, SOCK_STREAM)
            sock.connect((SERVER_NAME, SERVER_PORT))
            break
        return sock
    except Exception, arg:
        print "There seems to be an Exception ", arg
    finally:
        pass

def receive_Line(sock):
    data = ""
    while True:
        data += sock.recv(BUFSIZE)
        if data == '':
            raise RuntimeError("socket connection broken")
        elif data[len(data)-1] == "\n":
            return data

def send_Line(sock, data):
    totalsent = 0
    while True:
        sent = sock.send(data[totalsent:])
        totalsent += sent
        if totalsent >= len(data):
            break

if __name__ == '__main__':
    main()
