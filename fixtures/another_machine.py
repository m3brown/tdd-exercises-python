# another_machine.py

PRICE = 2


class AnotherMachine:
    _coins = 0
    change_return = 0

    def __init__(self):
        return

    def release_change(self):
        change = self._coins
        self._coins = 0
        return change

    def insert_coin(self):
        self._coins += 1

    def buy_product(self):
        if self._coins >= PRICE:
            self._coins -= PRICE
            self.change_return = self._coins
            self._coins = 0
            return "cola"
        return
