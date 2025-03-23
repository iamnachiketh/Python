class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_details(self):
        return f"{self.name} and dog age is {self.age}"



class Owner:
    def __init__(self, name, place, number, dog):
        self.name = name
        self.place = place
        self.dog = dog
        self.number = number

    def print_details(self):
        print(f"The owner name is {self.name} and owner place is {self.place} and owner's dog name is {self.dog.print_details()} and owner number is {self.number}")

# dog1 = Dog("Tommy", 3)

# owner = Owner("Alex", "NYC", 1234567890, dog1)

# owner.print_details()


class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

    def print_details(self):
        return f"The person name is {self.name} and person age is {self.age} and person city is {self.city} and person country is {self.country}"
    

person1 = Person("Thena", 30, "NYC", "USA")

print(person1.print_details())