class PizzaDelivery:

    def __init__(self, name:str, price:float, ingredients:dict):
        self.name = name                # Margarita
        self.price = price              # 11
        self.ingredients = ingredients  # {'cheese': 2, 'tomatoes': 1}
        self.ordered = False

    def add_extra(self, ingredient:str, quantity:int, price_per_quantity:float)-> str:
        """
        If we already have this ingredient in our pizza, increase the ingredient quantity
        If we do not have this ingredient in our pizza, we should add it and update the pizza price
        :param ingredient: mozzarella
        :param quantity: 1
        :param price_per_quantity: 0.5
        :return:
        """
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        # dictionary.get(keyname, value)
        # key: required
        # value: Optional. A value to return if the specified key does not exist
        # Example this is equivalent to:
        #
        # if ingredient in self.ingredients:
        #     self.ingredients[ingredient] += quantity
        #
        # else:
        #     self.ingredients[ingredient] = quantity

        self.ingredients[ingredient] = self.ingredients.get(ingredient, 0) + quantity
        self.price += price_per_quantity * quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float)->str:
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        if quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"
        self.ingredients[ingredient] -= quantity
        self.price -= price_per_quantity * quantity

    def make_order(self)->str:

        self.ordered = True
        ingredient_quantity = ', '.join(f"{k}: {v}" for k, v in self.ingredients.items())
        return  (f"You've ordered pizza {self.name} prepared with "
                 f"{ingredient_quantity} "
                 f"and the price will be {self.price}lv.")




margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))