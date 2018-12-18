class Cars:
    """Simple Class with Template for Cars"""

    dealer = "Bestcars"

    def __init__(self, type, color):
        self.type = type
        self.color = color

    def describe_car(self):
        print("My car is a " + self.color + " " + self.type)
        print("this is from " + Cars.dealer)

class Electric_cars(Cars):

    def __init__(self, type, color, capacity):
        super().__init__(type, color)

        self.capacity = capacity

    def describe_car(self):
        print("My car is a " + self.color + " " + self.type
              + " that has a range of " + self.capacity)
        print("this is from " + self.dealer)

# instances of Car class
car1 = Cars('sedan', 'blue')
car2 = Cars('SUV', 'green')

ecars = Electric_cars('sedan', 'green', '180miles')


# call method within Car Class
car1.describe_car()

car2.describe_car()

ecars.describe_car()