#A pipe is the oldest method of the inter process communication (IPC)
#it is TWO end point connection between wo process.
#Created using PIPE command 
#Creating a chat bot using PIPE

"""
1. One Process write into the pipe 
2. Another process read from the pipe    
    """

from multiprocessing import Process, Pipe
import time as t
def process2(conn):
    while True:
        msg = conn.recv()  # wait for P1
        print(f"Process1 said: {msg}")
        if msg.lower() == "quit":
            break
        # Instead of using input() here (which fails in child),
        # we send a request back for Process1 to take input.
        conn.send("your_turn")

if __name__ == "__main__":
    conn1, conn2 = Pipe()

    p2 = Process(target=process2, args=(conn2,))
    p2.start()
   
    while True:
        msg = input("Process1: ")
        conn1.send(msg)
        if msg.lower() == "quit":
            break
        t.sleep(1)
        signal = conn1.recv()
        if signal == "your_turn":
            reply = input("Process2: ")
            conn1.send(reply)
            if reply.lower() == "quit":
                break

    p2.join()
    print("Chat Ended ✅")

