class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def make_payment(self, amount):
        try:
            amount = float(amount)
        except:
            raise Exception('Paid amount should be a number')

        self._balance -= amount

    def charge(self, price):
        try:
            price = float(price)
        except:
            raise Exception('Charged amount should be a number')

        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
