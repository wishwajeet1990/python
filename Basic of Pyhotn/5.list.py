# Definition :- A list is a ordered mutable and allow duplicate element 

# ---------------Syntax------------------------------
# list_name = [item_1,item_2,item_3..............item_n]
# using list constructor
# list name = list(iterable item)

# A list could have any type of variable

print("Manual Entry\n")
my_list = [1,2.3,'Wishwajeet',3+4j]     #Simply Create a list manually
print(my_list)
print("\n")

print("Using range function:- ")
my_list = list(range(10, 100, 2))   #Using range function as iterable variable
print(my_list)
print("\n")

print("Passing a string literal\n")
my_list = list("hello") #Passing a string to list constructor
print(my_list)
print("\n")

print("Passing a tupple\n")
my_list = list((1, 2, 3, 4))    #Passing a tupple to list constructor
print(my_list)
print("\n")

print("From dictionary\n")
my_dict = {'a': 1, 'b': 2}
my_list = list(my_dict) #Passing a dictionary to list constructor
print(my_list)
print("\n")

print("Empty List\n")
my_list = list()        #Empty list
print(my_list)

print("\n")
print("Passing set to List constructor\n")
my_list = list({5, 6, 7})       #Passing a set to list constructor
print(my_list)
print("\n")

