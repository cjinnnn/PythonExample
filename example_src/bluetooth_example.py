"""
설치:
sudo apt-get install python3-dev python3-pip libbluetooth-dev
sudo pip3 install pybluez

설명:
위 코드 예제는 "SampleServer"라는 이름을 가진 Bluetooth 서버를 검색하고 첫 번째로 발견된 서버에 연결하여 "Hello World!"라는 문자열을 전송하는 예제입니다.
참고로 이 코드는 Python 3.x 환경에서 실행되어야 합니다. Python 2.x 환경에서는 PyBluez 대신 bluetooth 모듈을 사용해야 합니다.
"""

import bluetooth

# 서비스 검색
service_matches = bluetooth.find_service(name='SampleServer',
                                          uuid=bluetooth.SERIAL_PORT_CLASS)

if len(service_matches) == 0:
    print("No services found")
    exit(0)

# 첫 번째 서비스 선택
first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("Connecting to \"%s\" on %s" % (name, host))

# Bluetooth 통신 연결
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((host, port))

# 데이터 전송
sock.send("Hello World!")

# Bluetooth 통신 종료
sock.close()
