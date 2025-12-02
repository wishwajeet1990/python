import threading, time

lock1 = threading.Lock()
lock2 = threading.Lock()

def task1():
    lock1.acquire()
    print("Task1 got lock1")
    lock2.acquire()   # waits forever
    print("Task1 got lock2")
    lock2.release()
    lock1.release()

def task2():
    lock2.acquire()
    print("Task2 got lock2")
    lock1.acquire()   # waits forever
    print("Task2 got lock1")
    lock1.release()
    lock2.release()

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()
