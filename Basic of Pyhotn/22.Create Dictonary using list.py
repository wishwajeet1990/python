#Create dictionary using list of tuple
#list should have only one key value pair in it's pair of tuple

pair_list = [("name", "Wishwajeet"), ("age", 31), ("city", "Delhi_NCR")]
my_dict = dict(pair_list)
print("Using List of Tuple \n",my_dict)
print(my_dict.keys())
print(my_dict.values())

#Create dictionary using list of list
#list should have only one key value pair in it's pair of tuple

pair_list = [["name", "Wishwajeet"], ["age", 31], ["city", "Delhi_NCR"]]
my_dict = dict(pair_list)
print("Using List of List\n",my_dict)
print(my_dict.keys())
print(my_dict.values())

#Create dictionary using tuple of list
#Each Tuple should have only one key value pair in it's pair of tuple

pair_list = (["name", "Wishwajeet"], ["age", 31], ["city", "Delhi_NCR"])
my_dict = dict(pair_list)
print("Using tuple of list \n",pair_list)
print(my_dict.keys())
print(my_dict.values())

#Create dictionary using tuple of tuple
#Each Tuple should have only one key value pair in it's pair of tuple

pair_list = (("name", "Wishwajeet"), ("age", 31), ("city", "Delhi_NCR"))
my_dict = dict(pair_list)
print("Using Tuple of tuple \n",pair_list)
print(my_dict.keys())
print(my_dict.values())


#Create dictionary using set of tuple
#Each Set should have only one key value pair in it's pair of sets

pair_list = {("name", "Wishwajeet"), ("age", 31), ("city", "Delhi_NCR")}
my_dict = dict(pair_list)
print("Using set of tuple \n",pair_list)
print(my_dict.keys())
print(my_dict.values())

# Create dictionary using set of list
# Each Set should have only one key value pair in it's pair of sets

# pair_list = {["name", "Wishwajeet"], ["age", 31], ["city", "Delhi_NCR"]}
# my_dict = dict(pair_list)
# print("Using set of list \n",pair_list)

# Create dictionary using list of sets
# Each Set should have only one key value pair in it's pair of sets
# Sequence of key value pair may change sometime the value becomes key and key becomes value an vice - versa

# pair_list = [{"name", "Wishwajeet"}, {"age", 31}, {"city", "Delhi_NCR"}]
# my_dict = dict(pair_list)
# print("Using list of sets \n",pair_list)
# print(my_dict.keys())
# print(my_dict.values())

# Create dictionary using set of sets
# Each Set should have only one key value pair in it's pair of sets
# Sets are unhashable so we can't create dictionary in this format

# pair_list = {{"name", "Wishwajeet"}, {"age", 31}, {"city", "Delhi_NCR"}}
# my_dict = dict(pair_list)
# print("Using set of sets \n",pair_list)