from battery_management_system.template import BaseTemplate
from battery_treatments.charge_rate import ChargeRateTreatment


class ChargeRate(BaseTemplate, ChargeRateTreatment):
    def __init__(self, charge_rate) -> None:
        BaseTemplate.__init__(self, charge_rate)
        self.charge_rate = charge_rate


if __name__ == "__main__":
    c = ChargeRate(0.1)
    c.provide_treatment()
