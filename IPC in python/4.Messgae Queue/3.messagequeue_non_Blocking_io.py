from multiprocessing import Process, Queue
import time

def sender(q):
    for i in range(5):
        msg = f"Message {i}"
        print(f"Sender: {msg}")
        q.put(msg)   # put message in queue
        time.sleep(1)
    q.put("quit")

def receiver(q):
    while True:
        msg = q.get(block=False)   # read message from queue if there else ir raise empty queue and return back will not hold here
        print(f"Receiver got: {msg}")
        if msg == "quit":
            break

if __name__ == "__main__":
    q = Queue()

    p1 = Process(target=sender, args=(q,))
    p2 = Process(target=receiver, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("Programme End here")
    
