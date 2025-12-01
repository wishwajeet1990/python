# "A range is datatype in python that takes integer as an argument and generate a sequence"

# ------------------syntax-------------------
# range(int1,int2,int3)
# int1 - Start From
# int2 - End at
# int3 - Step count"""

my_range = range(10,100,2)  #define the range

print(list(my_range))   # simply use to print the simply list of the range

# or using the iterative tech to print the range

for i in my_range:      #for loop and in keyword together
    print(i)
    
    