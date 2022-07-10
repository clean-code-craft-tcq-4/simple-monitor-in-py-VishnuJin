from battery_management_system.template import BaseTemplate
from battery_treatments.state_of_charge import StateOfChargeTreatment
from config_parser import ConfigProvider


class StateOfCharge(BaseTemplate, StateOfChargeTreatment):
    def __init__(self, state_of_charge) -> None:
        config_provider = ConfigProvider()
        self.config = config_provider.parse_config("thresholds.ini")
        self.MIN = config_provider.get_value(self, "MIN")
        self.MAX = config_provider.get_value(self, "MAX")
        self.state_of_charge = state_of_charge
        BaseTemplate.__init__(self, state_of_charge)
