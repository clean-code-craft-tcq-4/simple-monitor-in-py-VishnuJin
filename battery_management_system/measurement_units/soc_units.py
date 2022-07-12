from battery_management_system.measurement_units.unit import Units


class StateOfChargeUnits(Units):
    def get_accepted_units():
        return [unit.__name__ for unit in StateOfChargeUnits.__subclasses__()]


class Percentage(StateOfChargeUnits):
    def __init__(self, percentage) -> None:
        self.percentage = percentage
