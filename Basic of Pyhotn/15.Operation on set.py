"""A set in Python is:

Unordered - didn't maintain any order during fetching the set
Unindexed - As set didn't maintained the order in nature hence they are not able to access using their index
Mutable - Their element/item are mutable and hence they can be changed 

"""
#Creating a Set

print("Using set std format")
s_set = {1, 2, 3,4,5}
print(s_set)  
print("Using set constructor")
s_set1 = set([6,7,8,9,10])  # Using set constructor
print(s_set1) 

print("Adding item to the set")

s_set1.add(20)  #insert one item at a time
print(s_set1) 
s_set1.update([300,400,500]) #Enter more than one item at a time
print(s_set1)

print("set operation")

print("union - adding two set together")

print(s_set | s_set1)
print(s_set.union(s_set1))

print("Difference in two set ")

print(s_set - s_set1)
print(s_set.difference(s_set1))
print(s_set1 - s_set)
print(s_set1.difference(s_set))

print("Intersection - same in two set ")
print(s_set & s_set1)
print(s_set.intersection(s_set1))
print(s_set1 & s_set)
print(s_set1.intersection(s_set))

print("Symmetric Difference (non-common elements)")
print(s_set ^ s_set1)
print(s_set.symmetric_difference(s_set1))
print(s_set1 ^ s_set)
print(s_set1.symmetric_difference(s_set))


#Removing Elements
# s_set1.remove(10)   # Removes 100; Error if not found
# print(s_set1)
# s_set1.discard(100)  # Removes if exists; No error if not
# print(s_set1)
# s_set1.pop()       # Removes and returns a random element
# print(s_set1)
# s_set1.clear()     # Removes all elements
# print(s_set1)