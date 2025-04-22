from project.band_members.musician import Musician

class Guitarist(Musician):
    AVAILABLE_TYPES_OF_SKILLS = ["play rock", "play metal", "play jazz"]

    def __init__(self, name, age):
        super().__init__(name,age,)
        self.skills = []

    def learn_new_skill(self, new_skill: str):
        return super().learn_new_skill(new_skill)


