class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.__price = price
        self.__quantity = quantity

    def get_details(self):
        print(f"Name: {self.name}, Price: {self.__price}, Quantity: {self.__quantity}") 
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price

product_switch = Product("Nintendo Switch", 400, 89)
product_switch.get_details()
