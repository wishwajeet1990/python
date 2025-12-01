# a set is a collection of unordered mutable and does not allow duplicate element 

#---------------------syntax--------------------------
# set_name = {el_1,el_2,el_3,el_4...........el_n}
#or by using constructor 
#variable_name = set(iterable item)

#create set using standard format

#As the sets are using hashing tech to store the data/element hence it not possible to access the element byt their index.
#Also due to this while getting the sets we might get the different ordered manner while fetching

print("Using standard syntax set")
my_set = {1,2.5,"wishwajeet",3+4j}
print(my_set)
print("\n")


#create empty sets
print("Empty set")
my_set = set()
print(my_set)
print("\n")

print("set using list")
my_set = set([1, 2, 3, 2, 1,20,34,54,267,352,22,11,85,45,33,55,22,66,77,44,24,10,1,2,3])       #Doesn't allow duplicate values in it also might get the unordered set as they stored
print(my_set)
print("\n")

print("set using tuple")
my_tuple = (1,2.3,3+4j,"wishwajeet")
my_set = set(my_tuple)       #Using tuple but in unordered manner
print(my_set)
print("\n")

print("set using Dict")
my_dict = {"Wishwajeet":99,"Rahul":54,"Monu":98,"Wishwajeet":99}
my_set = set(my_dict)       #Using tuple but in unordered manner and duplicate will be removed automatically
print(my_set)
print("\n")

