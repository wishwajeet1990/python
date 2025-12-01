class sub:
    def __init__(self,val,name):
        self.val = val
        self.name = name
    def __sub__(obj1,obj2):
        val = obj1.val + obj2.val
        return val
    def __str__(obj):
        return f"You have entered {obj.name}"

cls1 = sub(6,"monu")
cls2 = sub(7,"joni")
cls3 = cls2-cls1
print(cls3)
print(cls1)
print(cls2)