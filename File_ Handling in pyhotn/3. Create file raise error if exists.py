import os
import time
file = open(r"E:\\Training\\Python\\Codding\\File_ Handling in pyhotn\\my_file_2.txt","w")         #Create new File without error
time.sleep(1)
file.close()
time.sleep(1)
try:
    file = open(r"E:\\Training\\Python\\Codding\\File_ Handling in pyhotn\\my_file_3.txt","x")   #Raise File Exist error
except FileExistsError:
    print("File Already exists")
print("End of programme")