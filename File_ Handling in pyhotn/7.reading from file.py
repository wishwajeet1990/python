import time 

file = open(r"E:\\Training\\Python\\Codding\\File_ Handling in pyhotn\\my_file_6.txt","r")         #Open the file in read mode only we can't write to it
my_line = file.read()
print(my_line) #Can be read as to store into object or by directly by print statement
print(file.read())
for line in file:
    print(line.strip())
    time.sleep(1)

try:
    file.write("We are trying to write into the file which has been opened in read only mode")
except Exception as e:
    print("File opened in read mode only you can't write into it.",e)
    
print("End of programme")

print(file.readable())