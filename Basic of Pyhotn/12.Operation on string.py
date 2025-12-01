"""Following operation can be performed on string

Concatenation - add two or more string together
Indexing - get the indexed value from the string
Slicing - cut down the string and get the value
Upper/lower - change the letter of the string
Find/Replace - find the substring or char in string
Split/Join - To join or split the string 
Strip - cut the string 
Length - calculate the length of the string

"""

#Lets Assume the string

F_Name = "wishwajeet"
M_Name = "singh"
L_Name = "tanwar"

Res_String = ""


#concatenation of the string 
Res_String = F_Name +" " + M_Name + " " + L_Name
print("My name is {} ".format(Res_String))

#indexing of the string
ind = Res_String[5] #Indesing start from 0 to n so when we give 4 as and index input then it will print the 5th char from the string
print(ind)

#Slicing of the string
# format of slicing name_of_string[int start:int end:int step_count val Step count may considered as 1 if missing or not given as explicitly

slc = Res_String[4:7]                          #Here it will print from start to end pt as explicitly stated
print("Res_String[4:7]  :-  {}".format(slc))   #Slicing the string
slc = Res_String[7:15]
print("Res_String[7:15]  :-  {}".format(slc)) #Slicing the string
slc = Res_String[10:50]                 
print("Res_String[10:50]  :-  {}".format(slc)) #Here the length of string is less than the explicitly written value 50 so the value store in slc will be last upto max of the len of string
slc = Res_String[23::-1]
print("Res_String[22:0:-1]  :-  {}".format(slc))    #Using step count 1 while slicing the string
slc = Res_String[0:23:2]                       
print("Res_String[0:23:2]  :-  {}".format(slc)) #Using step count 2 while slicing the string

#Upper/lower the string
print("Upper :-  %s"%Res_String.upper())       #Upper String format
print("lower :-  %s"%Res_String.lower())       #Lower String format
print("Capitalize :-  %s"%Res_String.capitalize())  #Capitalize the first letter of the String format
print("Title :-  %s"%Res_String.title())       #capital the first letter of the every word after the space String format

# Find/Replace
print(Res_String.find("singh"))   #Return the first occurence (integer value) whenever it trigger the character as specified in the find function else return -1 on failure
print(Res_String.find("sigh"))   #Return -1 bcz no such match will find in the res_string 
print(Res_String.find("w",7))   #Return the first occurence (integer value) whenever it trigger the character as specified in the find function starting from 7 position else return -1 on failure
print(Res_String.startswith("w"))   # Check the string wether startwith the given word or not and return as boolean value true
print(Res_String.endswith("w"))   # Return false
print("Z"in Res_String)   # Check the string wether in the exesiting string or not and return as boolean value

#Repeatation in string
rpt = 3
print(Res_String*rpt)   #While repeating the string we must have a positive integer value to repeat with 

#replacing
print(Res_String.replace("a","A"))    # Replace a with A in all occurence
print(Res_String.replace("a","A",1))    # Replace a with A with only 2 occuraence

#Stripping Whitespace

print(Res_String.strip())   #strip from both side
print(Res_String.lstrip()) #strip from left
print(Res_String.rstrip()) #strip from right

# Length
print("length of string = %d"%len(Res_String))      #Calculate the string of the string

#Advance string function 
s = "banana"
print(s.count("a"))   # 3
print(s.index("n"))   # 2

s = "Python123"
print(s.isalpha())   # False
print(s.isdigit())   # False
print(s.isalnum())   # True
print("   ".isspace())  # True


#Splitting and Joining the string
print(Res_String.split())

#slicing of string
New_S = "Python123 is very interesting language"
print(New_S)
print((New_S[10:17:1]).strip("y"))  #in this print statement the return value from the slicing of the New_S will be strip by the given character
print(New_S[::-1])  #this give you the complete reverse of the string inside New_S
#it will work like the New_S during slicing we give the start , end and step count , so if we do not give these parameter inside it 
#it automatically start with the step that is -1 from the starting from back side and decrement itself by -1 and reach to the 0th position of the string
