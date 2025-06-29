import  socket

server = socket.socket(type=socket.SOCK_DGRAM) # udp
addr = ('192.168.142.135',9999)
# ss - anu

server.bind(addr)
# server.recv(1024)

data, raddr = server.recvfrom(1024)
server.sendto(b'ack',raddr) # udp 需要用sendto


# -----------------------------------

server = socket.socket(type=socket.SOCK_DGRAM) # udp
addr = ('192.168.142.135',9999)
# ss - anu

server.bind(addr) # 绑定本地用

server.connect(raddr) # udp 不真连接，可以用server.send

# server.sendto 随便发，不用考虑对方是否存在


# netstat -anp udp|find "9988" windows 查看进程

# echo "123abc" |nc -u 127.0.0.1 9988 linux 下发服务器数据