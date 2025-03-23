import re

class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    @staticmethod
    def validate_email(email):
        pattern = r'^[\w.-]+@[a-zA-Z\d.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    @staticmethod
    def validate_phone(phone):
        pattern = r'^\d{10}$'
        return re.match(pattern, phone) is not None

    def __eq__(self, other):
        return self.first_name.lower() == other.first_name.lower() and self.last_name.lower() == other.last_name.lower()

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.phone}, {self.email}"
