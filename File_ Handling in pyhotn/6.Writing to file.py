import time as t

mf = open(r"E:\\Training\\Python\\Codding\\File_ Handling in pyhotn\\my_file_6.txt","w")       #Always Open or create in fresh start point for writing the file .
# mf = open(r"E:\\Training\\Python\\Codding\\File_ Handling in pyhotn\\my_file_6.txt","a")       #Always Open or create in fresh End of file point for writing the file .
mf.write("Hello this is my New file created using python .\nIt has one line but more character than next line which will be executed after next open statement\n")
mf.close()
t.sleep(1)
mf = open(r"E:\\Training\\Python\\Codding\\File_ Handling in pyhotn\\my_file_6.txt","r")       #Always Open or create in fresh start point for writing the file .
print(mf.read())
mf.close()
mf = open(r"E:\\Training\\Python\\Codding\\File_ Handling in pyhotn\\my_file_6.txt","w")       #Always Open or create in fresh start point for writing the file .
mf.write("SOL My File has been created EOL .")      #Whenever we open a file using "w" mode it always open it to write from start overwrite it
                                                                #Hence whenever we try to read this file we always find only 
                                                                #the line that has been added
                                                                
mf.close()
mf = open(r"E:\\Training\\Python\\Codding\\File_ Handling in pyhotn\\my_file_6.txt","a")       #Always Open or create in fresh End of file point for writing the file .
mf.write("Hello this is my New file created using python append mode .\n")      #Whenever we open a file using "a" mode it always open it to write from End of file
                                                                #Hence whenever we try to write it will write from EOF and hence when 
                                                                # we read this file we always find the appended line as well                                                              
                                                                 # the line that has been added