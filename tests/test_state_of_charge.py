import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from battery_management_system.state_of_charge import StateOfCharge


def test_low_state_of_charge():
    assert StateOfCharge(10).is_low() == True


def test_high_state_of_charge():
    assert StateOfCharge(100).is_high() == True


def test_normal_state_of_charge():
    assert StateOfCharge(60).is_normal() == True


def test_treatment_for_high_state_of_charge():
    assert StateOfCharge(110).provide_treatment() == True


def test_treatment_for_normal_state_of_charge():
    assert StateOfCharge(70).provide_treatment() == False


def test_treatment_for_low_state_of_charge():
    assert StateOfCharge(5).provide_treatment() == True
