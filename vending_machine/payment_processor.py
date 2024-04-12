class PaymentProcessor:
    _coins = 0

    def __init__(self) -> None:
        pass

    def make_payment(self):
        self._coins += 1
    
    def process_payment(self, price):
        self._coins -= price

    def is_payment_made(self, price):
        if self._coins >= price:
            return True
        return False

    def refund_payment(self):
        coins = self._coins
        self._coins = 0
        return coins

