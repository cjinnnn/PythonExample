
#가장 기초적인 필터링 방법 for문 뺑뺑이돌기
def list_filtering_for():
    data = [1,2,3,4,5,6,7,8,9,10]
    print("초기데이터:",data)

    #5보다 큰 수를 필터링
    filtered = []
    for x in data:
        if x > 5:
            filtered.append(x)
    print("5보다 큰 수:",filtered)

    #필터링 된 값을 제거
    for r in filtered:
        data.remove(r)
    print("제거후데이터", data)

#list comprehension 활용
def list_filtering_comprehension():
    data = [1,2,3,4,5,6,7,8,9,10]
    print("초기데이터:",data)

    # 문법 : data = [ ( 변수를 활용한 값 ) for ( 사용할 변수 이름 ) in ( 순회할 수 있는 값 ) if (조건)]
    filtered = [ e for e in data if e < 5 ]
    print("5보다 작은 수:",filtered)

    filtered = [ e for e in data if e > 3 and e < 7 ]
    print("3보다 크고, 7보다 작은 수:",filtered)

#filter 와 람다의 활용
def list_filtering_filter():
    data = [1,2,3,4,5,6,7,8,9,10]
    print("초기데이터:",data)

    #list 로 변환 후 출력한다.
    filtered = filter(lambda x: x > 4, data)
    print("4보다 큰 수:", list(filtered))
    filtered = filter(lambda x:x < 3, data)
    print("3보다 작은 수:", list(filtered))

    #filter() 로 리턴된 값은 filter 객체로, 프린트문으로 보면 데이터가 아니라 객체의 정보가 나온다.
    print(type(filtered), filtered)

if __name__ == '__main__':
    list_filtering_for()
    list_filtering_comprehension()
    list_filtering_filter()

