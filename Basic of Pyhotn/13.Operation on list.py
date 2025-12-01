#Creating list
lst = []                    # Empty List
print(lst)
lst = list([1,2,3,4,5])       #using constructor
print(lst)
lst = [1, 2, 3, 4, 5]       # List of integers
print(lst)
lst1 = list(lst)
print("chagne in list element ")

lst1[0] = 10
print(lst1)
lst1[1:] = [20,30,40,50,60,70,80,90]
print(lst1)

print("Accessing Elements (Indexing & Slicing)")
print(lst1[0])      # print 0th element of the list i.e 10
print(lst1[-1])     # print reverse element at nth position in case i.e 2  50
print(lst1[1:4])    # print list from start and end pos given as argument in this case i.e [20, 30, 40]
print(lst1[7:2:-1])   #print reverse of list using -1 step count

print("Adding Elements")
lst1.append(6)                # add single item 4 at the end of the end of the list[1, 2, 3, 4]
print(lst1)
lst1.insert(6, 7)            # add single item 10 at 1 position not the list would be [1, 10, 2, 3, 4]
print(lst1)
lst_1 = lst.extend([8,9,10])           # add multiple item at end of the list now the list would be [1, 10, 2, 3, 4, 5, 6]
print(lst)

print("Removing Elements: ")
lst1.remove(10)           # Removes first occurrence of 1
print(lst1)
lst.pop()               # Removes last item
print(lst)
lst.pop(1)              # Removes item at index
print(lst)
del lst[0]              # Removes element at index 0 
print(lst)
lst.clear()             # Empties the list → []
print(lst)

#Searching and Counting
print("Searching and Counting")
lst = [10, 20, 30, 20]
try:
    print(lst.index(120))   # 1 (first occurrence)
except Exception as e:
    print("Value Not Found",e)
print(lst.count(20))   # 2

#Sorting and Reversing 
lst = [3, 1, 4, 2]
lst.sort()             # [1, 2, 3, 4]
print(lst)
lst.sort(reverse=True) # [4, 3, 2, 1]
print(lst)
lst.reverse()          # Reverses current order
print(lst)

#Looping Through a List
fruits = ["apple", "banana", "cherry","potato"]
for fruit in fruits:
    print(fruit)

#comprehension of list 
sqr_frt = [z*4 for z in fruits]
print(sqr_frt)