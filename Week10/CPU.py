class CPU:
    def __init__(self, price, brand, clock_speed):
        self.price = price
        self.brand = brand
        self.clock_speed = clock_speed
    def compute(self):
        print("The CPU is processing.")