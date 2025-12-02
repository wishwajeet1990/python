# tell() will let you know about the current position of the cursor in file 

file = open(r"E:\\Training\\Python\\Codding\\File_ Handling in pyhotn\\my_file_6.txt","r")
print(file.readline())
print(file.tell())  #it will return the current position of the cursor here in case return 50 
                    #means the cursor is at 50 position character in file .
print(file.read())
print(file.tell())  #it will return the current position of the cursor here in case return 50 
                    #means the cursor is at 50 position character in file .
                    