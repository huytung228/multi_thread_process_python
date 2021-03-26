import multiprocessing
import time
import os
from datetime import datetime

class multi_process():
    def __init__(self):
        self.number_process = 2

        # Share memory with Array and Value
        # Array vaf Value la nhung object ma tat cac cac process deu co the truy cap
        self.array = multiprocessing.Array('i', 4)
        self.value = multiprocessing.Value('i')

        # Queue and Pipe
        self.parent_conn, self.child_conn = multiprocessing.Pipe()

        # Synchronization with lock
        self.lock = multiprocessing.Lock()

    def process_1(self, conn, lock):
        while True:
            lock.acquire()
            time.sleep(1)
            print(f"process with pid = {os.getpid()} running name {multiprocessing.current_process().name}")

            # Share memory
            self.value.value = datetime.now().minute

            # Pipe
            conn.send(f"send mess to child at {datetime.now().second}")
            # msg = conn.recv()
            # if msg == "END":
            #     break
            # print("Received the message from parent: {}".format(msg))
            lock.release()

    def process_2(self, conn, lock):
        while True:
            lock.acquire()
            time.sleep(2)
            print(f"process with pid = {os.getpid()} running name {multiprocessing.current_process().name}")

            # Share memory
            print(self.value.value)

            # Pipe
            msg = conn.recv()
            if msg == "END":
                break
            print("Received the message from parent: {}".format(msg))
            conn.send(f"send mess to parent at {datetime.now().second}")
            lock.release()

    def run_process(self):
        p1 = multiprocessing.Process(target=self.process_1, name="first process", args=(self.parent_conn,self.lock,))
        p2 = multiprocessing.Process(target=self.process_2, name="second process", args=(self.child_conn,self.lock,))
        p1.start()
        p2.start()
    
if __name__ == "__main__":
    mp = multi_process()
    mp.run_process()
    