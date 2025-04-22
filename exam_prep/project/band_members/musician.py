from abc import ABC, abstractmethod


class Musician(ABC):
    MINIMUM_MUSICIAN_AGE = 16
    AVAILABLE_TYPES_OF_SKILLS = []

    @abstractmethod
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Musician name cannot be empty!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < self.MINIMUM_MUSICIAN_AGE:
            raise ValueError(f"Musicians should be at least {self.MINIMUM_MUSICIAN_AGE} years old!")
        self.__age = value

    def learn_new_skill(self, new_skill: str):
        if new_skill not in self.AVAILABLE_TYPES_OF_SKILLS:
            raise ValueError(f"{new_skill} is not a needed skill!")
        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        self.skills.append(new_skill)
        return f"{self.name} learned to {new_skill}."