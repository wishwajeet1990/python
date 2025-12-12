from csv import DictReader

# my_dict = {"name" : ["wishwajeet","satyajeet","hasim","gaurav","sharvan"],
# "Dept":["ETB","FAS","FAS","ETB","WPMS"]}

# print(my_dict["Dept"])
file_handler = open(r"E:\Training\Python\Codding\Basic of Pyhotn\sample1.csv","r",encoding = "utf8")
csv_reader = DictReader(file_handler)
table : List[Dict[str,float]] = []
for row in csv_reader:
    float_row: Dict[str,float] = {}
    for cloumn in row:
       float_row[cloumn] = float(row[cloumn])
    table.append(float_row)

print(table)

high_temp_sum :float = 0.0
for row in table:
    high_temp_sum += row["High"]
print("High Temp Average is ",high_temp_sum/len(table))
file_handler.close()