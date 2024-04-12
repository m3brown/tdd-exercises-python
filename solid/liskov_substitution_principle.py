# This is a common violation of Liskov Substitution Principle


class PaymentProcessor:
    def pay(self, amount):
        """Process a payment for the given amount."""
        raise NotImplementedError("Each subclass must implement this method.")

class CreditCardProcessor(PaymentProcessor):
    def __init__(self, card_number, cvv):
        self.card_number = card_number
        self.cvv = cvv

    def pay(self, amount):
        print(f"Processing ${amount} payment via Credit Card for card number {self.card_number}")

class PaypalProcessor(PaymentProcessor):
    def __init__(self, email_address):
        self.email_address = email_address

    def pay(self, amount):
        print(f"Processing ${amount} payment via PayPal for email {self.email_address}")

class DeferredPaymentProcessor(PaymentProcessor):
    def __init__(self, account_id):
        self.account_id = account_id
        self.deferred = True

    def pay(self, amount):
        if self.deferred:
            raise Exception("Payment is deferred and cannot be processed immediately. Please approve first.")
        print(f"Processing ${amount} payment for account {self.account_id}")

    def approve_payment(self):
        self.deferred = False


# Usage
def process_payment(processor, amount):
    try:
        processor.pay(amount)
    except Exception as e:
        print(f"Error: {e}")

# Create instances of payment processors
credit_card_processor = CreditCardProcessor("1234567890123456", "123")
paypal_processor = PaypalProcessor("user@example.com")
deferred_payment_processor = DeferredPaymentProcessor("account123")

# Process payments
process_payment(credit_card_processor, 50.00)
process_payment(paypal_processor, 25.00)
process_payment(deferred_payment_processor, 75.00)  # This will fail
#               ^^ needs special handling to approve payment
