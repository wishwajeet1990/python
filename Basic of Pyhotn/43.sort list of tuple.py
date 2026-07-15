#This programme will let you know how to sort the list of tuple using lambda function
import time as t
my_list = [(2,5),(29,3),(11,22),(66,33),(1,4),(33,42),(5,44),(44,5),
           (11,67),(77,45),(99,87),(98,56),(76,90),(33,24),(56,56),
           (77,89),(22,44),(76,54),(88,2)]

print("My list \n ", my_list )
new_list = sorted( my_list , reverse = False )
print("Without Using Lambda Function \n " , new_list )
new_list = sorted( my_list , reverse = False , key = lambda x:x[0])
print("Using Lambda Function \n " , new_list )