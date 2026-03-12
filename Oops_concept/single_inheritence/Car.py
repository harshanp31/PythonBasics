from Oops_concept.single_inheritence.Vehicle import Vehicle
class Car(Vehicle):
    def __init__(self,color,mileage,model,year):
        super().__init__(model,year) #super() keyword is used to acquire something from the parent class
        self.color = color
        self.mileage = mileage

    def display(self):
        super().display() #method overriding here parent & child class has same function display()
        print(self.color)
        print(self.mileage)

car1 = Car("red",2000,"Mercede",2000)
car1.display()
car2 = Car("blue",2000,"BMW",2025)
car2.display()