class Equipment:
    NEXT_ID = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Equipment.get_next_id()
        Equipment.NEXT_ID += 1

    @staticmethod
    def get_next_id():
        return Equipment.NEXT_ID

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"