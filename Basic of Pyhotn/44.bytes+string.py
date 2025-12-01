"""----------------encoding-------------------------------
this encoding is necessary if you dealing with string data type while working on byte constructor
----------------types of encoding---------------------------------------------------------------
ASCII
UTF-8
utf-16

latin-1
cp1252
------------------------end--------------------------------------------------------------------
"""

# """--------------------Error-------------------------------
# strict -  it will generate the error if encounter and is treated ad default behavour of the byte constructor is
# ignore- If the encounter the character is not as type of encoding then it will discard it
# replace -  it is used to replace the character with  ?
# backslashreplace - Replaces with Python-style escape: \uXXXX
# namereplace- Uses Unicode name: \\N{NAME}
# """
"""----------------------------------------Syntax------------------------------------
bytes(str,encoding= "",error="")
------------------------------end----------------------------------------------------
"""



b = bytes("Wishwajeeté",encoding="ASCII",errors="ignore")
print(b)         # b'Wishwajeet'

b = bytes("Wishwajeeté",encoding="ASCII",errors="replace")
print(b)         # b'Wishwajeet?'
b = bytes("Wishwajeeté",encoding="ASCII",errors="backslashreplace")
print(b)         #b'Wishwajeet\\xe9'

b = bytes("Wishwajeeté",encoding="ASCII",errors="namereplace")
print(b)         # b'Wishwajeet\\N{LATIN SMALL LETTER E WITH ACUTE}'
# b = bytes("Wishwajeeté",encoding="ASCII",errors="strict")
# print(b)         #UnicodeEncodeError: 'ascii' codec can't encode character '\xe9' in position 10: ordinal not in range(128)