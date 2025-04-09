class HardDisk:
    def __init__(self, price, brand, HDType, size):
        self.price = price
        self.brand = brand
        self.HDType = HDType
        self.size = size
    def load_os(self):
        print("The OS is loading.")