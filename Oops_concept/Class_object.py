from Oops_concept.data_encapsulation import Person


class Student:
    school_name = "ABC" #class/ global variable
    def __init__(self,name,age):
        print("this is a constructor")
        self.name = name  #instance/local variable
        self.age = age   #instance/local variable

    def display(self):
        print("NAME :", self.name)
        print("AGE :", self.age)
        print("sCHOOL NAME :", Student.school_name)


#Object Creation
#Constructior is automatically created when an object is created
student1 = Student("Harsha",25)
student1.display()

student2 = Student("Ashwin",31)
student2.display()

