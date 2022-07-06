from battery_management_system.template import BaseTemplate
from battery_treatments.state_of_charge import StateOfChargeTreatment


class StateOfCharge(BaseTemplate, StateOfChargeTreatment):
    def __init__(self, state_of_charge) -> None:
        BaseTemplate.__init__(self, state_of_charge)
        self.state_of_charge = state_of_charge
