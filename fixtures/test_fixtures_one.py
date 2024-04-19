import pytest

from another_machine import AnotherMachine


@pytest.fixture()
def machine_with_one_dollar():
    machine = AnotherMachine()
    machine.insert_coin()
    machine.insert_coin()
    machine.insert_coin()
    machine.insert_coin()
    return machine


def test_release_change_when_x_expect_y(machine_with_one_dollar):
    # Arrange
    machine_with_one_dollar.release_change()
    # Act
    actual = machine_with_one_dollar.change_return
    # Assert
    assert actual == 5
