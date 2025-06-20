import socket
import threading
import logging


# FORMAT = '%(asctime)-15s\t [%(threadName)s, %(thread)d] %(message)s'
# logging.basicConfig(level=logging.INFO, format=FORMAT)
#
# client = socket.socket(type=socket.SOCK_DGRAM)
# raddr = ('127.0.0.1',9999)
# client.connect(raddr)
#
# client.sendto(b'hello',raddr)
# data,addr = client.recvfrom(1024)
#
# logging.info(data)
#
# client.close()

class ChatUdpClient:
    def __init__(self, rip='127.0.0.1', rport=9999,interval=10):
        self.raddr = (rip, rport)
        self.sock = socket.socket(type=socket.SOCK_DGRAM)
        self.event = threading.Event()
        self.interval= interval

    def start(self):
        self.sock.connect(self.raddr)
        threading.Thread(target=self.hb, name='heartbeat').start()
        threading.Thread(target=self.recv, name='recv').start()

    def recv(self):
        while not self.event.is_set():
            data, addr = self.sock.recvfrom(1024)
            logging.info(data)

    def send(self, msg: str):
        self.sock.sendto(msg.encode(), self.raddr)

    def hb(self):
        while not self.event.wait(self.interval):
            self.send('^hb^')


    def stop(self):
        self.sock.close()
        self.event.set()


def main():
    cc = ChatUdpClient(interval=5)
    cc.start()

    while True:
        cmd = input('Please input your msg: ')
        if cmd.strip() == 'quit':
            cc.send('quit')
            cc.stop()
            break
        logging.info(threading.enumerate())
        cc.send(cmd)


if __name__ == '__main__':
    main()
