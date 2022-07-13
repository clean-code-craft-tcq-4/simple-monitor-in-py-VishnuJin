from battery_management_system.charge_rate import ChargeRate
from battery_management_system.state_of_charge import StateOfCharge
from battery_management_system.temperature import Temperature
from battery_management_system.measurement_units.temperature_units import (
    Fahrenheit,
    Celcius,
)
from battery_management_system.measurement_units.cr_units import Amps
from battery_management_system.measurement_units.soc_units import Percentage



def battery_is_ok(validations):
    for validation in validations:
        if not validation.is_normal():
            return False
    return True


def get_Validation_list(temperature, state_of_charge, charge_rate):
    validations = []
    validations.append(Temperature(temperature))
    validations.append(StateOfCharge(state_of_charge))
    validations.append(ChargeRate(charge_rate))
    return validations


if __name__ == "__main__":
    assert (
        battery_is_ok(get_Validation_list(Fahrenheit(77), Percentage(50), Amps(0.7)))
        == True
    )
    assert (
        battery_is_ok(get_Validation_list(Celcius(25), Percentage(70), Amps(0.5)))
        is True
    )
    assert (
        battery_is_ok(get_Validation_list(Celcius(50), Percentage(85), Amps(0.1)))
        is False
    )
    assert (
        battery_is_ok(get_Validation_list(Celcius(25), Percentage(70), Amps(0.9)))
        is False
    )
