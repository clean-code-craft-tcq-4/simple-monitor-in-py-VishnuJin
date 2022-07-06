from battery_management_system.temperature import Temperature
from battery_management_system.state_of_charge import StateOfCharge
from battery_management_system.charge_rate import ChargeRate


class BatteryManagementSystem:
    def __init__(self, temperature, state_of_charge, current_rate) -> None:
        self.temperature = Temperature(temperature)
        self.state_of_charge = StateOfCharge(state_of_charge)
        self.current_rate = ChargeRate(current_rate)

if __name__ == "__main__":
    b = BatteryManagementSystem(10, 20, 0.9)
