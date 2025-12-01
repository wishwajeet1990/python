class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property           #When we use property as decorator then the decorated function will behave more like pythonic 
                        #Means the decorated function can be called like a variable instead using parenthesis
    def balance(self):  # Getter
        return self.__balance

    @balance.setter                 #Control behavior of the balance method the class
    def balance(self, amount):      #syntax @func_name.decorator_object that of property object
                                    #While decorating with the property decorator object the function is decorated 
                                    #with the same same name as that of the function name .(dot)object property 
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance can't be negative.")

account = BankAccount(1000)
print(account.balance)   # ✅ Get balance
account.balance = 500    # ✅ Set balance
account.balance = -200   # ❌ Rejected

