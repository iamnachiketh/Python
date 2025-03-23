class User:
    user_count = 0
    def __init__(self, name, password):
        self.name = name
        self.password = password
        User.user_count += 1
    
    def print_details(self):
        print(f'Name: {self.name}, Password: {self.password} User count: {User.user_count}')

    @staticmethod
    def print_user_count():
        print(User.user_count)

user1 = User("John", 123456)
user2 = User("Jane", 654321)

user1.print_details() # Output: Name: John, Password: 123456 User count: 2

user2.print_details() # Output: Name: Jane, Password: 654321 User count: 2

# The user_count is a class variable, so it is shared among all instances of the class.
# When we increment the user_count in the __init__ method, it is incremented for all instances of the class.

User.print_user_count() # Output: 2