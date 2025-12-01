def deco1(func):
    def wrapper1():
        print("Before func → from deco1")
        func()
        print("After func → from deco1")
    return wrapper1

def deco2(func):
    def wrapper2():
        print("Before func → from deco2")
        func()
        print("After func → from deco2")
    return wrapper2
    

@deco1
@deco2
def my_func():          #my_func = deco1(deco2(my_func))
                        #my_func = deco1(wrapper2)
                        #my_func  = 
                        # 1st line  = Before func → from deco1
                        # 2nd Line  = now it has ref to the wrapper2 fun and 
                        #instruction is func() which is equal to wrapper2
                        #now from wrapper2 print 
                        # Before func → from deco2
                        #Now as the wrapper2 function called hence 
                        #next statement will also from wrapper2 func() which has the address of main decorated function
                        #no actually call the main decorated function and call the main function.
                        # next instruction is from the deco2 which is print statement 
                        # now print "After func → from deco2"
                        # and finally the control return back to the dec1 function 
                        # print After func → from deco1
    print("This is my original function")

my_func()
print()
my_func()
"""---------------------output--------------------------------------
                    Before func → from deco1
                    Before func → from deco2
                    This is my original function
                    After func → from deco2
                    After func → from deco1
---------------------END-------------------------------------------"""