"""
cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())

"""

class Cup:
    def __init__(self, size:int, quantity:int):
        self.size = size
        self.quantity = quantity

    def status(self):
        return self.size - self.quantity

    def fill(self, millilitre):

        if self.status() >= millilitre:
            self.quantity += millilitre

cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())