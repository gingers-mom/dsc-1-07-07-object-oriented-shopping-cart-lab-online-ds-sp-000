import statistics

class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        self.total = 0
        self.employee_discount = emp_discount
        self.items = []
        pass

    def add_item(self, name, price, quantity=1):
        for i in range(quantity):
            self.items.append(price)
            self.total += price
        return self.total

    def mean_item_price(self):
        return self.total / len(self.items)


    def median_item_price(self):
        return statistics.median(self.items)


    def apply_discount(self):
        if self.employee_discount:
            return self.total - (self.total * (self.employee_discount / 100))
        else:
            return "Sorry, there is no discount to apply to your cart :("

    def void_last_item(self):
        if len(self.items) == 0:
            return "There are no items in your cart!"
        else:
            self.total = self.total - self.items[len(self.items) - 1]
            return self.total
