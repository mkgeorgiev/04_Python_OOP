from project.band_members.musician import Musician

class Drummer(Musician):
    AVAILABLE_TYPES_OF_SKILLS = ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]
    def __init__(self, name, age):
        super().__init__(name,age,)
        self.skills = []
    # @property
    # def skills (self):
    #     return self.__skills
    # 
    # @skills .setter
    # def skills (self, value):
        
    def learn_new_skill(self, new_skill: str):
        return super().learn_new_skill(new_skill)

# drummer = Drummer("barabanist", 20)
# print(drummer.learn_new_skill("read sheet music"))
