class Person():
    def __init__(self, name, age):
        self.Name = name
        self.Age = age
    def __repr__(self):
        return f"[{self.Name}, {self.Age}]"

def list_sort():
    list = [2,4,1,3,5]
    print("기본정렬",list)
    list.sort()
    print("오름차순",list)
    list.sort(reverse=True)
    print("내림차순",list)

    #region test
    print(sum(list))
    print(min(list))
    print(max(list))
    #endregion
    print((list))
    

    

def list_people_sort():
    people = []
    people.append( Person("홍길동", 23) )
    people.append( Person("강나래", 22) )
    people.append( Person("이승길", 21) )
    print("기본 정렬    ", people)

    # 이름 오름차순 (Ascending)
    people.sort(key=lambda x: x.Name)
    print("이름 오름차순", people)

    # 이름 내림차순 (Descending)
    people.sort(key=lambda x: x.Name, reverse=True)
    print("이름 내림차순", people)

    # 나이 오름차순 (Ascending)
    people.sort(key=lambda x: x.Age)
    print("나이 오름차순", people)

    # 나이 내림차순 (Descending)
    people.sort(key=lambda x: x.Age, reverse=True)
    print("나이 내림차순", people)

if __name__ == '__main__':
    list_sort()
    list_people_sort()

