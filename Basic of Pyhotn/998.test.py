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
    def new_student_obj(cls,text):
        name ,age = text.split("_")
        s1 = student(name,age)
        return cls(s1)

c1 = college.new_student_obj("Wishwajeet_34")

c1.student.print_details()