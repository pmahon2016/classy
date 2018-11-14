class Pizza:
    def __init__(self, type,toppings):
        self.type = type
        self.toppings = toppings

    def pie(self, lowcost):
        print("I love my " + self.type + " pizza with " + self.toppings)
        print("it is also very " + lowcost)

mypizza = Pizza("medium", "sausage")



mypizza.pie("expensive")



