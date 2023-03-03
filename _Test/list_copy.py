import time

#객체 참조는 대상과 원본이 동일하여, 어느한쪽에서 데이터를 바꾸면 같이 바뀐다.
#얕은 복사는 1차원 리스트에서는 문제가 발생하지 않지만, 2차원 리스트부터는 문제가 생긴다.
#깊은 복사는 문제가 발생하지 않는다.

def reference():
    src_list = [0, 1, 2, [10,11,12]]
    copied_list = src_list  #이렇게 하면 같은놈
    copied_list[0] = -1     #얘도 바뀌고
    copied_list[3][0] = -1  #얘도 바뀐다
    print("== copied_list = src_list")
    print(src_list)
    print(copied_list)

def shallow_copy_01():
    src_list = [0, 1, 2, [10,11,12]]
    copied_list = list(src_list)
    copied_list[0] = -1     #1차원인 얘는 원본을 유지한다
    copied_list[3][0] = -1  #2차원인 얘는 원본도 바뀐다
    print("== copied_list = list(src_list)")
    print(src_list)
    print(copied_list)

def shallow_copy_02():
    src_list = [0, 1, 2, [10,11,12]]
    copied_list = src_list.copy()
    copied_list[0] = -1     #1차원인 얘는 원본을 유지한다
    copied_list[3][0] = -1  #2차원인 얘는 원본도 바뀐다
    print("== copied_list = src_list.copy()")
    print(src_list)
    print(copied_list)

from copy import copy
def shallow_copy_03():
    src_list = [0, 1, 2, [10,11,12]]
    copied_list = copy(src_list)
    copied_list[0] = -1     #1차원인 얘는 원본을 유지한다
    copied_list[3][0] = -1  #2차원인 얘는 원본도 바뀐다
    print("== copied_list = copy(src_list)")
    print(src_list)
    print(copied_list)

from copy import deepcopy
def deep_copy_01():
    src_list = [0, 1, 2, [10,11,12]]
    copied_list = deepcopy(src_list)
    copied_list[0] = -1     #원본유지
    copied_list[3][0] = -1  #원본유지
    print("== copied_list = deepcopy(src_list)")
    print(src_list)
    print(copied_list)

if __name__ == '__main__':
    reference()
    shallow_copy_01()
    shallow_copy_02()
    shallow_copy_03()
    deep_copy_01()
    

