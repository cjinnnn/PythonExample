
#2진수 문자열을 10진수로 변환
def metohd_2_to_10():
    txt = "01010101"
    dec = int(txt, 2)
    display(dec)

#8진수 문자열을 10진수로 변환
def metohd_8_to_10():
    txt = "100"
    dec = int(txt, 8)
    display(dec)

#10진수 문자열을 10진수로 변환
def metohd_10_to_10():
    txt = "100"
    dec = int(txt, 10) #10생략가능.
    display(dec)

#16진수 문자열을 10진수로 변환
def metohd_16_to_10():
    txt = "FF"
    dec = int(txt, 16)
    display(dec)

#정수값을 각각 방식으로 표현
def display(dec):
    # 표현방식을 알려주기 위해 b,o,d,x 붙임.
    print(f"2진수: '0b{dec:b}'")
    print(f"8진수: '0o{dec:o}'")
    print(f"10진수: '0d{dec:d}'")
    print(f"16진수: '0x{dec:x}'")

#10진수를 2진수 문자열로 변환
def metohd_10_to_2():
    dec = 10
    txt = bin(dec)
    print("10진수를 2진수로:",txt)

#10진수를 8진수 문자열로 변환
def metohd_10_to_8():
    dec = 10
    txt = oct(dec)
    print("10진수를 8진수로:",txt)

#10진수를 10진수 문자열로 변환
def metohd_10_to_str10():
    dec = 100
    txt = str(dec)
    print("10진수를 10진수로:",txt)

#10진수를 16진수 문자열로 변환
def metohd_10_to_16():
    dec = 10
    txt = hex(dec)
    print("10진수를 16진수로:",txt)
    

if __name__ == '__main__':
    #진수 표현 방법
    display(10)

    #문자열을 정수로 변경 후 출력
    metohd_2_to_10()
    metohd_8_to_10()
    metohd_10_to_10()
    metohd_16_to_10()

    #정수를 문자열로 변환
    metohd_10_to_2()
    metohd_10_to_8()
    metohd_10_to_str10()
    metohd_10_to_16()
