from configparser import ConfigParser
from unit_conversion import get_value_for_percentage
from battery_management_system.measurement_units.temperature_units import (
    Fahrenheit,
    Celcius,
)
from battery_management_system.measurement_units.cr_units import Amps
from battery_management_system.measurement_units.soc_units import Percentage


class ConfigProvider:
    def __init__(self, filename, category, accpeted_units) -> None:
        self.filename = filename
        self.category = category
        self.config = self.parse_config(self.filename)
        self.accepted_units = accpeted_units

    def parse_config(self, filename):
        config = ConfigParser()
        config.read(filename)
        return config

    def get_value(self, category, field, value_type):
        try:
            value = self.config.get(f"{type(category).__name__}", field)
        except:
            value = None
        return value_type(value) if value else None

    def get_tolerance(self, category):
        return get_value_for_percentage(
            self.get_value(category, "warning_tolerance_percentage", float),
            self.get_max(self.category),
        )

    def get_max(self, category):
        return self.get_value(category, "MAX", float)

    def get_min(self, category):
        return self.get_value(category, "MIN", float)

    def get_all_fields(self):
        return (
            self.get_min(self.category),
            self.get_max(self.category),
            self.get_tolerance(self.category),
            self.get_unit(self.category),
        )

    def get_unit(self, category):
        accepted_units = self.accepted_units
        given_unit = self.get_value(category, "unit", str)
        if given_unit in accepted_units:
            return eval(f"{given_unit}")
        raise ValueError(f"no unit as {given_unit}\nOnly {accepted_units} are accepted")
