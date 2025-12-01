#Single level if else       
marks = int(input("Enter your  marks"))
grade = "A" if marks>80 else "D" 
print("Your Grade is %s"%grade)

#Multilevel If Else statement
marks = int(input("Enter your  marks"))
grade = "A" if marks>=80 else "B" if marks>=70 else "C" if marks>=60 else "D"
print("Your Grade is %s"%grade)

#Clever If Else Statement
marks = int(input("Enter your  marks"))
grade = ["B","A"] [marks>=90]
print("Your Grade is %s"%grade)