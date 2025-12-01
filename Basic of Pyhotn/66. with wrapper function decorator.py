#This function will let allow you to under stand the concept of wrapper function or inner function usage 

def log_deco(fun_name):
    def inside_log_deco():
        print("Logging before function runs......")
        fun_name()
        print("Logging After Function runs ...... ")
    return inside_log_deco      #Here is we return the same object that receives at the parameter the the decorator will not run
    # return fun_name           #No decorator function will run because it is returning the self ref, object of the decorated function
@log_deco
def say_hello():            
    print("Hello using say hello function")
"""
                                say_hello = log_deco(say_hello)    
                                say_hello = inside_log_deco()
                                hence now the inside_log_deco will run
                                1.  print 'Logging before function runs......'
                                2.  call the fun_name variable which has stored the the address of the say_hello()
                                3.  run the say_hello()
                                4.  now print   'Logging After Function runs ...... '
                                and call over for the fist time
"""
say_hello()     #Now whenever we call the say hello function the log deco function will automatically run
say_hello()     #Now whenever we call the say hello function the log deco function will automatically run
say_hello()     #Now whenever we call the say hello function the log deco function will automatically run

"""-------------------------output---------------------------------------------
            Logging before function runs......
            Hello using say hello function
            Logging After Function runs ......
            Logging before function runs......
            Hello using say hello function
            Logging After Function runs ......
            Logging before function runs......
            Hello using say hello function
            Logging After Function runs ......
----------------------End----------------------------------------------------"""