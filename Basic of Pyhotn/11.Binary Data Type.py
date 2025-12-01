#This chapter tell you about the binary data type

#these data type are used to store the binary data

"""----------------syntax---------------------------
bytes([int_1,int_2,int_3............int_n])
bytearray([int_0_1,int_0_2,int_0_3............int_0_n],[int_1_1,int_1_2,int_1_3............int_1_n])"""

#let us deep drive into the byte data type using some example

print("Fetcting the byte data types")

print("Using Tuple")
byt = bytes((65,66,67)) #using tuple
print(byt)
print("\n")
print("Using sets")
byt = bytes({68,69,70}) #using sets
print(byt)
print("\n")
print("Using List")
byt = bytes([71,72,73]) #using list
print(byt)
print("\n")

print("Print String using byte data type")
byt = bytes([72,69,76,76,79]) #using byte Data type "HELLO"
print(byt)
print("\n")


#This will not work 
# print("Using dict")
# my_dict = {"Wishwajeet":99,"Jhon":98,"Monu":95}
# b_a = bytes(my_dict) #using list
# print(b_a)
# print("\n")

#print the bytearray 

print("Fetcting the bytearray data types")

print("Bytearray Using Tuple")
byt_arr = bytearray((65,66,67)) #Bytearray using tuple
print(byt_arr)
print("\n")
print("Bytearray Using sets")
byt_arr = bytearray({67,68,69}) #Bytearray using sets
print(byt_arr)
print("\n")
print("Bytearray Using List")
byt_arr = bytearray([70,71,72]) #Bytearray using list
print(byt_arr)
print("\n")

print("Print String using Bytearray  data type")
byt_arr = bytearray([72,69,76,76,79]) #Bytearray using byte Data type "HELLO"
print(byt_arr)
print("\n")

#This will not work 
# print("Using dict")
# my_dict = {"Wishwajeet":99,"Jhon":98,"Monu":95}
# b_a = bytes(my_dict) #using list
# print(b_a)
# print("\n")