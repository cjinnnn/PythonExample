
#bytes 를 사용해서 bytes 로 변환한다.
def to_bytes_bytes():
    txt = "to_bytes_bytes."
    print(type(txt), txt)
    bin = bytes(txt, 'utf-8')
    print(type(bin), bin)

#encode 를 사용해서 bytes 로 변환한다.
def to_bytes_encode():
    txt = "to_bytes_encode."
    print(type(txt), txt)
    bin = txt.encode('utf-8')
    print(type(bin), bin)


#decode 를 사용해서 string 으로 변환한다.
def to_string_decode():
    bin = b"to_string_decode."
    print(type(bin), bin)
    
    txt = bin.decode('utf-8')
    print(type(txt), txt)

#str 을 사용해서 string 으로 변환한다.
def to_string_str():
    bin = b"test byte to string."
    print(type(bin), bin)
    
    txt = str(bin, 'utf-8')
    print(type(txt), txt)

if __name__ == '__main__':
    to_bytes_bytes()
    to_bytes_encode()
    to_string_decode()
    to_string_str()
