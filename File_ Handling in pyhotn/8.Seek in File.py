#Seek is function to set the cursor of the file 
"""
============================Syntax of Seek==================================
                    seek(offset, whence=0)  
                    offset  = how many bytes/chars to move
                    whence  = reference point
                        0 = from beginning of file (SEEK_SET)
                        1 = from current position (SEEK_CUR)
                        2 = from end of file (SEEK_END)
===================================EOF Seek==================================
"""



file  = open(r"E:\\Training\\Python\\Codding\\File_ Handling in pyhotn\\my_file_6.txt","r")
print(file.readline()) 
"""No when we read this file my cursor has been reached at EOL and when we again 
                        try to read this file it starts read from next to cursor position """
print(file.readline()) 
print(file.readline()) 
print(file.readline())  #As we already at EOF it will not print anything
file.seek(0)    #Set cursor to Start of file
print(file.readline())  #As we are at SOF it will print from starting
file.seek(12,0)     #Start at 10 character 
print(file.readline())  #As we are at SOF it will print from starting till \n finds
print(file.read())  #As we are at second line it will print from third line till EOF