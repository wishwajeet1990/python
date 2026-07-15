import time as t 
import sys
for i in sys.path:
    print(i)
    # t.sleep(1)
    
for i in sys.builtin_module_names:
    print(i)
    # t.sleep(1)
print('math' in sys.builtin_module_names)