class Pizza:
    order_number = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients
        Pizza.order_number += 1
        self.order_number = Pizza.order_number

    @staticmethod
    def hawaiian():
        return Pizza("ham, pineapple".split(","))

    @staticmethod
    def meat_festival():
        return Pizza("beef, meatball, bacon".split(","))

    @staticmethod
    def garden_feast():
        return Pizza("spinach, olives, mushroom".split(","))


p1 = Pizza(["bacon", "parmesan", "ham"])    # order 1
p2 = Pizza.garden_feast()                  # order 2
print(p1.ingredients)  # ➞ ["bacon", "parmesan", "ham"]
print(p1.order_number)  # ➞ 1

print(p2.ingredients)  # ➞ ["spinach", "olives", "mushroom"]

print(p2.order_number)  # ➞ 2
