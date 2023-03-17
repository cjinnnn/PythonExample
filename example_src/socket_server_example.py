import socket
import threading

# 서버 정보
HOST = 'localhost'
PORT = 9999

def handle_client(client_socket, address):
    # 클라이언트의 연결 처리
    print(f"[NEW CONNECTION] {address} connected.")
    msg = 'Welcome to the server!'
    client_socket.send(msg.encode('utf-8'))

    while True:
        # 클라이언트로부터 메시지 수신
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"[{address}] {data.decode('utf-8')}")
        except:
            break

    # 클라이언트와 연결 종료
    print(f"[DISCONNECTED] {address} disconnected.")
    client_socket.close()

def start_server():
    # 서버 소켓 생성
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"[SERVER STARTED] Listening on {HOST}:{PORT}")

    while True:
        # 클라이언트 연결 대기
        client_socket, address = server_socket.accept()

        # 새로운 스레드 생성하여 클라이언트 연결 처리
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()

if __name__ == '__main__':
    start_server()