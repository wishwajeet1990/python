#------------------------------------Syntax----------------------------

"""
thread = threading.Thread(target=print_hello, args=(), kwargs={}, name='MyThread', daemon=False)
thread.start()
thread.join()

1. target: The function or callable object that the thread will execute.
2. args: A tuple containing the positional arguments to pass to the target function.
3. kwargs: A dictionary containing the keyword arguments to pass to the target function.
4. name: (Optional) A string name for the thread. If not set, Python assigns a default unique name.
5. daemon: (Optional) A boolean indicating whether the thread is a daemon thread (background thread). If True, the thread won’t block program exit.
6. group: Currently unused and should be set to None.

thread.start()
    This method starts the thread's activity.
    It invokes the thread’s run() method in a separate thread of control.
    The call to start() is non-blocking and returns immediately, allowing the thread to run concurrently with the caller.
  
  ***A thread can only be started once; calling start() again will raise an exception.

thread.join(timeout=None)
    This method blocks the calling thread until the thread whose join() is called terminates or optionally until the specified timeout expires.
    Useful to wait for a thread to complete before proceeding.
    If timeout is not specified or None, it waits indefinitely.

***Calling join() before start() raises a RuntimeError.
    For example, thread.join() ensures the main program waits for the thread to finish.
"""

import threading,time
my_num = 1
# loop = 1000000

def count_inc():
    global my_num
    for a in range(10):
        print(f"{my_num} in INC")
        time.sleep(1)
        my_num+=1

def count_dec():
    global my_num
    for a in range(10):
        time.sleep(2)
        my_num-=1
        print(f"{my_num} in dec",)

if __name__ == "__main__":
    thread1 = threading.Thread(target=count_inc,args=())
    thread2 = threading.Thread(target=count_dec,args=())
    # thread1.join()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
print(my_num)