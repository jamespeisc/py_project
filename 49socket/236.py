import socketserver


class MyHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print(self.request)
        print(self.client_address)
        print(self.server)
        print(self.__dict__)
        print(self.server.__dict__)
        for i in range(3):
            data,raddr = self.request.recvfrom(1024)
            print(data,self.client_address)




server = socketserver.ThreadingTCPServer(('0.0.0.0', 9999), MyHandler)
print(server)
server.serve_forever()
