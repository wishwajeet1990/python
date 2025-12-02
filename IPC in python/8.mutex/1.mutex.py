# Mutex (Lock in Python)
"""
Mutex = Mutual Exclusion
Only one thread/process can hold it at a time.
Prevents race conditions by locking critical sections.
"""

import threading

lock = threading.Lock()
counter = 0


def task():
    global counter
    for _ in range(1000000):
        lock.acquire()
        counter += 1
        lock.release()
def task2():
    global counter
    for _ in range(100000):
        lock.acquire()
        counter -= 1
        lock.release()

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task2)
t1.start(); t2.start()
t1.join(); t2.join()

print("Final Counter:", counter)
