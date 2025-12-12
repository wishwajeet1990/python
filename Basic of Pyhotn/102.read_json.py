import json

with open(r"E:\Training\Python\Codding\Basic of Pyhotn\sample2.json","r") as people_string :
    data = people_string.read()
    dt = json.loads(data)
for row in dt["people"]:
    if row["name"] == "Monu Singh":
        print(row["email"])
