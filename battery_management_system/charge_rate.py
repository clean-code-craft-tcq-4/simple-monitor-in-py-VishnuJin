from ast import Not
from battery_management_system.template import BaseTemplate
from battery_treatments.charge_rate import ChargeRateTreatment
from config_parser import ConfigProvider


class ChargeRate(BaseTemplate, ChargeRateTreatment):
    def __init__(self, charge_rate) -> None:
        config_provider = ConfigProvider()
        self.config = config_provider.parse_config("thresholds.ini")
        self.MAX = config_provider.get_value(self, "MAX")
        self.charge_rate = charge_rate
        BaseTemplate.__init__(self, charge_rate)

    def is_normal(self):
        return not self.is_high()

    def is_low(self):
        raise NotImplementedError


if __name__ == "__main__":
    c = ChargeRate(0.1)
    c.provide_treatment()
