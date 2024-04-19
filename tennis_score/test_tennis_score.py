import pytest


@pytest.skip("Ignored", allow_module_level=True)
def test_start():
    assert True == False, "Not yet implemented!"
