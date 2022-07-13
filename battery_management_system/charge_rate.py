from battery_management_system.measurement_units.cr_units import ChargeRateUnits
from battery_management_system.template import BaseTemplate
from battery_treatments.charge_rate import ChargeRateTreatment
from config_parser import ConfigProvider


class ChargeRate(BaseTemplate, ChargeRateTreatment):
    def __init__(self, charge_rate) -> None:
        config_provider = ConfigProvider(
            "thresholds.ini", self, ChargeRateUnits.get_accepted_units()
        )
        self.MIN, self.MAX, self.tolerance, self.unit = config_provider.get_all_fields()
        self.MIN, self.MAX, self.charge_rate = map(
            self.convert_to_common_unit,
            [self.unit(self.MIN), self.unit(self.MAX), charge_rate],
        )
        BaseTemplate.__init__(self, self.charge_rate)

    def is_normal(self):
        return not self.is_high()

    def is_low(self):
        raise NotImplementedError

    def is_approaching_discharge(self):
        raise NotImplementedError

    def is_tolerance_level_breached(self):
        return self.is_approaching_peak()

    def convert_to_common_unit(self, value):
        return value.amps


if __name__ == "__main__":
    c = ChargeRate(0.1)
    c.provide_treatment()
