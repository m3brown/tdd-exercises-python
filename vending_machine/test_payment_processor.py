from payment_processor import PaymentProcessor


def test_is_payment_made_when_no_payment_expect_false():
    # Arrange
    cut = PaymentProcessor()
    # Act
    actual = cut.is_payment_made(2)
    # Assert
    assert actual == False


def test_is_payment_made_when_full_payment_expect_true():
    # Arrange
    cut = PaymentProcessor()
    cut.make_payment()
    cut.make_payment()
    # Act
    actual = cut.is_payment_made(2)
    # Assert
    assert actual == True


def test_is_payment_made_when_excess_payment_expect_true():
    # Arrange
    cut = PaymentProcessor()
    cut.make_payment()
    cut.make_payment()
    cut.make_payment()
    cut.make_payment()
    # Act
    actual = cut.is_payment_made(3)
    # Assert
    assert actual == True


def test_refund_payment_when_no_payment_expect_no_refund():
    # Arrange
    cut = PaymentProcessor()
    # Act
    actual = cut.refund_payment()
    # Assert
    assert actual == 0


def test_refund_payment_when_one_payment_expect_one_refund():
    # Arrange
    cut = PaymentProcessor()
    cut.make_payment()
    # Act
    actual = cut.refund_payment()
    # Assert
    assert actual == 1


def test_is_payment_made_when_payment_processed_expect_false():
    # Arrange
    cut = PaymentProcessor()
    cut.make_payment()
    cut.make_payment()
    cut.make_payment()
    cut.process_payment(2)
    # Act
    actual = cut.is_payment_made(3)
    # Assert
    assert actual == False


def test_is_payment_made_when_payment_processed_twice_expect_false():
    # Arrange
    cut = PaymentProcessor()
    cut.make_payment()
    cut.make_payment()
    cut.make_payment()
    cut.process_payment(1)
    cut.process_payment(1)
    # Act
    actual = cut.is_payment_made(3)
    # Assert
    assert actual == False
