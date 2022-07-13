from battery_treatments.treatment_template import TreatmentTemplate


class ChargeRateTreatment(TreatmentTemplate):
    def for_low(self):
        raise NotImplementedError
