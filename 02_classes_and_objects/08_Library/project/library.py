from project.user import User


class Library:
    def __init__(self):
        self.user_records = []  # Will store Users objects
        self.books_available = {}  # Will keep info for authors(key:str) and books(value:list:strings)
        self.rented_books = {}  # Will keep info for usernames(key:str) and nested dict -> books(key:str) : days left(value:int)

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if author in self.books_available:
            if book_name in self.books_available[author]:
                if book_name not in user.books:
                    user.books.append(book_name)
                    self.books_available[author].remove(book_name)
                    if user.username not in self.rented_books:
                        self.rented_books[user.username] = {book_name:days_to_return}
                        return f"{book_name} successfully rented for the next {days_to_return} days!"
                    doubled_key = False
                    for key in self.rented_books[user.username]:
                        if key == book_name:
                            doubled_key = True
                            break
                        if not doubled_key:
                            self.rented_books[user.username][book_name] = days_to_return
                            return f"{book_name} successfully rented for the next {days_to_return} days!"

            for user in self.rented_books:
                for book in self.rented_books[user]:
                    if book == book_name:
                        return f'The book "{book}" is already rented and will be available in {self.rented_books[user][book]} days!'

    def return_book(self, author:str, book_name:str, user: User):
        if book_name not in user.books:
            return f"{user.username} doesn't have this book in his/her records!"
        user.books.remove(book_name)
        self.books_available[author].append(book_name)
        self.rented_books[user.username].pop(book_name)

