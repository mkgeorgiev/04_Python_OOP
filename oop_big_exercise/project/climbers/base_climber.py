from abc import ABC, abstractmethod


class BaseClimber(ABC):
    MIN_STRENGTH = 0
    RESTORE_STRENGTH = 15.0
    def __init__(self,name: str, strength: float):
        self.name = name
        self.strength = strength
        self.conquered_peaks = []
        self.is_prepared = True


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Climber name cannot be null or empty!")
        self.__name = value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        if value <= self.MIN_STRENGTH:
            raise ValueError(f"A climber cannot have negative strength or strength equal to {self.MIN_STRENGTH}!")
        self.__strength = value

    @abstractmethod
    def can_climb(self):
        pass

    @abstractmethod
    def climb(self, peak):
        pass

    def rest(self):
        self.strength += self.RESTORE_STRENGTH

    def __str__(self):
        return f"{self.__class__.__name__}: /// Climber name: {self.name} * Left strength: {self.strength:.1f}" \
               f" * Conquered peaks: {', '. join(peak.name for peak in self.conquered_peaks)} ///"
