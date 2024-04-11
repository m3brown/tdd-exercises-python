import pytest
from vending_machine import VendingMachine

def test_release_change_when_no_coins_expect_no_change():
    # Arrange
    class_under_test = VendingMachine()
    # Act
    actual_coins = class_under_test.release_change()
    # Assert
    assert actual_coins == 0

def test_release_change_when_one_coin_expect_some_change():
    # Arrange
    class_under_test = VendingMachine()
    class_under_test.insert_coin()
    # Act
    actual_coins = class_under_test.release_change()
    # Assert
    assert actual_coins != 0

def test_release_change_when_7c_inserted_expect_7c_returned():
    # Arrange
    cut = VendingMachine()
    # insert 7 coins
    cut.insert_coin()
    cut.insert_coin()
    cut.insert_coin()
    cut.insert_coin()
    cut.insert_coin()
    cut.insert_coin()
    cut.insert_coin()
    # Act
    actual = cut.release_change()
    # Assert
    assert actual == 7

def test_buy_product_when_no_coins_expect_no_product():
    # Arrange
    cut = VendingMachine()
    # Act
    actual_product = cut.buy_product()
    # Assert
    assert actual_product is None

def test_buy_product_when_2c_inserted_expect_product():
    # Arrange
    cut = VendingMachine()
    cut.insert_coin()
    cut.insert_coin()
    # Act
    actual = cut.buy_product()
    # Assert
    assert actual is not None

def test_buy_product_when_5c_inserted_expect_product():
    # Arrange
    cut = VendingMachine()
    cut.insert_coin()
    cut.insert_coin()
    cut.insert_coin()
    cut.insert_coin()
    cut.insert_coin()
    # Act
    actual = cut.buy_product()
    # Assert
    assert actual == 'cola'

def test_buy_product_when_product_already_purchase_expect_no_2nd_product():
    # Arrange
    cut = VendingMachine()
    cut.insert_coin()
    cut.insert_coin()
    product = cut.buy_product()
    assert product == 'cola'
    # Act
    actual = cut.buy_product()
    # Assert
    assert actual is None

def test_buy_product_when_3c_and_buy_product_expect_1c_change():
    # Arrange
    cut = VendingMachine()
    cut.insert_coin()
    cut.insert_coin()
    cut.insert_coin()
    product = cut.buy_product()
    assert product == 'cola'
    # Act
    actual_change = cut.change_return
    # Assert
    assert actual_change == 1

def test_release_change_when_change_already_released_expect_no_change():
    # Arrange
    cut = VendingMachine()
    cut.insert_coin()
    cut.insert_coin()
    cut.insert_coin()
    cut.release_change()
    # Act
    actual = cut.release_change()
    # Assert
    assert actual == 0

def test_release_change_when_buy_product_releases_change_expect_no_change():
    # Arrange
    cut = VendingMachine()
    cut.insert_coin()
    cut.insert_coin()
    cut.insert_coin()
    cut.buy_product()
    change = cut.change_return
    assert change == 1
    # Act
    actual = cut.release_change()
    # Assert
    assert actual == 0
