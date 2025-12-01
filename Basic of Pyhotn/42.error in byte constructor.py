# """
# Option	                 Meaning
# strict	            :- Default. Throws error on bad character
# ignore	            :- Skips unsupported characters
# replace	            :- Replaces unsupported characters with ?
# backslashreplace	:- Replaces with Python-style escape: \uXXXX
# namereplace	        :- Uses Unicode name: 
# 
# """

s = "Café ☕"
# Using ASCII encoding (does not support 'é' or emoji)
b = bytes(s, encoding="ascii", errors="ignore") # it will simply ignore the character and print the rest
print(b)  # b'Caf '

# Using "replace" to insert ?
b = bytes(s, encoding="ascii", errors="replace")    # replace with ? 
print(b)  # b'Caf? ?'

