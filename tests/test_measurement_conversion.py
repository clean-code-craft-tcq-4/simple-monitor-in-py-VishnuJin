import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from unit_conversion import get_celcius_from_fahrenheit, get_fahrenheit_from_celcius


def test_fahrenheit_to_celcius():
    assert get_celcius_from_fahrenheit(176) == 80


def test_celcius_to_fahrenheit():
    assert get_fahrenheit_from_celcius(20) == 68
