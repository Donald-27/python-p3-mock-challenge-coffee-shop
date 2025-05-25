class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []
        
    def orders(self):
        return self._orders
    
    def customers(self):
     
        return list({order.customer for order in self._orders})
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        if not self._orders:
            return 0
        total = sum(order.price for order in self._orders)
        return total / len(self._orders)

class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = [] 
        
    def orders(self):
        return self._orders
    
    def coffees(self):
     
        return list({order.coffee for order in self._orders})
    
    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._orders.append(order) 
        return order
    
class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
