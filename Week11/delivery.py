class Delivery:
    def __init__(self, ID, name, information, date, address):
        self.ID = ID
        self.name = name
        self.information = information
        self.date = date
        self.address = address
    def processDelivery(self):
        print(f"Shipping your {self.name} to {self.address}.\n Order was processed on {self.date}.\n Your ID is {self.ID}.\n Furhter information on product: {self.information}")
