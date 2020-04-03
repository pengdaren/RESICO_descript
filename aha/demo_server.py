import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建服务器socket
server_socket.bind(('192.168.100.204', 10000))  # 绑定ip和端口号
server_socket.listen()       # 监
client_list = []
c, addr = server_socket.accept()  # 接


def send_manage(c):
    while 1:
        content = str(c.recv(2048).decode('utf-8'))
        print(content)
        for cl in client_list:
            cl.send(content.encode('utf-8'))


while 1:             # 接
    getManage = c.recv(2048).decode('utf-8')
    print('收到来自于', addr, '信息  ', getManage)
    client_list.append(c)
    threading.Thread(target=send_manage, args=(c,)).start()

