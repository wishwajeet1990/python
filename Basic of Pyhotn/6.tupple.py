# Definition :- A tupple is a ordered imutable and allow duplicate element "

# ---------------Syntax------------------------------
# tupple_name = (item_1,item_2,item_3..............item_n)
# using tupple constructor
# list name = tuple(iterable item)

# A tupple could have any type of variable
name  = "Wishwajeet Singh Tanwar"
mylist = [1,2.4,3+4j,"hello"]

print("Using manual entry \n")
my_tupple = (1,2.3,'Wishwajeet',3+4j)   #manual entry of the tuple 
print(my_tupple)
print("\n")

print("Using string literal tupple constructor\n")
my_tupple = tuple("Wishwajeet")   #Passing String literal to the tuple constructor
print(my_tupple)
print("\n")

 #or

print("Using string literal tupple constructor\n")
my_tupple = tuple(name)   #Passing String literal to the tuple constructor
print(my_tupple)
print("\n")

print("Using range function to tupple constructor\n")
my_tupple = tuple(range(10,100,2))   #Passing range function to the tuple constructor
print(my_tupple)
print("\n")


print("Using passing list to tupple constructor\n")
my_tupple = tuple(mylist)   #Passing list to the tuple constructor
print(my_tupple)
print("\n")

print("Passing set to tuple constructor\n")
my_tupple = tuple({5, 6, 7})       #Passing a set to tuple constructor
print(my_tupple)
print("\n")

print("create one element tuple using tuple constructor\n")
my_tupple = tuple([5])       #Passing a single element to tuple constructor
print(my_tupple)
print("\n")