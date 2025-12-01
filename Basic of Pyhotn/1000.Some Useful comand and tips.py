# dir() → Shows all attributes and methods (including special methods)

import os       #Access the system level command

# Clear command for Windows ('cls') and Unix/Linux/Mac ('clear')
os.system("clear")      #This method is used to run the system command using system method.
# os.system("dir")        #This method is used to run the system command using system method.

# print("Str")
# print(dir(str))      # For str class
print("OS related")
print(dir(os))
details =  os.times()
print(details.system )
print("\n")
print("list")
print(dir(list))     # For list class
print("\n")
print("Dict")
print(dir(dict))     # For dict class

""" help() → Gives detailed documentation (press q to quit help viewer)"""

help(str)        # Shows doc string and methods of the str class
help(dict)      # Shows doc string and methods of the str class
for item in dir(str):
    
    if not item.startswith('__'):
        print(item)
