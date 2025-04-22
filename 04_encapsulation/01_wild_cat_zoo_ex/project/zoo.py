from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget < price:
            return "Not enough budget"
        if self.__animal_capacity <= 0:
            return "Not enough space for animal"
        self.__budget -= price
        self.animals.append(animal)
        self.__animal_capacity -= 1
        return f"{animal.name} the {type(animal).__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity <= 0:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {type(worker).__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = 0
        for worker in self.workers:
            total_salaries += worker.salary
        if total_salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_money_animals_care = 0
        for animal in self.animals:
            total_money_animals_care += animal.money_for_care
        if total_money_animals_care > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= total_money_animals_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animals_dict = {}
        for animal in self.animals:
            if type(animal).__name__ not in animals_dict:
                animals_dict[type(animal).__name__] = [1, [animal]]
            else:
                animals_dict[type(animal).__name__][0] += 1
                animals_dict[type(animal).__name__][1].append(animal)
        result = f"You have {len(self.animals)} animals"
        if len(self.animals) > 0:
            result += "\n"

        counter = 0
        animal_types = ["Lion", "Tiger", "Cheetah"]
        while len(animal_types) > 0:
            for key in animals_dict:
                if key == animal_types[0]:
                    result += f"----- {animals_dict[key][0]} {key}s:\n"
                    counter +=1
                    inner_counter = 0
                    for value in animals_dict[key][1]:
                        inner_counter += 1
                        if inner_counter == len(animals_dict[key][1]) and counter == len(animals_dict):
                            result += f"{str(value)}"
                        else:
                            result += f"{str(value)}\n"
            animal_types.pop(0)
        return result

    def workers_status(self):
        workers_dict = {}
        for worker in self.workers:
            if type(worker).__name__ not in workers_dict:
                workers_dict[type(worker).__name__] = [1, [worker]]
            else:
                workers_dict[type(worker).__name__][0] += 1
                workers_dict[type(worker).__name__][1].append(worker)
        result = f"You have {len(self.workers)} workers"
        if len(self.workers) > 0:
            result += "\n"

        counter = 0
        professions = ["Keeper", "Caretaker", "Vet"]
        while len(professions) > 0:
            for key in workers_dict:
                if key == professions[0]:
                    result += f"----- {workers_dict[key][0]} {key}s:\n"
                    counter += 1
                    inner_counter = 0
                    for value in workers_dict[key][1]:
                        inner_counter += 1
                        if inner_counter == len(workers_dict[key][1]) and counter == len(workers_dict):
                            result += f"{str(value)}"
                        else:
                            result += f"{str(value)}\n"
            professions.pop(0)
        return result

