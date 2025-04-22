from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    INITIAL_STRENGTH = 200
    STRENGTH_NEEDED = 100
    DIFFICULTY_MULTIPLIER = {"Extreme":2, "Advanced": 1.5}
    STRENGTH_REDUCTION = 20
    def __init__(self, name):
        super().__init__(name, strength=self.INITIAL_STRENGTH)


    def can_climb(self):
        return True if self.strength >= self.STRENGTH_NEEDED else False

    def climb(self, peak:BasePeak):
        # if self.can_climb() and is_prepared():
        for difficulty in self.DIFFICULTY_MULTIPLIER:
            if peak.difficulty_level == difficulty:
                self.strength -= self.STRENGTH_REDUCTION * self.DIFFICULTY_MULTIPLIER[difficulty]
        self.conquered_peaks.append(peak)

