# Use the -s flag to view STDOUT
# pytest -s test_fixtures_multiple.py
import pytest


@pytest.fixture
def foo():
    return "FOO"


@pytest.fixture
def bar(foo):
    return foo+"BAR"


@pytest.fixture
def baz(foo, bar):
    return foo+bar+"BAZ"


@pytest.fixture(autouse=True)
def auto():
    print()
    print("AUTO")


def test_auto():
    pass


def test_multi(foo, bar, baz):
    print(f"{foo=}")
    print(f"{bar=}")
    print(f"{baz=}")
