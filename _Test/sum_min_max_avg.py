def sum_min_max_avg():
    list = [1,2,3,4,5]
    print("초기값",list)

    print("sum: ", sum(list))
    print("min: ", min(list))
    print("max: ", max(list))
    print("avg: ", avg(list))

#평균을 구한다.
def avg(data):
    return sum(data) / len(data)

if __name__ == '__main__':
    sum_min_max_avg()
