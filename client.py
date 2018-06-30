import socket
from time import sleep

class ClientObject:

    def __init__(self,host_address,server_port,port = 0):

        self._server = (host_address,server_port)
        self._s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._s.bind((host_address,port))


    def handshake(self):

        print(' sending marco')

        self._s.sendto('marco'.encode(),self._server)
        sleep(.1)
        self._s.sendto('marco'.encode(),self._server)

        while True:
            if str(self._s.recvfrom(1024)[0].decode()) == 'polo':
                break

        #self._s.sendto('marco',self._server)
        #self._s.sendto('marco',self._server)

        print(' connection verified')
        self._s.sendto('confirm'.encode(),self._server)

        self._s.setblocking(0)

        return True

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

    def send(self,data):
        self._s.sendto(str(data),self._server)

    def close(self):
        self._s.close()
        print('_socket closed_')


if __name__ == '__main__':

    host = '127.0.0.1'
    port = 0

    talk = ClientObject(host,6003,port)
    talk.handshake()
    
    talk.close()

    #while True:
        #print(talk.recieve())