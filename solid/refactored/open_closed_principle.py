from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit payment of {amount}")

class PayPalPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount}")

class PaymentManager:
    def execute_payment(self, processor, amount):
        processor.process_payment(amount)

# Usage
payment_manager = PaymentManager()
credit_processor = CreditPaymentProcessor()
paypal_processor = PayPalPaymentProcessor()

payment_manager.execute_payment(credit_processor, 100)
payment_manager.execute_payment(paypal_processor, 200)
