#This programme will let you know how to sort the list of tuple using lambda function


my_list = [(2,5),(29,3),(11,22),(66,33),(1,4),(33,42),(5,44),(44,5),
           (11,67),(77,45),(99,87),(98,56),(76,90),(33,24),(56,56),
           (77,89),(22,44),(76,54),(88,78)]

new_list = sorted(my_list,key= lambda x :x[0],reverse=False)
print("Using Lambda Function \n",new_list)
