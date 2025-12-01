# Using multipledispatch Library (True Multiple Dispatch)


from multipledispatch import dispatch

@dispatch(int,int)
def add(a,b):
    return a+b
@dispatch(str,str)
def add(a,b):
    return a+b
    
# @dispatch(float,float)
# def add(a,b):
#     return a+b
@dispatch()
def add(a,b):
    return a+b

try:
    print(add(3.5,4.8))
except Exception as e :
    print(e)
finally:
    print("No More Exceution pending")
print("EOP")