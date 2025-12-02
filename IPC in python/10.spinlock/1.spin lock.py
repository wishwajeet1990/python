# Spin Lock
print("""-------------------------Spin Lock-----------------------------------------
      1. spin lock = Lock where threads busy-wait (keep checking) until lock is free.
      2. Useful in low-latency systems where context-switching overhead is higher than spinning.
      3. Python doesn't have a built-in spinlock, but we can simulate it:""")

import threading, time

class SpinLock:
    def __init__(self):
        self.locked = False
        self._lock = threading.Lock()

    def acquire(self):
        while True:
            with self._lock:
                if not self.locked:
                    self.locked = True
                    return
            # busy-wait (spin)
            time.sleep(1)  

    def release(self):
        with self._lock:
            self.locked = False


spinlock = SpinLock()
counter = 0

def task():
    global counter
    for _ in range(1000000):
        spinlock.acquire()
        counter += 1
        spinlock.release()

threads = [threading.Thread(target=task) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()

print("Final Counter:", counter)
