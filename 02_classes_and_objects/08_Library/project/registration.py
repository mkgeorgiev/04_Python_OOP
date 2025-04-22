from project.user import User
from project.library import Library


class Registration:

    def add_user(self, user: User, library: Library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)

    def remove_user(self, user: User, library: Library):
        if user not in library.user_records:
            return f"We could not find such user to remove!"
        library.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str, library: Library):
        counter = 0
        for user in library.user_records:
            if user.user_id == user_id:
                if new_username == user.username:
                    return "Please check again the provided username - " \
                           "it should be different than the username used so far!"
                if user.username in library.rented_books:
                    library.rented_books[new_username] = library.rented_books.pop(user.username)
                library.user_records[counter].username = new_username
                return f"Username successfully changed to: {new_username} for user id: {user_id}"
            counter+=1
        return f"There is no user with id = {user_id}!"


# user = User(12, 'Valentina')
# library = Library()
# register = Registration()
# library.books_available.update({'J.K.Rowling': ['Harry Potter and the Philosopher\'s Stone',
#                                                              'Harry Potter and the Philosopher\'s Stone',
#                                                              'Harry Potter and the Deathly Hallows',
#                                                              'Harry Potter and the Order of the Phoenix']})
# library.get_book('J.K.Rowling', 'Harry Potter and the Deathly Hallows', 17,user)