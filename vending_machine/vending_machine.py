# vending_machine.py
# https://github.com/valenjet/tdd-exercises-python

from payment_processor import PaymentProcessor

PRICE = 2


class VendingMachine:
    def __init__(self, payment_processor: PaymentProcessor):
        self._change_return = 0
        self._payment_processor = payment_processor
        return

    def release_change(self):
        self._change_return = self._payment_processor.refund_payment()
        return self._change_return

    def insert_coin(self):
        self._payment_processor.make_payment()

    def buy_product(self):
        if self._payment_processor.is_payment_made(PRICE):
            self._payment_processor.process_payment(PRICE)
            self.release_change()
            return "cola"
        return

    def empty_change_return(self):
        coins = self._change_return
        self._change_return = 0
        return coins
