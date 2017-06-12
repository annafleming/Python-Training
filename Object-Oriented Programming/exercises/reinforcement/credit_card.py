class CreditCard:
    def __init__(self, customer, bank, acnt, limit, balance=0):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance

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
        if amount < 0:
            raise ValueError('Payment amount cannot be negative')
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


class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._total_charges = 0

    def charge(self, price):
        self._total_charges += 1
        success = super().charge(price)
        if not success:
            self._balance += 5
        return success

    def process_month(self):
        if self._balance > 0:
            additional_charge = self._total_charges - 12 if self._total_charges > 12 else 0
            monthly_factor = pow(1 + self._apr, 1 / 12) + additional_charge
            self._balance = monthly_factor
