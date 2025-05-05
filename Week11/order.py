from delivery import Delivery
import random
import datetime

class Order:
    def __init__(self, name, details):
        self.name = name
        self.details = details
        self.ID = 0
    def setOrder(self):
        self.ID = random.randint(0, 999999999)
        user_delivery = Delivery(self.ID, self.name, self.details, datetime.date.today(), user_address)
        user_delivery.processDelivery()

user_order = Order("Apple Airpod Pros", "Very overly expensive headphones")
user_address = "40 Launceston Street, Phillip, ACT"

# This implementation means the order is only given an ID once finalised to ensure IDs are not wasted on unfinished orders 
user_order.setOrder()