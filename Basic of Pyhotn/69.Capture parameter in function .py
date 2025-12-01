#   *args/*parm used to store the tuple value 
#   **kargs/**parm used to store the dict value 

def callee_function(*parm,**k_parm):
    print(f"Parm = {parm}")
    print(f"k_parm = {k_parm}")
    
    
dic = {
        "name": {"wishwajeet singh","Satyajeet singh","Parmjeet Singh"},
        "age": {34,33,30},
        "Education":{"B.tech","B.tech","B.A"}
       }
print("1,2,3,4,5,6,7,8,9:- ")
callee_function(1,2,3,4,5,6,7,8,9)                                  #value will captured in *parm
print("Dict:- ")
callee_function(dic)                                                #print as normal tuple  not as dictionary
print("name = Wishwajeet,Comp = RT Vision, salary  = 250000:- ")
callee_function(name = "Wishwajeet",Comp = "RT Vision", salary  = 250000)    #value will captured in **k_parm
print("1,2,3,4,5,6,7,8,9,Name = Wishwajeet,age = 34 :- ")
callee_function(1,2,3,4,5,6,7,8,9,Name = "Wishwajeet",age = 34)     #value will captured in **k_parm and *parm

