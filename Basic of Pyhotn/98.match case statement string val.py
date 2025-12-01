try:
    num1 = int(input("Enter Num 1 "))
    num2 = int(input("Enter Num 2 "))
    opr = input("Enter Operator")
    match opr:
        case "+":
            print(f"The Sum of {num1} + {num2} is ",num1+num2)
        case "-":
            print(f"The Sum of {num1} - {num2} is ",num1-num2)
        case "*":
            print(f"The Sum of {num1} * {num2} is ",num1*num2)
        case "/":
            print(f"The Sum of {num1} / {num2} is ",num1/num2)
        case "%":
            print(f"The remainder of {num1} % {num2} is ",num1%num2)
        case _:
            print("Invalid Operator") 
except Exception as e:
    print("Operation unsuccessful",e)
    
    