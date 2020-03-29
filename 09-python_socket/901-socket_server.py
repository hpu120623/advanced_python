"""
推荐阅读：《tcp/ip》详解
五层网络模型：应用层（http），传输层（tcp/udp），网络层，数据链路层，物理层
http：应用层协议
tcp/udp：tcp三次握手，四次挥手
socket：不属于计算机网络中的协议，连接应用层和传输层，可以使我们自己的应用直接和tcp打交道，可以实现自己的协议
"""
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()

def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024)
        print(data.decode('utf8'))
        re_data = input()
        sock.send(re_data.encode('utf8'))

# 获取从客户端发送的数据
# 一次获取1k的数据
while True:
    sock, addr = server.accept()
    # 用线程去处理新接收的连接（用户）
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()



    # data = sock.recv(1024)
    # print(data.decode('utf8'))
    # re_data = input()
    # sock.send(re_data.encode('utf8'))
    # server.close()
    # sock.close()