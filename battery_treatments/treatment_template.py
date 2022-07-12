class TreatmentTemplate:
    def for_high(self):
        print(f"Current state of battery {type(self).__name__} is {self.state.name}")
        print("treatment provided..")
        return True

    def for_low(self):
        print(f"Current state of battery {type(self).__name__} is {self.state.name}")
        print("treatment provided..")
        return True

    def for_normal(self):
        print(f"Current state of battery {type(self).__name__} is {self.state.name}")
        print("no treatment required..")
        return False
