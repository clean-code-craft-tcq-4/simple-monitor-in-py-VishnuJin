from battery_management_system.battery_management_system import BatteryManagementSystem as BMS

battery_validations = ["temperature", "state_of_charge", "current_rate"]


def battery_is_ok(temperature, state_of_charge, charge_rate):
    battery_metrics = BMS(temperature, state_of_charge, charge_rate)
    for metric in battery_validations:
        validation = getattr(battery_metrics, metric)
        if not validation.is_normal():
            return False
    return True


if __name__ == "__main__":
    assert battery_is_ok(25, 70, 0.7) is True
    assert battery_is_ok(50, 85, 0) is False
