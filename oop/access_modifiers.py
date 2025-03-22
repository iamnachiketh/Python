class Person:
    def __init__(self, name, age, pno):
        self.name = name
        self.age = age
        self._pno = pno # protected attribute

    def get_pno(self):
        return self._pno  
    

person1 = Person("Alex", 25, 1234567890)

person1._pno = 45678934567 # This is allowed but not recommended since it's a protected attribute

print(person1.get_pno()) # 1234567890


class Student:
    def __init__(self, sno, name, city):
        self.__sno = sno # private attribute
        self.name = name
        self.city = city

    def get_sno(self):
        return self.__sno
    
    def set_sno(self, sno):
        self.__sno = sno


student1 = Student(1, "Alex", "NYC")

# print(student1.__sno) # AttributeError: 'Student' object has no attribute '__sno'

print(student1.get_sno()) # 1


