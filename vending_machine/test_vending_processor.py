from unittest.mock import patch, MagicMock

from payment_processor import PaymentProcessor
from vending_machine import VendingMachine


@patch("payment_processor.PaymentProcessor.refund_payment")  # mock arg 1
def test_release_change_when_refund_payment_expect_patch_return_value(
    mock_refund_payment,
):
    # Arrange
    mock_refund_payment.return_value = 0  # patch the return
    payment_processor = PaymentProcessor()
    cut = VendingMachine(payment_processor)
    # Act
    actual = cut.release_change()
    # Assert
    assert actual == 0


def test_release_change_when_no_payment_expect_no_payment():
    # Arrange
    mock_processor = MagicMock()
    mock_processor.refund_payment.return_value = 0
    cut = VendingMachine(mock_processor)
    # Act
    actual = cut.release_change()
    # Assert
    assert actual == 0


def test_release_change_when_payment_expect_a_payment():
    # Arrange
    mock_processor = MagicMock()
    mock_processor.refund_payment.return_value = 101
    cut = VendingMachine(mock_processor)
    cut.insert_coin()
    # Act
    actual = cut.release_change()
    # Assert
    assert actual == 101


def test_insert_coin_when_called_expect_processor_make_payment_1x():
    # Arrange
    mock_processor = MagicMock()
    cut = VendingMachine(mock_processor)
    # Act
    cut.insert_coin()
    # Assert
    mock_processor.make_payment.assert_called_once()
