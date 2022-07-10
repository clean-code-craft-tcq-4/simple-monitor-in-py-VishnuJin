from unittest import result

# from battery_management_system.battery_management_system import BatteryManagementSystem as BMS
from battery_management_system.charge_rate import ChargeRate
from battery_management_system.state_of_charge import StateOfCharge
from battery_management_system.temperature import Temperature


def battery_is_ok(validations):
    for validation in validations:
        if not validation.is_normal():
            return False
    return True


def get_Validation_list(temperature, state_of_charge, current_rate):
    validations = []
    validations.append(Temperature(temperature))
    validations.append(StateOfCharge(state_of_charge))
    validations.append(ChargeRate(current_rate))
    return validations


if __name__ == "__main__":
    assert battery_is_ok(get_Validation_list(25, 70, 0.7)) is True
    assert battery_is_ok(get_Validation_list(50, 85, 0)) is False
