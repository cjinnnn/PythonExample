
def enumerate_test1():
    list = ["1111","2222","3333","4444","5555"]
    #튜플 형태로 반환. 그대로 받기
    for item in enumerate(list):
        print("data:", item)

def enumerate_test2():
    list = ["1111","2222","3333","4444","5555"]
    #튜플을 각각의 데이터로 받기
    for idx, val in enumerate(list):
        print("idx:",idx, "value:",val)
    

def enumerate_test3():
    list = ["1111","2222","3333","4444","5555"]
    #튜플을 각각의 데이터로 받기
    for idx, val in enumerate(list, start=10):
        print("idx:",idx, "value:",val)

if __name__ == "__main__":
    enumerate_test1()
    enumerate_test2()
    enumerate_test3()