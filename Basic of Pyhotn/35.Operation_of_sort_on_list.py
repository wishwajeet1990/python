my_tuple = tuple((33,22,55,66,77,88,22,33,4,5,77,88,66))
my_list = list(my_tuple)
my_list.sort(reverse=False)
print(my_list)
new_unique_list  = list(set(my_list))
new_unique_list.sort()
print(new_unique_list)

