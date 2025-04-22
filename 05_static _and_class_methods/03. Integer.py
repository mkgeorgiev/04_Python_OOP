

class Integer:
    def __init__(self, value: int):
        self.value = value

    @staticmethod
    def roman_to_int(s):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0

        for numeral in reversed(s):
            value = roman_numerals[numeral]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value

        return result

    @classmethod
    def from_float(cls, float_value):
        if not type(float_value) == float:
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        if isinstance(value,str):
            return cls(cls.roman_to_int(value))

    @classmethod
    def from_string(cls,value):
        if type(value) == str:
            try:
                return cls(int(value))
            except ValueError:
                return "wrong type"
        return "wrong type"

    def __str__(self):
        return str(self.value)


number = Integer.from_float(5.2)
print(Integer.from_float(5.2))
print(number)
second_num = Integer.from_roman("IV")
print(second_num.value)




