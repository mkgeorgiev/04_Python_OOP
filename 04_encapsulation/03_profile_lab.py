class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @username.setter
    def username(self, user_name):
        if not 4 < len(user_name) < 16 or type(user_name) != str:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = user_name

    @password.setter
    def password(self, pass_word):
        is_capital = False
        is_number = False
        for ch in pass_word:
            if ch.isdigit():
                is_number = True
            if ch.isupper():
                is_capital = True
        if not len(pass_word) >= 8 or not is_capital or not is_number:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = pass_word


    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'