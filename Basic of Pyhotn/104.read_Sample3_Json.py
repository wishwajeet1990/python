import json

with open(r"E:\Training\Python\Codding\Basic of Pyhotn\sample3.json","r") as people_string :
    data = people_string.read()
    dt = json.loads(data)

for row in dt:
    print(row)
    for column in dt[row]:
        print(column)
        for data in column:
            print(column[data])