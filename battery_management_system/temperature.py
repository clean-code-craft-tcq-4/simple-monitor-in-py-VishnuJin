from battery_management_system.template import BaseTemplate
from battery_treatments.temperature import TemperatureTreatment
from battery_management_system.measurement_units.temperature_units import (
    TemperatureUnits,
)
from config_parser import ConfigProvider


class Temperature(BaseTemplate, TemperatureTreatment):
    def __init__(self, temperature) -> None:
        config_provider = ConfigProvider(
            "thresholds.ini", self, TemperatureUnits.get_accepted_units()
        )
        self.MIN, self.MAX, self.tolerance, self.unit = config_provider.get_all_fields()
        self.MIN, self.MAX, self.temperature = map(
            self.convert_to_common_unit,
            [self.unit(self.MIN), self.unit(self.MAX), temperature],
        )
        BaseTemplate.__init__(self, self.temperature)

    def __convert_to_celcius(self, temperature):
        try:
            return temperature.convert_to_celcius()
        except:
            raise ValueError(f"No unit available as {type(temperature)}")

    def convert_to_common_unit(self, temperature):
        return self.__convert_to_celcius(temperature)

if __name__ == "__main__":
    t = Temperature(100)
    t.provide_treatment()
