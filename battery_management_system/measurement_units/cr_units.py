from battery_management_system.measurement_units.unit import Units


class ChargeRateUnits(Units):
    def get_accepted_units():
        return [unit.__name__ for unit in ChargeRateUnits.__subclasses__()]


class Amps(ChargeRateUnits):
    def __init__(self, amps) -> None:
        self.amps = amps
