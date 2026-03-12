from Oops_concept.multilevel_inheritence.Bike import Bike


class MotorBike(Bike):
    def __init__(self, color,brand,model,year):
        super().__init__(brand,model,year)
        self.color = color

    def display(self):
        super().display()
        print(self.color)

Motor1 = MotorBike("red","HONDA","XX6",2022)
Motor1.display()
