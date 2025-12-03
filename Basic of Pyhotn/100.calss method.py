class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print_details(self):
        print(f"Name of student :- {self.name}, Age of Mr. {self.name} is {self.age}")

class college():
    def __init__(self, student):
        self.student = student
    @classmethod
    def new_student_obj(cls,text):  #Here we will receive the text string of  "Wishwajeet_34"
        name ,age = text.split("_")    #we will split the string rceived from the function call by the object creation of the college class
        s1 = student(name,age)          # We create an object of class sttudent and pass the value to the newly created object of the class student
        return college(s1)              #here we will return the object of the class student bu passing it into the college class   

c1 = college.new_student_obj("Wishwajeet_34")      #here basically what is happening 
                                                    #when creted the object of the class college an calling to the new_student_object functio
                                                    #it will convert to c1  = college(s1)
                                                    # now when the above line executed the __init__ of t college calss get invocked 
                                                    # so now c is pass as first argument which will be captured as self s1 will be capturen in student varaible 
                                                    

c1.student.print_details()                      #No At this stage we are trying to access the print_details fucntion bu using the object of the c1 of college 
                                                #class to student class to print_details() function