"""-------------------------- Syntax-----------------------------------
            memoryview_object = memoryview(obj)
            
------------------------------------------------------------------------"""
data = bytearray("Wishwajeet", "utf-8")
mv = memoryview(data)

print(mv[0])         # Output: 87 (ASCII of 'W')
mv[0] = 65           # Changing 'W' to 'A'
print(data)          # bytearray(b'Aishwajeet')
data[4] = 99
print(data)          # bytearray(b'Aishcajeet')


mystr = b"Wishwajeet"
print(mystr)

print(mystr[3]) # It will print the 4th letter of the string
n_mv = memoryview(mystr)
# n_mv[4]= 127 # it will raise an error while run with comment this line because this will not work directly without bytearray
print(mystr)


"""--------------------------------------------------------------------
Notes:- 
    We can't use memoryview with str directly. 
    Use bytes or bytearray.
-------------------------------------------------------------------"""