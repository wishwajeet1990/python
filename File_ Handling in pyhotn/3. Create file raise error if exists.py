import os
import time
file = open(r"D:\Python\Codding\File_ Handling\ my_file_3.txt","w")         #Create new File without error
time.sleep(1)
file.close()
time.sleep(1)
try:
    file = open(r"D:\Python\Codding\File_ Handling\ my_file_3.txt","x")   #Raise File Exist error
except FileExistsError:
    print("File Already exists")
print("End of programme")

