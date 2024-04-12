import time

SLEEP_TIME = 5
PAYMENT_TABLE = 'payments'

class PaymentDao:
    def __init__(self, initial_value: int = 0):
        self._storage = { PAYMENT_TABLE: initial_value }

    def retrieve(self) -> int:
        print('\nCalling PaymentDao.retrieve()')
        time.sleep(SLEEP_TIME)
        return self._storage[PAYMENT_TABLE]

    def save(self, payment: int) -> None:
        print('\nCalling PaymentDao.save()')
        time.sleep(SLEEP_TIME)
        self._storage[PAYMENT_TABLE] = payment