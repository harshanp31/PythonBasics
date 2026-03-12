class Person:
    def __init__(self,name,age,password):
        self.name = name #public attribute: so it can be accessed anywhere in the package
        self._age = age #protected attribute
        self.__password = password #private attributes

    def set_password(self,password): #to access private set & get method
        self.__password = password

    def get_password(self):
        return self.__password

P1 = Person("Harsha","31","Vedh")
P1.name = "Ashwin"
print(P1.name)
P1.set_password("Harsha@123")
print(P1.get_password())
print(P1._age)

