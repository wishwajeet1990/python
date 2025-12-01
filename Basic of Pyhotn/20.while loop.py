#This tutorial tells you about the loop in python

"""--------------Syntax for while loop--------------"""
# while condition:

print("Enter a variable to which your want to print the counting")
count = int(input())
i = 0
print(f"here is your counting form {count} to 1")
while i < count+1:
    if i == 5:
        i+=1
        continue
    for j in range(i):
        print("|",end="")
    print(i)
    i += 1
    