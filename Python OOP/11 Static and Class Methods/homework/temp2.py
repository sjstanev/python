class Pizza:
    def __init__(self, ingredients: list[str]) -> None:
        self.ingredients = ingredients

    @classmethod
    def pepperoni(cls) -> 'Pizza':
        return cls(["tomato sauce", "parmesan", "pepperoni"])


    @classmethod
    def quattro_formaggi(cls) -> 'Pizza':
        return cls(["mozzarella", "gorgonzola", "fontina", "parmigiana"])

first_pizza = Pizza.pepperoni()
second_pizza = Pizza.quattro_formaggi()
print(first_pizza)
print(second_pizza)


a = {"item": 1, "item2":2, "item3":3, "item4":4}
for x in a.values():
    print(x)

y = sum([s for s in a.values()])
print(y)
print(a["item5"])
print(a["item3"])
if a["item3"]:
    print('yes')
else:
    print('nope')
