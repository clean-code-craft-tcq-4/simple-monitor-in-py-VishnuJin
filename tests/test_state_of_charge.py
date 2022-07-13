import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from battery_management_system.state_of_charge import StateOfCharge
from battery_management_system.measurement_units.soc_units import Percentage


def test_low_state_of_charge():
    assert StateOfCharge(Percentage(10)).is_low() == True


def test_high_state_of_charge():
    assert StateOfCharge(Percentage(100)).is_high() == True


def test_normal_state_of_charge():
    assert StateOfCharge(Percentage(60)).is_normal() == True


def test_treatment_for_high_state_of_charge():
    assert StateOfCharge(Percentage(110)).provide_treatment() == True


def test_treatment_for_normal_state_of_charge():
    assert StateOfCharge(Percentage(70)).provide_treatment() == False


def test_treatment_for_low_state_of_charge():
    assert StateOfCharge(Percentage(5)).provide_treatment() == True


def test_warning_low_tolerance():
    assert StateOfCharge(Percentage(22)).is_approaching_discharge() == True


def test_warning_peak_tolerance():
    assert StateOfCharge(Percentage(78)).is_approaching_peak() == True


def test_warning_tolerance_breach():
    assert StateOfCharge(Percentage(60)).is_tolerance_level_breached() == False
