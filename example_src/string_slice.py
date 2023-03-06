
#문자열 뽑아쓰기
def string_slice():
    data = "0123456789ABCDEFGH"
    print("slice 데이터:", data, len(data),"글자")
    print("인덱싱활용:", data[0],data[1],data[10],data[11])
    print("맨처음글자:, 맨마지막글자", data[0],data[17])
    print("맨처음글자:, 맨마지막글자", data[0],data[-1])
    print("ABC출력:", f"{data[10]}{data[11]}{data[12]}")
    print("ABC출력:", data[10:13])
    print("ABC출력:", data[-8:-5])
    print("A~끝:", data[10:])
    print("A~끝:", data[-8:])
    print("0~9:", data[:10])
    print("전체출력:", data[:])

#문자 위치 인덱스
def string_find_index():
    data = "0123456789ABCDEFGH"
    print("find 0 위치:", data.find("0"))
    print("index 0 위치:", data.index("0"))
    print("find A 위치:", data.find("A"))
    print("index A 위치:", data.index("A"))

#문자 갯수 세기
def string_count():
    data = "0123456789ABCDEFGH0001122222222222222"
    print("0 갯수:", data.count("0"))
    print("1 갯수:", data.count("1"))
    print("2 갯수:", data.count("2"))

#문자열 나누기
def string_split():
    data = "abc def ghi* jkl mno pqr* stu vwx yz"
    print("split 데이터:",data)
    print("공백으로 split:", data.split(" "))
    print("* 로 split:",data.split("*"))

#문자열 바꾸기
def string_replace():
    data = "abcdefgggggg    h"
    print("replace 데이터:",data)
    print("g replace:",data.replace("gggggg","g"))
    print("공백 replace:",data.replace("    ",""))

#공백 없애기
def string_strip():
    data = "     hi!    "
    print("strip 데이터:",f"<{data}>")
    print("양쪽공백지우기:", f"<{data.strip()}>")
    print("왼쪽공백지우기:", f"<{data.lstrip()}>")
    print("오른쪽공백지우기:", f"<{data.rstrip()}>")

#소문자, 대문자
def string_lower_upper():
    data = "abcDEF"
    print("대소문자:",data)
    print("소문자:",data.lower())
    print("대문자:",data.upper())

if __name__ == '__main__':
    string_slice()
    string_find_index()
    string_count()
    string_split()
    string_replace()
    string_strip()
    string_lower_upper()

