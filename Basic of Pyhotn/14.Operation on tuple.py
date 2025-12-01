#Simply create a tuple

tpl = tuple()   #Empty tuple using tuple constructor
print("tpl",tpl)
tpl = ()        #Simply create tuple with standard format
print(tpl)
tpl = ("a", 1, True)        # Mixed data types
print("Mixed data types",tpl)
tpl = (5,)                  # Single-element tuple (note the comma)
print("Single-element tuple (note the comma)",tpl)
tpl = (1, 2, 3,4,5,6,7,8,9,10)             # Tuple of integers
print(tpl)
tpl1 = tuple(tpl)       #Simply copy the tpl to tpl1 variable
print(tpl1)

#Accessing the element of the tuple
print(tpl[0])      # print the value at 0th element 
print(tpl[-1])     # print the value at 1st location from the reverse of the tuple

#slicing the tuple 

print(tpl[1:])     # print element from the 1st pos till end 
print(tpl[:2])     # print element from 0th pos to till 2nd -1  element


#looping through tuple

for t_i in tpl:
    print(t_i)
    
# Checking Membership in tuple
print("1 in tpl",1 in tpl)  # True
print("2 not in tpl",2 not in tpl)  # False
print("20 not in tpl",20 not in tpl)  # True

#Tuple length
print("len(tpl)",len(tpl))  

#Tuple Unpacking
el1,el2,el3,el4,el5,el6,el7,el8,el9,el10 = tpl
print(el3,el10)

#Conversion: Tuple ↔ List
lst = list(tpl)       # Convert to list
lst[0] = 100
print(lst)
tpl = tuple(lst)      # Convert back to tuple
print(tpl)            # (100, 2, 3)

# tpl[1] = 20       #Doesn't support item assignment because the tpl are immutable in nature
# print(tpl)