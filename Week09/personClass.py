class Person:

    def __init__(self, name, money, hair_length):
        self.name = name
        self.money = money
        self.hair_length = hair_length

    def eat(self):
        print(f"{self.name} eats a bowl of soup. Their {self.hair_length} inch hair gets in the way")
    def spend(self):
        if self.money >= 2:
            print(f"{self.name} has {self.money} dollars to spend. They spend 2 dollars of it")
            self.money -= 2
        else:
            print(f"{self.name} cannot afford to spend any money!")

Luka = Person("Luka", 5, 23)
Luka.eat()

Phoenix = Person("Phoenix", 6, 12)
for i in range(0, 4):
    Phoenix.spend()



