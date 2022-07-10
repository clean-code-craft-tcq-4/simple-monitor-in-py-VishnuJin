from battery_management_system.template import BaseTemplate
from battery_treatments.temperature import TemperatureTreatment
from config_parser import ConfigProvider


class Temperature(BaseTemplate, TemperatureTreatment):
    def __init__(self, temperature) -> None:
        config_provider = ConfigProvider()
        self.config = config_provider.parse_config("thresholds.ini")
        self.MIN = config_provider.get_value(self, "MIN")
        self.MAX = config_provider.get_value(self, "MAX")
        self.temperature = temperature
        BaseTemplate.__init__(self, temperature)


if __name__ == "__main__":
    t = Temperature(100)
    t.provide_treatment()
