"""The bytes() constructor creates an immutable sequence of bytes (integers in the range 0–255).
It’s like a read-only array of bytes."""

"""------------------------------Syntax---------------------------------
                bytes([source[, encoding[, errors]]])
------------------------------------------------------------------------"""
#No arguments – returns an empty bytes object:
b = bytes()
print(b)         # b''

#Integer (size) – returns a bytes object of that length filled with null bytes (0x00):
b = bytes(4)
print(b)         # b'\x00\x00\x00\x00'

#Iterable of integers (0–255) – converts each to a byte:
b = bytes([65, 66, 67])
print(b)         # b'ABC'

#String + Encoding – encodes string into bytes:
b = bytes("Wishwajeet", encoding='utf=8')
print(b)         # b'Wishwajeet'