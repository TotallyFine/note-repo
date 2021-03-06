# coding:utf-8
# TODO 1.多线程 2. 持久socket
import socket
from util import Request, response_request # 自己实现对请求进行解析，和相应请求
from datetime import datetime
from urllib.parse import unquote

def run_server(host='127.0.0.1', port=8001, max_in=1):
    # 实例化socket类
    with socket.socket() as s:
        # 设置socket在服务端关闭之后马上释放端口
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定host port
        s.bind((host, port))

        print('server start, welcome socket at port:', port, '\n')
        while(True):
            s.listen(max_in) # 设置最大连接数
            connection, addr = s.accept()
            print('create socket with: ', *addr)
            packet = ''
            buffer_size = 1024
            while(True):
                data = connection.recv(buffer_size)
                # print(data)
                data = data.decode()
                # print(data)
                packet += data
                if len(data) < buffer_size:
                    break

            if len(packet.split()) < 2:# 防止浏览器传送空请求
                continue

            r = Request(packet) # 根据请求内容生成request类
            print(str(datetime.now())[:19], *addr, r.method, r.path) # 显示log信息
            response = response_request(r)
            connection.sendall(response)
            # python tcp socket 分为同步套接字和异步套接字，缺省是同步套接字，recv在接受完数据或是遇到错误才会返回，所以如果不主动断开就一直是连接着的。
            # connection.close()

if __name__ == '__main__':
    run_server()
