import os

if __name__ == '__main__':
    # print(os.environ)
    # print(os.environ["PATH"])
    # print(os.environ["LANG"])

    # print(os.getcwd())

    path = "/home/cjinnnn/Downloads"
    os.chdir(path)
    # print(os.getcwd())

    #대상 경로의 파일리스트 반환
    print(os.listdir())
    print(os.listdir(path))

    #대상 경로의 파일 및 디렉토리 반환 (하위디렉토리 포함)
    for x in os.walk(path):
        print(x)



    # os.mkdir("/home/cjinnnn/Downloads/test1")
    # path = "/home/cjinnnn/Downloads/test1"
    # file = os.path.join(path,"test.png")
    # # os.mkdir(path) #오류발생
    # os.makedirs(path)
    # os.remove(file)
    # os.rmdir(path)
    # import shutil
    # shutil.rmtree(path)

    # path = "/home/cjinnnn/Downloads/test1"
    # print(os.path.basename(path))

    #현재 코드의 파일 경로
    # print(os.path.dirname(__file__))

    #test1 이 있는 디렉토리의 경로
    
    # print(os.path.dirname(path))

    # print(os.path.split(__file__))
    # print(os.path.split(__file__)[0])
    # print(os.path.split(__file__)[1])

    # print(os.path.exists(__file__))
    # path = "/home/cjinnnn/Downloads/test1"
    # print(os.path.exists(path))
    # print(os.path.exists( os.path.join(path,"1.png")))

    # path = "/home/cjinnnn/Downloads/test1"
    # file = os.path.join(path,"1.png")
    # print(os.path.isfile(path))
    # print(os.path.isfile(file))
    # print(os.path.isdir(path))
    # print(os.path.isdir(file))

    # path = os.path.join("test1","test2","test3","test4", "1.png")
    # print(path)

