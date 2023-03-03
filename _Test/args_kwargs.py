
def TestFunc(*args, **kargs):
    print("*args  :", args)
    print("**kargs:", kargs)
    print("----")

def TestFunc2(*args):
    print("*args  :", args)

def TestFunc3(**kargs):
    print("**kargs:", kargs)

if __name__ == '__main__':
    print("=== TestFunc(*args, **kargs)")
    TestFunc(1)
    TestFunc(1,2,3)
    TestFunc(name="hong")
    TestFunc(name="hong",age=20)
    TestFunc(1,2,3, name="hong",age=20)

    print("=== 이렇게넣으면? ===")
    TestFunc(1,2,3,["name","hong"])
    TestFunc(1,2,3,{"name":"hong"})

    print("=== 하나더해봅니다 ===")
    TestFunc2(1)
    TestFunc3(name="hong")

    # 오류발생 예
    # TestFunc2(name="hong")
    # TestFunc3(1)
