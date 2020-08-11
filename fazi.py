from random import randint
class Dice:
    def roll(self):
        return randint(1,6), randint(1,6)


a=Dice()
print(a.roll())

