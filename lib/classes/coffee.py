import ipdb

from classes.order import Order

class Coffee:

    all = []

    def __init__(self, name):
        if type(name) == str:
            self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, "_name"):
            self._name = name
        else:
            print("Can't change the name of the coffee!")

    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        customers = []
        for order in self.orders():
            if order.customer not in customers:
                customers.append(order.customer)
        return customers
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        total = 0
        for order in self.orders():
            total += order.price
        return total / len(self.orders())
        

# mocha = Coffee("mocha")
# latte = Coffee("latte")
# coffee = Coffee("coffee")