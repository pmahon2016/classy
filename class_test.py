class Cars:
    """Simple Class with Template for Cars"""

    dealer = 'Best Cars'

    def __init__(self, type, color):
        self.type = type
        self.color = color

    def describe_car(self):
        print("My car is a " + self.color + " " + self.type)
        print("This car was purchased at " + Cars.dealer)


class Electric_cars(Cars):
    def __init__(self, type, color, capacity):
        super().__init__(type, color)

        self.capacity = capacity

    def describe_car(self):
        print("My car is a " + self.color + " " + self.type
              + " that has a range of " + self.capacity)
        print("This car was purchased at " + Cars.dealer)


# instances of Car class
car1 = Cars('sedan', 'blue')
car2 = Cars('SUV', 'green')
ecar = Electric_cars('Sedan', 'Green', '160miles')

# call method within Car Class
car1.describe_car()

car2.describe_car()

ecar.describe_car()

Electric_cars.describe_car(ecar)