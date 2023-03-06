
#가장 기초적인 필터링 방법 for문 뺑뺑이돌기
def dict_filtering_for():
    data = {1:"일",2:"이",3:"삼",4:"사",5:"오",6:"육",7:"칠",8:"팔",9:"구",10:"십"}
    print("초기데이터:",data)

    #5보다 큰 수를 필터링
    filtered = {}
    for key, val in data.items():
        if key > 5:
            filtered[key] = val
    print("5보다 큰 수:",filtered)

    #필터링 된 값을 제거
    for key in filtered.keys():
        data.pop(key)
        #del data[key] #이것으로 사용해도 됨.
    print("제거후데이터", data)

#dict comprehension 활용
def dict_filtering_comprehension():
    data = {1:"일",2:"이",3:"삼",4:"사",5:"오",6:"육",7:"칠",8:"팔",9:"구",10:"십"}
    print("초기데이터:",data)

    # 문법 : data = { 키:값 for 키, 값 in 딕셔너리데이터.items() if (조건) }
    filtered = {k:v for k, v in data.items() if k < 5 }
    print("5보다 작은 수:",filtered)

    filtered = { k:v for k, v in data.items()  if k > 3 and k < 7 }
    print("3보다 크고, 7보다 작은 수:",filtered)

#filter 와 람다의 활용
def dict_filtering_filter():
    data = {1:"일",2:"이",3:"삼",4:"사",5:"오",6:"육",7:"칠",8:"팔",9:"구",10:"십"}
    print("초기데이터:",data)

    #dict 로 변환 후 출력한다.
    filtered = filter(lambda x: x[0] > 4, data.items())
    print("4보다 큰 수:", dict(filtered))
    filtered = filter(lambda x: x[0] < 3, data.items())
    print("3보다 작은 수:", dict(filtered))

    #filter() 로 리턴된 값은 filter 객체로, 프린트문으로 보면 데이터가 아니라 객체의 정보가 나온다.
    print(type(filtered), filtered)

if __name__ == '__main__':
    dict_filtering_for()
    dict_filtering_comprehension()
    dict_filtering_filter()

