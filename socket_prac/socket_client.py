import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 9999)

client_socket.connect(server_address)

try:
    while True:
        data = input('SEND MESSAGE: ')

        if data == 'quit':
            break

        #메세지를 엔코딩해서 보내고 다시 받은걸 디코딩해서 나한테 표기해주느건가벼
        client_socket.sendall(data.encode())
        message = client_socket.recv(1024)

        print("SERVER MASSAGE: ", message.decode())
    
except OSError as e:
    print(f'socket err{e}')
    
client_socket.close()

#왜 try에서 오류?????????? 어이x
#해결했음 except ,finally 없어서 그랬구요~