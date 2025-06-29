import logging
import socket

raddr = ("127.0.0.1", 9999)
client = socket.socket()
client.connect(raddr)
while True:
    data = client.recv(1024)
    print(data)
    if data.strip() == b'quit':
        break
    client.send(b'ack')
client.close()


class ChatClient:
    def __init__(self, rip='127.0.0.1', rport=9999):
        self.raddr = (rip, rport)
        self.sock = socket.socket()
        self.event = threading.Event()

    def start(self):
        self.sock.connect(self.raddr)
        threading.Thread(target=self.recv, name='recv').start()

    def recv(self):
        while not self.event.is_set():
            data = self.sock.recv(1024)
            logging.info(data)

    def send(self, msg: str):
        data = "{}\n".format(msg.strip()).encode()
        self.sock.send(data)

    def stop(self):
        self.sock.close()
        self.event.set()


import threading

def main():
    cc = ChatClient()
    cc.start()

    while True:
        cmd = input(">>>")
        if cmd.strip() =='quit':
            cc.stop()
            break
        cc.send(cmd)
        print(threading.enumerate())

if __name__ == '__main__':
    main()