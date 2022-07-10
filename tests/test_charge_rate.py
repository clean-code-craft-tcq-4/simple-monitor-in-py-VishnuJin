import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from battery_management_system.charge_rate import ChargeRate
from exception_handlers import get_error_type


def test_low_charge_rate():
    assert get_error_type(ChargeRate(0.1).is_low) == NotImplementedError


def test_high_charge_rate():
    assert ChargeRate(1.0).is_high() == True


def test_normal_charge_rate():
    assert ChargeRate(0.5).is_normal() == True


def test_treatment_for_normal_charge_rate():
    assert ChargeRate(0.5).provide_treatment() == False


def test_treatment_for_high_charge_rate():
    assert ChargeRate(1.0).provide_treatment() == True


def test_treatment_for_normal_charge_rate():
    assert ChargeRate(0.5).provide_treatment() == False


def test_treatment_for_low_charge_rate():
    assert ChargeRate(0.1).provide_treatment() == False
