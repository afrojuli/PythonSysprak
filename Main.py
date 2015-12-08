from socket import *
import sys
from multiprocessing import Process
import info
from constants import *
from send_receive import *
from get_connection import *




def thinker(title):
    info.info(title)


def connector(title):
    info.info(title)
    gameId = sys.argv[1]

    sock = getConnection()
    data = receive_Line(sock)
    print ("Daten: %s" % (data))

    data = 'VERSION 1.0\n'
    send_Line(sock, data)

    data = receive_Line(sock)
    print ("Daten: %s" % (data))

    sock.close()


def main():
    p = Process(target=connector, args=('Connector',))
    p.start()
    thinker("Thinker")
    p.join()


if __name__ == '__main__':
    main()
