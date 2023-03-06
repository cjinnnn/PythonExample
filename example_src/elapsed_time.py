import time

def test_process():
    for x in range(10000000):
        pass
    time.sleep(1)

def elapsed_test_time():
    start = time.time()

    test_process()

    end = time.time()
    elapsed = end - start
    print(f"start:{start} end:{end}")
    print(f"time() 경과시간 : {elapsed}")

def elapsed_test_process_time():
    start = time.process_time()
    
    test_process()

    end = time.process_time()
    elapsed = end - start
    print(f"start:{start} end:{end}")
    print(f"process_time() 경과시간 : {elapsed}")

def elapsed_test_perf_counter():
    start = time.perf_counter()
    
    test_process()

    end = time.perf_counter()
    elapsed = end - start
    print(f"start:{start} end:{end}")
    print(f"perf_counter() 경과시간 : {elapsed}")

def elapsed_test_monotonic():
    start = time.monotonic()
    
    test_process()

    end = time.monotonic()
    elapsed = end - start
    print(f"start:{start} end:{end}")
    print(f"monotonic() 경과시간 : {elapsed}")

def getelapsedtime(t): #함수로 만들어 놓으면 사용하기 편하다.
    elapsed = time.time() - t
    return elapsed

if __name__ == "__main__":
    print("===== time() ====")
    elapsed_test_time()
    print("===== process_time() ====")
    elapsed_test_process_time()
    print("===== perf_counter() ====")
    elapsed_test_perf_counter()
    print("===== monotonic() ====")
    elapsed_test_monotonic()

    print("===== 함수테스트 (1,2,3차)====")
    t = time.time()
    test_process()
    elapsed1 = getelapsedtime(t)
    test_process()
    elapsed2 = getelapsedtime(t)
    test_process()
    elapsed3 = getelapsedtime(t)

    print(f"경과시간: {elapsed1} > {elapsed2} > {elapsed3}")