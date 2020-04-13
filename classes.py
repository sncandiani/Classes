class Pizza: 
    def __init__(self, size, crust_type, toppings):
        self.size = size
        self.crust_type = crust_type
        self.toppings = toppings

    def add_topping(self): 
        self.append(toppings)
    
    def print_order(self):
        print(f"I would like a {self.size}, {self.crust_type} pizza with {self.toppings}")
