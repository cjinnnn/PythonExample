
def list_compare():
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = [3, 2, 1]
    list4 = [4, 5, 6]

    print("[기본] 값 순서 모두 같은 리스트 비교 : ", list1 == list2)
    print("[기본] 값은 같지만 순서가 다른 리스트 비교 : ", list1 == list3)
    print("[기본] 값 순서 모두 다른 리스트 비교 : ", list1 == list4)

def list_compare_sort():
    list1 = [1, 2, 3]
    list2 = [3, 2, 1]
    print("[sort] 순서가 다른 리스트 sort전 리스트 비교 : ", list1 == list2)
    print("[sort] sort후 순서가 같아진 리스트 비교 : ", list1.sort() == list2.sort())

def list_compare_set():
    list1 = [1, 2, 3]
    list2 = [3, 2, 1]
    print("[set] 순서가 다른 리스트 비교 : ", list1 == list2)
    print("[set] set으로 변경 후 비교 : ", set(list1) == set(list2))

import collections
def list_compare_collection_counter():
    list1 = [1, 1, 1, 2, 3]
    list2 = [3, 2, 1, 1, 1]
    print("[collections.counter] 순서가 다른 리스트 비교 : ", list1 == list2)
    print("[collections.counter] collections.counter 비교 : ", collections.Counter(list1) == collections.Counter(list2))
    print(collections.Counter(list1))
    print(collections.Counter(list2))


if __name__ == '__main__':
    list_compare()
    list_compare_sort()
    list_compare_set()
    list_compare_collection_counter()