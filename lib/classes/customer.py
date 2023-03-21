from classes.order import Order

class Customer:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if (type(name) == str) and (1 <= len(name) <= 15):
            self._name = name

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        coffees = []
        for order in self.orders():
            if order.coffee not in coffees:
                coffees.append(order.coffee)
        return coffees
    
    def create_order(self, coffee, price):
        if type(price) == int:
            Order(self, coffee, price)