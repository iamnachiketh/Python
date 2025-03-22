class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        self.__password = value


user1 = User('John', 123456)

print(user1.password) # if we create a property, we dont have to write getters ans setters anymore
