from battery_management_system.measurement_units.soc_units import StateOfChargeUnits
from battery_management_system.template import BaseTemplate
from battery_treatments.state_of_charge import StateOfChargeTreatment
from config_parser import ConfigProvider


class StateOfCharge(BaseTemplate, StateOfChargeTreatment):
    def __init__(self, state_of_charge) -> None:
        config_provider = ConfigProvider(
            "thresholds.ini", self, StateOfChargeUnits.get_accepted_units()
        )
        self.MIN, self.MAX, self.tolerance, self.unit = config_provider.get_all_fields()
        self.MIN, self.MAX, self.state_of_charge = map(
            self.convert_to_common_unit,
            [self.unit(self.MIN), self.unit(self.MAX), state_of_charge],
        )
        BaseTemplate.__init__(self, self.state_of_charge)

    def convert_to_common_unit(self, value):
        return value.percentage
