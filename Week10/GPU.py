class GPU:
    def __init__(self, price, brand, model, clock_speed):
        self.price = price
        self.brand = brand
        self.model = model
        self.clock_speed = clock_speed
    def compute(self):
        print("The GPU is processing.")