try:
    num1 = int(input("Enter Num  1 "))
    num2 = int(input("Enter Num  2 "))
    opr = int(input("Enter Operator "))
    match opr:
        case 1:
            print(f"The Sum of {num1} + {num2} is ",num1+num2)
        case 2:
            print(f"The Sum of {num1} - {num2} is ",num1-num2)
        case 3:
            print(f"The Sum of {num1} * {num2} is ",num1*num2)
        case 4:
            print(f"The Sum of {num1} / {num2} is ",num1/num2)
        case 5:
            print(f"The remainder of {num1} % {num2} is ",num1%num2)
        case _:
            print("Invalid Operator") 
except Exception as e:
    print("Operation unsuccessful",e)
    
    