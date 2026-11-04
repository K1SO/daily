import socket

#IPV4 방식 설정 TCP연결하겠음 뜻임-------V------------V
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#소켓 정보세팅(튜플이라는데 이렇게 쓰는법이있네)
server_address = ('127.0.0.1', 9999)
print("Start up on {} Port {}".format(*server_address))

server_socket.bind(server_address)
server_socket.listen()

while True:
    print('accept wait...')
    client_socket, client_adress = server_socket.accept()
    print("Client Access: ", client_adress)

    try: 
        while True:
            data = client_socket.recv(1024)

            if not data: 
                break

            message = data.decode()
            print("Client Message: ", message)


            #VVV 이게 왜 있는거임? 왜 sendall을 쓰는거야? 받았다고 답장해주는건가?
            # 아 그냥 체크용도임 client에게 이런 메세지 받았다고 확인
            #이걸 에코통신이라고 하내ㅔ요~
            client_socket.sendall(f'Server recv Message: {message}'.encode())

    except OSError as e:
        print("socket err ",e)

    finally:
        client_socket.close()
        print("###Client Disconnection###")




"""    try:
        data = client_socket.recv(1024)
        data = data.decode()

    except Exception as err :
        client_socket.close()
        break

    finally:
        client_socket.close()
        break
"""
"""def recv_message():
    message = client_socket.recv(1024)
    message = message.decode()

start_new_thread(recv_message, (client_socket))"""
#>>> 이게 뭐야