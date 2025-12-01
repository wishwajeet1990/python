# Class Decorator Using a Class
#Yes we can make the class decorator for our class as well

class prefix:
    def __init__(self,prefix):
        self.prefix  = prefix
        
    def __call__(self, clsc):
        new_cls = clsc.__init__
        def update_init(cls_obj,name,*args,**kwargs):
            new_name  = self.prefix + name
            new_cls(cls_obj,new_name,*args,**kwargs)
            print("__call__ func called successfully") 
        clsc.__init__ = update_init
        return clsc
    
@prefix("Mr. ")     #Here we had done like this // p1 = prefix("Mr.") // create an object of the class prefix the we call  //      p1.__call__(p1)      //
class person:
    def __init__(self,name):
        self.name = name

p1 = person("Wishwajeet Singh")
print(p1.name)
