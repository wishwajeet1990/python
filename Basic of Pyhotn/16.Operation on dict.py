"""A Dictionary is key value pair data type in python 
A dictionary must have the unique and immutable key value 
a dictionary is mutable in nature
it unordered in <3.7 version of python but ordered in >3.7 version of the python"""

#Normal Dictionary
my_dict = {"Name":"Wishwajeet Singh","Age":32,"Roll No":1}
print(my_dict)
print(my_dict.keys())
my_dict["email"] = "wishwajeetrana1990@gmail.com"
my_dict["Mobile No"] = "9991100891"
print(my_dict)
print(my_dict.keys())

#nested Dictionary becomes an array of dictionary hence it should have to accessed by their index no
person_dtls = [{"name": "Wishwajeet", "age": 31, "city": "Delhi"},{"name": "Rahul", "age": 30, "city": "Mumbai"},{"name": "Amit", "age": 31, "city": "Kolkatta"}]
# s_set = set(person_dtls)        #Not valid because the this dictionary is nested hence not valid
# print(s_set)
print("Accessing Elements")
print(person_dtls[0:3:2])        # Return 1 element of the dictionary

print("Adding / Updating Elements")
person_dtls[0]["email"] = "wishwajeetrana1990@gmail.com"
person_dtls[0]["Mobile_No"] = "9991100891"
print(person_dtls)


print(person_dtls[0].keys())

if "email" in person_dtls[0]:
    print("Email exists")

print("Access the value of the dictionary")
print(person_dtls[0].values())

print("Access the items of the dictionary")

for item in person_dtls:
    print(item)
    for pair in item.items():# Accessing the single pair  by pair from the nested dictionary 
        print(pair)

#Merge two dictionaries


print(person_dtls)

# #deleting a dictionary

# print(person_dtls)
# del person_dtls[0]          #Delete a complete dictionary at 0th position
# print(person_dtls)

# print(person_dtls[0].pop("name"))       #Remove the dictionary value from the dictionary 0 where the key is name
# print(person_dtls)

# #clear the Dictionary 

# person_dtls.clear()
# print(person_dtls)