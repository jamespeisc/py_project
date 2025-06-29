import threading
import socket
import logging
import datetime
FORMAT = '%(asctime)-15s\t [%(threadName)s, %(thread)d] %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)


class ChatServer:
    def __init__(self, ip='127.0.0.1', port=9999):
        self.addr = (ip, port)
        self.sock = socket.socket()
        self.clients = {}

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()  # 服务启动了

        threading.Thread(target=self.accept, name="accept").start()

    def accept(self):
        while True:
            s, raddr = self.sock.accept()
            logging.info(raddr)
            logging.info(s)
            self.clients[raddr] = s
            threading.Thread(target=self.recv, name='recv', args=(s,)).start()

    def recv(self, sock:socket.socket):
        while True:
            try:
                data = sock.recv(1024)
                logging.info(data)
            except Exception as e:
                logging.error(e)
                data = b'quit'
            if data == b'quit':
                self.clients.pop(sock.getpeername())
                sock.close()
                break

            msg = "ack{}.{}{}".format(
                sock.getpeername(),
                datetime.datetime.now().strftime("%Y%m%d-%H:%M:%S"),data.decode()).encode()

            #sock.send('ack{}'.format(data.decode()).encode())
            for s in self.clients.values():
                s.send(msg)

    def stop(self):
        for s in self.clients.values():
            s.close()
        self.sock.close()


cs = ChatServer()
cs.start()

while True:
    cmd = input(">>>")
    if cmd.strip() == 'quit':
        cs.stop()
        threading.Event.wait(3)
        break
    logging.info(threading.enumerate())