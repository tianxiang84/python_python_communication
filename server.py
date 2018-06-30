import socket
from random import random
from time import sleep

class ServerObject:

    def __init__(self,host_address,port):

        self._host_address = host_address
        self._s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._s.bind((self._host_address,port))

    def handshake(self):

        print("Server Started. Awaiting Connection")

        while True: 
            _data, _addr = self._s.recvfrom(1024)
            if str(self._s.recvfrom(1024)[0].decode()) == 'marco':
                break

        print('marco recieved. sending polo...')

        while True:
            self._s.sendto('polo'.encode(),_addr)
            if str(self._s.recvfrom(1024)[0].decode()) == 'confirm':
                break
            sleep(.5)

        print('connection verified')

        self._addr = _addr

        return True

    def send(self,data):

        self._s.sendto(str(data),self._addr)

    def recieve(self,mode = 0):

        _data, _addr = self._s.recvfrom(1024)

        if mode == 0:
            return str(_data)
        if mode == 1:
            return int(_data)
        if mode == 2:
            return float(_data)
        if mode == 3:
            return tuple(_data)

    def change_port(self,port):

        self._s.bind((self._host_address,port))

    def close(self):
        self._s.close()
        print('_socket closed_')


if __name__ == '__main__':

    host = '127.0.0.1'

    talk = ServerObject(host,6003)
    talk.handshake()
    
    talk.close()
            