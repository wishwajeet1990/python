#This tutorial tells you about the loop in python

"""--------------Syntax for while loop--------------"""
# while condition:
import time as t
print("Enter a variable to which your want to print the counting")
count = int(input())
i = 0
print(f"here is your counting form 1 to {count}")
while i < count+1:
    if i == 5:
        i+=1
        continue
    for j in range(i):
        print("|",end="")
    print(i)
    i += 1

while count:
    for i in range(count):
        print("|",end="")
    print(count)
    count-=1