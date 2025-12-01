# a dict is a collection of ordered mutable and does not allow duplicate element in the key value 

#---------------------syntax--------------------------
# dict_name = {key_1:value1,key_2:value2...........key_n}
#or by using constructor 

#variable_name = dict(iterable item)

#create dict using standard format
#As the sets are using hashing tech to store the data/element hence it not possible to access the element byt their index.
#Also due to this while getting/reterving the sets we might get the different ordered manner while fetching


my_dict = {"Wishwajeet":99,"Rahul":54,"Monu":98,"Wishwajeet":99}
print(my_dict)  #Here when you run this code then you have will see the last updated key value pair will be printed not the earlier one wishwajeet key value pair
print("\n") 

#using dict constructor
my_dict = dict(Wishwajeet=95, Rahul=88, Monu=76)
print(my_dict)

#using tupple
my_tuple = (("wishwajeet",95),("monu",96),("Jhon",94),("Satya",98),("wishwajeet",988)) #Duplicate will automaticaly be removed while passing it to dict constructor
my_dict = dict(my_tuple)
print(my_dict)