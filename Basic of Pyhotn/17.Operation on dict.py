#multi nested dictionary
import time as t

student = {100:{"name":"Wishwajeet","Class":"B.tech","Stream":"IT"},
           101:{"name":"Neeraj","Class":"B.tech","Stream":"ECE"},
           102:{"name":"Anjani","Class":"B.tech","Stream":"CSE"},
           103:{"name":"Zeeshan","Class":"B.tech","Stream":"EEE"},
           104:{"name":"Satyajeet","Class":"B.tech","Stream":"Mech"},
           105:{"name":"Shailender","Class":"B.tech","Stream":"AI"},
           106:{"name":"Kulpreet","Class":"B.tech","Stream":"Civil"},
           }

print(student)
student[107] = {"name":"Arif","Class":"B.tech","Stream":"N/A"}

print("\n")
print(student)

print("\n")

if 107 in student:
    print("Student Exists\n")
names = list([])
print("\n")

#extracting the key value pair from the nested dictionary

names = [Details["name"] for Details in student.values()] #Retrieve name only
print(names)
print()
#here you will find the extended version of the above statement
all_name = list()
for key in student.values():
    all_name.append(key["Stream"])
print(all_name)

