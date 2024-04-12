# This is a common violation of OCP


class PaymentProcessor:
    def process_payment(self, type, amount):
        if type == "credit":
            self.process_credit_payment(amount)
        elif type == "paypal":
            self.process_paypal_payment(amount)
        # Each new payment method requires modifying this method

    def process_credit_payment(self, amount):
        print(f"Processing credit payment of {amount}")

    def process_paypal_payment(self, amount):
        print(f"Processing PayPal payment of {amount}")
