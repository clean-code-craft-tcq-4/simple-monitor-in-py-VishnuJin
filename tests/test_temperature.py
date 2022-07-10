import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from battery_management_system.temperature import Temperature


def test_low_temperature():
    assert Temperature(-1).is_low() == True


def test_high_temperature():
    assert Temperature(100).is_high() == True


def test_normal_temperature():
    assert Temperature(30).is_normal() == True


def test_treatment_for_high_temperature():
    assert Temperature(60).provide_treatment() == True


def test_treatment_for_normal_temperature():
    assert Temperature(30).provide_treatment() == False


def test_treatment_for_low_temperature():
    assert Temperature(-10).provide_treatment() == True
