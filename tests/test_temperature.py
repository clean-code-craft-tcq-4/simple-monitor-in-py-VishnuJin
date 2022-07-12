import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from battery_management_system.temperature import Temperature
from battery_management_system.measurement_units.temperature_units import (
    Celcius,
    Fahrenheit,
)


def test_low_temperature():
    assert Temperature(Celcius(-1)).is_low() == True


def test_high_temperature():
    assert Temperature(Celcius(100)).is_high() == True


def test_normal_temperature():
    assert Temperature(Celcius(30)).is_normal() == True


def test_treatment_for_high_temperature():
    assert Temperature(Celcius(60)).provide_treatment() == True


def test_treatment_for_normal_temperature():
    assert Temperature(Celcius(30)).provide_treatment() == False


def test_treatment_for_low_temperature():
    assert Temperature(Celcius(-10)).provide_treatment() == True


def test_warning_low_tolerance():
    assert Temperature(Celcius(2)).is_approaching_discharge() == True


def test_warning_peak_tolerance():
    assert Temperature(Celcius(43)).is_approaching_peak() == True


def test_warning_tolerance_breach():
    assert Temperature(Celcius(25)).is_tolerance_level_breached() == False


def test_high_temperature_with_fahrenheit():
    assert Temperature(Fahrenheit(212)).is_high() == True


def test_low_temperature_with_fahrenheit():
    assert Temperature(Fahrenheit(31)).is_high() == False
