import json

running = True

with open(r"E:\Training\Python\Codding\Pandas Library\AgeBarrierContent.json","r") as AgeBarrierContent:
    my_file = AgeBarrierContent.read()
    dt = json.loads(my_file)

while(running):
    Check = input("Enter a countary ")
    for data in dt:
        for new in dt[data]:
            if new == Check.upper():
                print("Yes Available")
                print(dt[data][new])
            if (Check.upper() == "EXIT"):
                running = False