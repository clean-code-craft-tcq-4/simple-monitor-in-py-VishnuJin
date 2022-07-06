from battery_management_system.template import BaseTemplate
from battery_treatments.temperature import TemperatureTreatment


class Temperature(BaseTemplate, TemperatureTreatment):
    def __init__(self, temperature) -> None:
        BaseTemplate.__init__(self, temperature)
        self.temperature = temperature


if __name__ == "__main__":
    t = Temperature(100)
    t.provide_treatment()
