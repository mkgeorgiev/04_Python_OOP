import sys

from project.peaks.base_peak import BasePeak


class SummitPeak(BasePeak):
    RECOMMENDED_GEAR = ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]
    PEAK_DIFFICULTY = {"Extreme": {"min":2501, 'max': sys.maxsize}, "Advanced": {"min": 1500, "max":2500}}
    IS_PEAK_CONQUERED = False


    def get_recommended_gear(self):
        return self.RECOMMENDED_GEAR

    def calculate_difficulty_level(self):
        for difficulty in self.PEAK_DIFFICULTY:
            if self.elevation >= self.PEAK_DIFFICULTY[difficulty]["min"]:
                return difficulty
            if self.PEAK_DIFFICULTY[difficulty]["min"] <= self.elevation <= self.PEAK_DIFFICULTY[difficulty]["max"]:
                return difficulty

            # what to do if peak is less than Advanced values


