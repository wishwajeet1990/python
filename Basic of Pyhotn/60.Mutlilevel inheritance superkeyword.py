#Use of super() key word
#In Python, the super() keyword is used to call methods or access properties from a parent (or superclass)
import time as t
class Father:
    family_title = "Tanwar"
    def __init__(self,name,age):
        self.fat_name = name
        self.fat_age = age
    def show(self):
        print(self.fat_name,self.family_title)
        print(self.fat_age," years old")
        

class Mother(Father):
    def __init__(self,m_name,f_name,f_age,m_age):
        self.mot_name = m_name
        self.mot_age = m_age
        super().__init__(f_name,f_age)
    def show(self):
        print(self.mot_name,self.family_title)
        print(self.mot_age," years old")
    def update_father_details(self,name,age):
        super().__init__(name,age)
        print("Father Details updated successfully")

class Child(Mother):
    def __init__(self,cname,cage,fname,fage,mname,mage):
        self.c_name= cname
        self.c_age = cage
        super().__init__(mname,fname,fage,mage)
    def show(self):
        print(self.c_name,self.family_title)
        print(self.c_age," years old")
    def update_FatherDetails(self,name,age):
        super().update_father_details(name,age)
    def show_complete_details(self):
        print("Father name :- ",self.fat_name,self.family_title)
        print("Father Age : -",self.fat_age)
        print("Mother name :- ",self.mot_name,self.family_title)
        print("Mother Age : -",self.mot_age)
        print("Child name :- ",self.c_name,self.family_title)
        print("Child Age : -",self.c_age)
        
        
c1 = Child("Wishwajeet Singh",34,"Ramesh Singh",59,"Chand Devi",58)
m1 = Mother("Chand Devi","Ramesh Singh",63,62)
m1.show()
m1.update_father_details("Ramesh Singh",65)     #Age of father changed wtr to m1 object not with respect to the child reffrence
c1.show_complete_details()
c1.show_complete_details()
t.sleep(5)
c1.update_FatherDetails("Ramesh Singh",60)
c1.show_complete_details()