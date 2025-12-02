print("""--------------------Some Basic function used in message queue-------------
      
1. q.put(item)                      :-      Put item in queue (can block).
2. q.put(item, block=False)	    :-      Non-blocking, raises queue.Full if full.
3. q.get()	                    :-      Get item from queue (can block).
4. q.get(block=False)               :-  	Non-blocking, raises queue.Empty if empty.
5. q.qsize()	                    :-      Returns approx size of queue.
6. q.empty()	                    :-      Returns True if queue is empty.
7. q.full()	                    :-      Returns True if queue is full.
8. q.close()	                    :-      Close the queue (no more data can be added).
9. q.cancel_join_thread()	    :-      Prevents join on queue thread.

--------------------------------EOF--------------------------------------------""")
