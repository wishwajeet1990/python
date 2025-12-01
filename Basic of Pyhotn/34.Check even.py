import time as t
prime = []
start = True
end  = False

start_num = int(input("Start Number :- "))
end_num = int(input("End Number :- "))

even = [yes for yes in range(end_num) if yes%2 ==0]
print(even)
odd = [yes for yes in range(end_num) if yes%2 !=0]
print(odd)

value = start_num
while start:
    if value >= 2 and end_num > start_num:
        for i in range(2,value):
            if value%i == 0:
                break
            else:
                if value not in prime:
                    prime.append(value)
    if value >= end_num:
        start=end
    value +=1
print("Prime :- ",prime)
