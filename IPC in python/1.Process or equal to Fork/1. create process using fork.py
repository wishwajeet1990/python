#Fork is used to create a new child process this is unix/linux based command
#in Windows we use process command to create new process

import multiprocessing as mp
import os 
import time as t
print(f"Process Started {__name__}")        #here module name will be __main__

def child_process():
    print(f"Parent Process ID =  {os.getppid()}\nChild Process ID  =  {os.getpid()} ")
    # print(__name__)
    
if __name__ == "__main__":          # We use this line because when the new process is being created 
                                    #it start executing by re importing the main module again and again 
                                    #So to avoid the re importing we use this line because every module has is own name 
    print(f"Process ID  = {os.getpid()}")
    for i in range(3):
        new_process = mp.Process(target=child_process)      #here module name will be __mp_main__
        new_process.start()         #This tells Python to start the new process
        new_process.join()          #This tells the parent process to wait until the child process finishes
        t.sleep(1)
        print()
    print("Child process finished")
    