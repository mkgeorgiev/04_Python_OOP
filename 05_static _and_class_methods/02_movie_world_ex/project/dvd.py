class DVD:
    MONTH_NAMES = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }

    def __init__(self, name:str, id:int, creation_year:int, creation_month:str, age_restriction:int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @property
    def creation_month(self):
        return self.__creation_month

    @creation_month.setter
    def creation_month(self, value):
        if value in DVD.MONTH_NAMES:
            self.__creation_month = DVD.MONTH_NAMES[value]
        else:
            self.__creation_month = value

    @classmethod
    def from_date(cls, id:int, name:str, date:str, age_restriction:int):
        return cls(name, id, int(date.split(".")[-1]),date.split(".")[1], age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction " \
               f"{self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"



