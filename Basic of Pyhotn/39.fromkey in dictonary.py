"""-------------------syntax----------------------------
        dict.fromkeys(iterable, value)
---------------------------------------------------------"""


keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys,[10])
print(new_dict)
new_dict["b"].append(5)         # Add 5 at the end of the list of the dictionary at every value 
new_dict["b"].append(20)        # Add 20 at the end of the list of the dictionary at every value 
new_dict["b"].append(20)        # Add 20 at the end of the list of the dictionary at every value 
print(new_dict)
new_dict["b"].remove(5)         # Remove 5 from the list of the dictionary 
new_dict["b"].remove(20)        # Remove 20 from the list of the dictionary from first occurence  
print(new_dict)

