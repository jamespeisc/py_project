import logging
import socketserver
import threading


class MyHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print(self.request)
        print(self.client_address)
        print(self.server)
        print(self.__dict__)
        print(self.server.__dict__)
        for i in range(3):
            data, raddr = self.request.recvfrom(1024)
            print(data, self.client_address)
            msg = '{}.ack'.format(data).encode()
            self.request.send(msg)


# server = socketserver.ThreadingTCPServer(('0.0.0.0', 9999), MyHandler)
server = socketserver.TCPServer(('0.0.0.0', 9999), MyHandler)
print(server)
t = threading.Thread(target=server.serve_forever, name='echoserver')
t.start()

try:
    while True:
        cmd = input('>>>')
        if cmd.strip() == 'quit':
            server.server_close()
            break
except  Exception as e:
    logging.info(e)
except KeyboardInterrupt:
    import sys
    sys.exit(0)

