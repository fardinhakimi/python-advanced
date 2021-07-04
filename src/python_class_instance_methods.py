
class BasePizza:
    ingredients = []

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def get_ingredients(self):
        return self.ingredients


class Pizza(BasePizza):

    def __init__(self, ingredients):
        super().__init__(ingredients)

    @classmethod
    def type1(cls):
        return cls(['ing1', 'ing2'])

    def get_ings(self):
        return self.ingredients

    @classmethod
    def type2(cls):
        return cls(['ing3', 'ing4'])

    @staticmethod
    def some_random_shit():
        return 'some random shit'


print(Pizza.type1().get_ings())
print(Pizza.type2().get_ings())
print(Pizza.some_random_shit())


pizza = Pizza(['tomato', 'onion'])

print(pizza.get_ings())


if __name__ == '__main__':
    pass