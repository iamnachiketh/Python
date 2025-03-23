class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def say_hi_to_user(self, user):
        print(f"Hi {user.username}, I'm {self.username}")


user1 = User("Alex", "prometheus@google.com", 123456)


user2 = User("Bruce", "batman@wayen.us", 90865443)

user1.say_hi_to_user(user2)


user1.email = "alex@bbc.uk"

print(user1.email)
