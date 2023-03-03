import threading
import time

#시간을 출력하는 함수
start_time = time.time()
def sec():
    elapsed_time = time.time() - start_time
    return "[시간 %.02f 초]"%(elapsed_time)

#스레드 함수
def event_wait_thread(name, event:threading.Event):
    print(f"{sec()}: {name} start.")
    while event.wait():
        for x in range(0,3):
            print(f"{sec()}: {x} 이요~~!")
        event.clear()
        print(f"{sec()}: event clear()")

def main():
    evt = threading.Event()

    th1 = threading.Thread(target=event_wait_thread, args=("Thread 1", evt), daemon=True)
    th1.start()

    cnt = 0
    while cnt < 3:
        cnt += 1
        print(f"{sec()}: main() event set()")
        evt.set()
        time.sleep(3)

    print(f"{sec()}: main() 프로그램 종료!")

if __name__ == "__main__":
    main()