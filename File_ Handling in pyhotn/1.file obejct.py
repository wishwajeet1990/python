"""A file handling is a process of manipulating or working with file that are stored on your computer
1. When you run a programme the data basically resides in you ram and will get lost when the execution wil be finished or the will be
    overridden by updated value when the statement will execute again 
"""
"""File handling allows us to 

1.create
2.read
3.write
4.update
5.close
6.delete 

files so that data is saved for later use."""

#   open("f_name with path" ,"Mode")    "To open the file "
#   file_obj.close()    "To close the opened file "

#Available Modes
"""------------------------------------------------------------------------ 
"r" → Read (default, file must exist)
"w" → Write (creates new file, overwrites existing)
"a" → Append (adds to end of file)
"x" → Create (new file, error if exists)
"b" → Binary mode (e.g., "rb", "wb")
"t" → Text mode (default, e.g., "rt", "wt") 
"r" → Read (default)
"r+" → Read + Write (update)
"w+" → Write + Read (overwrite)
"a+" → Append + Read
-----------------------------------------------------------------------------"""

# open a file

file = open("d:\\Python\\Codding\\File_ Handling\\ my_file_1.txt","w")        #it Will open a file if not exists it create or overwrite 
                                                                            # and open it for writing
if file:
    print("file create successfully")
    
try:
    file2 = open(r"d:\Python\Codding\File_ Handling\ my_file.txt","r")       #It will raise an error because the no file 
                                                                                #existed with name my_new_file.txt in current directory
                                                                                #so use exception handling
except FileNotFoundError:
    print("file not found")
finally:
    print("Please check the name of the file you entered for the reading. as no file exited such name ")

try:
    file3 = open(r"d:\Python\Codding\File_ Handling\ my_file_2.txt","a")      #It will not raise an error because the file will be created by mode "a"
                                                                                #and open the file in append mode
except FileNotFoundError:
    print("file not found")

print("End of programme")