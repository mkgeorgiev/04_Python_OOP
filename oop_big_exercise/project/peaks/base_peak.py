from abc import ABC, abstractmethod


class BasePeak(ABC):
    MINIMUM_NAME_CHARS = 2
    MINIMUM_ELEVATION = 1500
    IS_PEAK_CONQUERED = False


    def __init__(self, name: str, elevation: int):
        self.name = name
        self.elevation = elevation
        self.difficulty_level = self.calculate_difficulty_level()
        self.is_conquered = self.IS_PEAK_CONQUERED

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < self.MINIMUM_NAME_CHARS or not value.strip():
            raise ValueError(f"Peak name cannot be less than {self.MINIMUM_NAME_CHARS} symbols!")
        self.__name = value

    @property
    def elevation(self):
        return self.__elevation

    @elevation.setter
    def elevation(self, value):
        if value < self.MINIMUM_ELEVATION:
            raise ValueError(f"Peak elevation cannot be below {self.MINIMUM_ELEVATION}m.")
        self.__elevation = value

    @abstractmethod
    def get_recommended_gear(self):
        pass

    @abstractmethod
    def calculate_difficulty_level(self):
        pass

