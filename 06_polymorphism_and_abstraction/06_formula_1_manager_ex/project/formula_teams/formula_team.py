from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1000000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    @property
    @abstractmethod
    def expenses(self):
        pass

    @property
    @abstractmethod
    def sponsors_winnings(self):
        pass

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = -self.expenses
        for positions in self.sponsors_winnings.values():
            for position in positions:
                if race_pos <= position:
                    revenue += positions[position]
                    break
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"


