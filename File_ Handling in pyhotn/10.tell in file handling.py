# tell() will let you know about the current position of the cursor in file 

file = open(r"D:\Python\Codding\File_ Handling\ my_file_5.txt","r")
print(file.readline())
print(file.tell())  #it will return the current position of the cursor here in case return 50 
                    #means the cursor is at 50 position character in file .
                    