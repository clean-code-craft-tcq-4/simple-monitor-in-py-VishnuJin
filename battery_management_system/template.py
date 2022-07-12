import os, sys

SCRIPT_DIR = SCRIPT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from battery_management_system.battery_states import BatteryState


class BaseTemplate:
    def __init__(self, value) -> None:
        self.state = BatteryState.Normal
        self.__value = value

    def is_low(self):
        if self.__value < self.MIN:
            self.state = BatteryState.Low
            return True
        return False

    def is_high(self):
        if self.__value > self.MAX:
            self.state = BatteryState.High
            return True
        return False

    def is_normal(self):
        return not (self.is_high() or self.is_low())

    def provide_treatment(self):
        self.is_normal()
        return getattr(self, f"for_{str(self.state.name).lower()}")()

    def is_tolerance_level_breached(self):
        return self.is_approaching_discharge() or self.is_approaching_peak()

    def is_approaching_discharge(self):
        return self.__value <= (self.MIN + self.tolerance)

    def is_approaching_peak(self):
        return self.__value >= (self.MAX - self.tolerance)

    def convert_to_common_unit(self, value):
        raise NotImplementedError
