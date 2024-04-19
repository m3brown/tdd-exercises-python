import pytest
from temperature_converter import TemperatureConverter


def test_convert_ctof_when_0c_expect_32f():
    converter = TemperatureConverter()
    temp_f = converter.convert_ctof(0)
    assert temp_f == 32


def test_conver_ctof_when_100c_expect_212f():
    converter = TemperatureConverter()
    temp_f = converter.convert_ctof(100)
    assert temp_f == 212


def test_convert_ctof_when_m40c_expect_m40f():
    converter = TemperatureConverter()
    temp_f = converter.convert_ctof(-40)
    assert temp_f == -40


def test_convert_ctof_when_10c_expect_50f():
    converter = TemperatureConverter()
    temp_f = converter.convert_ctof(10)
    assert temp_f == 50


def test_convert_ctof_when_37c_expect_98_pt_6f():
    converter = TemperatureConverter()
    temp_f = converter.convert_ctof(37)
    assert temp_f == 98.6
