# truncate will resize the file after the passed parament position

file = open(r"E:\\Training\\Python\\Codding\\File_ Handling in pyhotn\\my_file_6.txt","a+")
content = file.read()
print(content)
file.seek(33)
file.truncate()
print("Current cursor position :- ",file.tell())  #it will return the current position of the cursor here in case return 50 
                    #means the cursor is at 50 position character in file .
file.seek(0)
print(file.read())