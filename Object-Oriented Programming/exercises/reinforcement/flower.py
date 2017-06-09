class Flower:
    def __init__(self, name, number_of_petals, price):
        self._name = name
        self._number_of_petals = number_of_petals
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price