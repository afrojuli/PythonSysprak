from socket import *
from constants import *

def getConnection():
    try:
        while True:
            print ("Serveradresse: ", SERVER_NAME)
            sock = socket(AF_INET, SOCK_STREAM)
            sock.connect((SERVER_NAME, SERVER_PORT))
            print ("Socket connected")
            break
        return sock
    except Exception:
        print ("There seems to be an Exception ")
    finally:
        pass
