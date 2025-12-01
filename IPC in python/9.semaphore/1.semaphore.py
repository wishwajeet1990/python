#Semaphore
print("""----------------Semaphore Property--------------------
      1. Semaphore = counter-based lock.
      2.Allows N threads to access a resource at the same time.
      3.When counter reaches 0, new threads block until one releases.
      """)

import threading, time

sem = threading.Semaphore(2)  # allow max 2 threads at a time

def worker(n):
    with sem:  # acquire automatically
        print(f"Thread {n} entered")
        time.sleep(1)
        print(f"Thread {n} leaving")

for i in range(5):
    threading.Thread(target=worker, args=(i,)).start()
