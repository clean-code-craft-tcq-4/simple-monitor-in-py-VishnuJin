from battery_management_system.battery_states import BatteryState
from configparser import ConfigParser

class BaseTemplate:
    def __init__(self, value) -> None:
        # configparser is kinda limited in auto serialization but servers fine for this simple example
        self.config = ConfigParser()
        self.config.read("./thresholds.ini")
        self.MIN = self.config.getfloat(f"{type(self).__name__}", "MIN")
        self.MAX = self.config.getfloat(f"{type(self).__name__}", "MAX")
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
