class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.mails = mails
        self.min_length = min_length
        self.domains = domains

    def __is_name_valid(self, name):
        return True if len(name)>= self.min_length else False

    def __is_mail_valid(self,mail):
        return True if mail in self.mails else False

    def __is_domain_valid(self, domain):
        return True if domain in self.domains else False

    def validate(self, email):
        username, mail, domain = email.split("@")[0], email.split("@")[1].split(".")[0], email.split("@")[1].split(".")[1]
        return self.__is_name_valid(username) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain)