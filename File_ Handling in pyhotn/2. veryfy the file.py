#To check wether the file is exists or not we have to check with the path as belows


import os as o

if o.path.exists(r"E:\\Training\\Python\\Codding\\File_ Handling in pyhotn\\my_file_1.txt"): #We use r → to prevent Python from confusing \n, \t, etc.
    print("File Exists")
else:
    print("File not exists")