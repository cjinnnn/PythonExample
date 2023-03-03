
def test_list():
    lq = []
    lq.append(1)
    lq.append(2)
    lq.append(3)
    print("list",lq)
    data = lq.pop(0)
    print("pop data",data)
    print("list",lq)


#양방향 추가 가능 (앞뒤)
from collections import deque
def test_dque():
    dq = deque()

    #추가
    dq.append(1)
    dq.append(2)
    dq.append(3)
    print("queue",dq)
    
    #data 빼내기
    data = dq.popleft()
    print("pop data",data)
    print("queue",dq)

    #맨 앞에 추가
    dq.appendleft(4)
    print("queue",dq)


#단방향 FIFO
from queue import Queue
def test_queue_fifo():
    q = Queue()

    #추가
    q.put(1)
    q.put(2)
    q.put(3)
    print("queue",q)
    
    #data 빼내기
    data = q.get()
    print("pop data",data)

#단방향 LIFO
from queue import LifoQueue
def test_queue_lifo():
    q = LifoQueue()

    #추가
    q.put(1)
    q.put(2)
    q.put(3)
    print("queue",q)
    
    #data 빼내기
    data = q.get()
    print("pop data",data)

from queue import PriorityQueue
def test_queue_priority():
    q = PriorityQueue()

    # 가장 작은 값이 우선순위가 높음.
    # 튜플로 (우선순위, 값) 의 형태로 넣을 수도있음.
    q.put(12)
    q.put(11)
    q.put(13)
    print("queue",q)
    
    #data 빼내기
    data = q.get()
    print("pop data",data)


if __name__ == "__main__":
    test_list()
    test_dque()
    test_queue_fifo()
    test_queue_lifo()
    test_queue_priority()