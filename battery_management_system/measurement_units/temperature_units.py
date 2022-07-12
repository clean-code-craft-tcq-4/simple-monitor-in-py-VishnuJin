from battery_management_system.measurement_units.unit import Units
from unit_conversion import get_celcius_from_fahrenheit, get_fahrenheit_from_celcius
from abc import abstractclassmethod


class TemperatureUnits(Units):
    @abstractclassmethod
    def convert_to_celcius(self):
        raise NotImplementedError

    @staticmethod
    def get_accepted_units():
        return [unit.__name__ for unit in TemperatureUnits.__subclasses__()]


class Celcius(TemperatureUnits):
    def __init__(self, celcius) -> None:
        self.celcius = celcius

    def convert_to_celcius(self):
        return self.celcius

    def convert_to_fahrenheit(self, celcius):
        return get_fahrenheit_from_celcius(celcius)


class Fahrenheit(TemperatureUnits):
    def __init__(self, fahrenheit) -> None:
        self.fahrenheit = fahrenheit

    def convert_to_celcius(self):
        return get_celcius_from_fahrenheit(self.fahrenheit)

    def convert_to_fahrenheit(self, _celcius):
        return self.fahrenheit
