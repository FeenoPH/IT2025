class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def getInfo(self):
        print(f"Title: {self.title}, Author: {self.author}")

book01 = Book("1984", "George Orwell")
book02 = Book("Green Eggs and Ham", "Dr Suess")

book01.getInfo()
book02.getInfo()
