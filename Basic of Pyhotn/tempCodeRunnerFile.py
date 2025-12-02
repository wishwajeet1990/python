file_path = r"E:\Training\Python\Codding\Basic of Pyhotn\sample.txt"
line_number = 3   # 1-based index

f = open(f"{file_path}", "w")
for i in range(5):
    f.write(f"This is my simple text file that contain my simple text {i+1}\n")
    f.flush()
f.close()

f = open(f"{file_path}", "r")
for i in range(5):
    line = f.readline()
    print(line)
f.close()

f = open(f"{file_path}", "a+")
lines =  f.readlines()
for i, line in enumerate(lines, start=1):
    if i != line_number:
        f.write(line)
f.close()

print()
print()
f = open(f"{file_path}", "r")
print(f.read())