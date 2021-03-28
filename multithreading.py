import threading
import time
from queue import Queue

def thread1_func(lock,q):
    count = 1
    while True:
        lock.acquire()
        print(q.qsize())
        time.sleep(1)
        q.put(count)
        print(f"thread {threading.current_thread().name} putted {count} to queue")
        count += 1
        lock.release()

def thread2_func(lock, q):
    while True:
        lock.acquire()
        time.sleep(1)
        if not q.empty():
            count = q.get()
        print(f"thread {threading.current_thread().name} getted {count} from queue")
        lock.release()

lock = threading.Lock()
q = Queue()

t1 = threading.Thread(target=thread1_func, name="huytung", args=(lock,q,))
t2 = threading.Thread(target=thread2_func, name="maidinh", args=(lock,q,))

if __name__ == '__main__':
    t1.start()
    t2.start()

