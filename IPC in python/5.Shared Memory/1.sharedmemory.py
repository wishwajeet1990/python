print("""--------------About Shared Memory--------------------------
      1. Normally, each process has its own memory space.
      2. Shared Memory = a memory region accessible by multiple processes.
      3. Faster than pipes/queues because data doesn’t need to be copied.
      4. Often used in real-time systems, multiprocessing, OS internals.""")

from multiprocessing import shared_memory
import numpy as np

# Create shared memory block
shm = shared_memory.SharedMemory(create=True, size=50000)
print(shm.name)
# Write into shared memory
buffer = np.ndarray((300,), dtype=np.uint16, buffer=shm.buf)
buffer[:] = np.arange(300)  # [0,1,2,3,4,5,6,7,8,9]

print("Parent wrote:", buffer)

# Attach to the same memory in another "process"
shm2 = shared_memory.SharedMemory(name=shm.name)
buffer2 = np.ndarray((300,), dtype=np.uint16, buffer=shm2.buf)
print("Child sees:", buffer2)

# Cleanup
shm.close()
shm.unlink()
