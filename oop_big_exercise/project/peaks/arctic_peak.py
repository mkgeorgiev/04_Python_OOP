import sys

from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):
    RECOMMENDED_GEAR = ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]
    PEAK_DIFFICULTY = {"Extreme": {"min":3001, 'max': sys.maxsize}, "Advanced": {"min": 2000, "max":3000}}
    IS_PEAK_CONQUERED = False


    def get_recommended_gear(self):
        return self.RECOMMENDED_GEAR

    def calculate_difficulty_level(self):
        for difficulty in self.PEAK_DIFFICULTY:
            if self.elevation >= self.PEAK_DIFFICULTY[difficulty]["min"]:
                return difficulty
            if self.PEAK_DIFFICULTY[difficulty]["min"] <= self.elevation <= self.PEAK_DIFFICULTY[difficulty]["max"]:
                return difficulty


# peak = ArcticPeak("everest", 2000)
# print(peak.calculate_difficulty_level())
# print(peak.difficulty_level)
# a=-2