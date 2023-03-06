#! /usr/bin/env python3
import socket
import json
import threading
import time
from enum import IntEnum


MAX_BUFFER = 4096
lock = threading.Lock()

#서버에서 사용되는 클라이언트 소켓
class Client(threading.Thread):
    def __init__(self, server, client, address, id, name, signal):
        threading.Thread.__init__(self)
        self.server:server_module = server
        self.client:socket.socket = client
        self.address = address
        self.id = id
        self.name = name
        self.signal = signal
        print("New connection at ID " + str(self.__str__()))
    
    def __str__(self):
        name = f"{self.address}_{self.id}"
        return name

    def remove(self):
        lock.acquire()
        self.client.close()
        self.signal = False
        self.server.connections.remove(self)
        lock.release()

    def run(self):
        while self.signal:
            try:
                data = self.client.recv(MAX_BUFFER)
                print(f"[{self} RCV:] {data}")
                if not data:
                    print("Client recv not data !" + str(self.address) + " has disconnected")
                    self.client.close()
                    self.signal = False
                    self.remove()
                    break
            except:
                print("Client recv Exception! " + str(self.address) + " has disconnected")
                self.signal = False
                self.remove()
                break
            #처리
            self.ProcessData(data)

    def ProcessData(self, data):
        data = data.decode("utf-8")
        for client in self.server.connections:
            client.send(data)

    def send(self, data):
        if self.signal == True and self.client != None:
            try:
                data = str.encode(data) #bytes(data, 'utf-8')
                self.client.sendall(data)
            except Exception as e:
                print("Client send exception !" + str(self.address) + " has disconnected")
                self.client.close()
                self.signal = False
                self.remove()
        else:
            print("Client send close !" + str(self.address) + " has disconnected")
            self.client.close()
            self.signal = False
            self.remove()

#서버 IP
def GetHostIp():
    #구글IP 접속시도해보고, 실제 통신하는 IP 알아냄. (인터넷 연결 안되어도 됨)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

#서버 모듈
class server_module():
    def __init__(self):
        self.Ip = GetHostIp()
        self.Port = 20001
        self.connections = []
        self.id = 0

        self.server:socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.Ip, self.Port))
        self.server.listen(999)

        newConnectionsThread = threading.Thread(target = self.newConnections, args = (self.server,))
        newConnectionsThread.start()

    def newConnections(self, socket:socket.socket):
        while True:
            sock, address = socket.accept()
            name = f"{address}_{self.id}"

            lock.acquire()
            self.connections.append(Client(self, sock, address, self.id, name, True))
            sock_index = len(self.connections) - 1
            self.connections[sock_index].start()
            self.id += 1
            lock.release()

#테스트 클라이언트 (참조용 코드)
class test_client():
    def __init__(self, ip, port):
        self.client = None
        self.signal = False

        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((ip, port))
            self.signal = True
        except:
            print("Could not make a connection to the server")

        receiveThread = threading.Thread(target = self.receive, args = (self.client, True))
        receiveThread.start()

        sendThread = threading.Thread(target = self.send_data)
        sendThread.start()

    def receive(self, client, signal):
        while signal:
            try:
                data = client.recv(MAX_BUFFER)
                print("[test_client RCV]",str(data.decode("utf-8")))
                if not data:
                    self.client.close()
                    self.signal = False
                    break
            except:
                print("You have been disconnected from the server")
                signal = False
                break

    def send_data(self):
        send_count = 3 #세번만 전송하고 죽어라.
        while True:
            message = "client -> server send data!"
            self.client.sendall(str.encode(message))
            send_count -= 1
            if send_count <= 0:
                self.client.close()
                self.signal = False
                break
            time.sleep(1)

def main():
    #내부 IP
    hostname = socket.gethostname()
    host_address = socket.gethostbyname(hostname)

    #구글IP 접속시도해보고, 실제 통신하는 IP 알아냄. (인터넷 연결 안되어도 됨)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    
    print(hostname, host_address, ip)

    server = server_module()

    while True:
        time.sleep(0.2)
        key = input("(a: 클라이언트 추가, q: 종료) : ")
        if key == "q":
            break
        elif key == "a":
            client = test_client(ip, 20001)
        elif key == 's':
            for c in server.connections:
                data = f"server -> client : send data!"
                c.send(data)
            print("코넥션 수량 : ", len(server.connections))
        else:
            try:
                pass
            except Exception as e:
                print(e)

    exit(0)
 
if __name__ == '__main__':
    main()