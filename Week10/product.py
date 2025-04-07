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
        else:
            print(f"The {self.name}'s new price must be positive")
    def set_quantity(self, new_quantity):
        if new_quantity > 0 and new_quantity % 1 == 0:
            self.__quantity = new_quantity
        else:
            print(f"The {self.name}'s new quantity must be a positive whole number")
    def get_price(self):
        return self.__price
    def get_quantity(self):
        return self.__quantity

product_switch = Product("Nintendo Switch", 400, 89)
product_switch.get_details()

product_switch.set_price(300)
product_switch.set_quantity(49)

print(f"Price: {product_switch.get_price()}")
print(f"Quantity: {product_switch.get_quantity()}")
