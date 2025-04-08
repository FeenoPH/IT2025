class Vehicle:
    def __init__(self, year_manufactured, model, colour):
        self.year_manufactured = year_manufactured
        self.model = model
        self.colour = colour
    def start_engine(self):
        print("The engine is starting up")

class Car(Vehicle):
    def __init__(self, year_manufactured, model, colour):
        super().__init__(year_manufactured, model, colour)
    def start_engine(self):
        print(f"The {self.colour} {self.year_manufactured} {self.model} car is starting its engine")

class Motorcycle(Vehicle):
    def __init__(self, year_manufactured, model, colour):
        super().__init__(year_manufactured, model, colour)
    def start_engine(self):
        print(f"The {self.colour} {self.year_manufactured} {self.model} motorcycle is starting its engine")

car = Car(1972, "Volkswagen Beetle", "red")
motorcycle = Motorcycle(2010, "Royal Enfield Classic 350", "purple")

car.start_engine()
motorcycle.start_engine()
