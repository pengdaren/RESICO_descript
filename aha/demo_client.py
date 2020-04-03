import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.100.204', 10000))


def get_server(client_socket):
    while 1:
        content = client_socket.recv(2048).decode('utf-8')
        if content is not None:
            print(content)


threading.Thread(target=get_server, args=(client_socket,)).start()

while 1:
    inputInfo = input('').strip()
    if inputInfo is None or inputInfo is 'exit':
        break
    client_socket.send(inputInfo.encode('utf-8'))
