from collections import defaultdict
from models.contact import Contact

class AddressBook:
    def __init__(self):
        self.books = defaultdict(list)

    def add_address_book(self, name):
        if name not in self.books:
            self.books[name] = []
        else:
            print(f"Address book '{name}' already exists!")

    def add_contact(self, book_name, contact):
        if contact not in self.books[book_name]:
            self.books[book_name].append(contact)
            print(f"Added {contact.first_name} to {book_name}.")
        else:
            print(f"Duplicate entry for {contact.first_name} in {book_name}.")

    def edit_contact(self, book_name, first_name, last_name, updated_contact):
        contacts = self.books[book_name]
        for i, contact in enumerate(contacts):
            if contact.first_name == first_name and contact.last_name == last_name:
                self.books[book_name][i] = updated_contact
                print(f"Updated {first_name} in {book_name}.")
                return
        print("Contact not found!")

    def delete_contact(self, book_name, first_name, last_name):
        contacts = self.books[book_name]
        self.books[book_name] = [c for c in contacts if c.first_name != first_name or c.last_name != last_name]

    def search_by_city_state(self, city=None, state=None):
        results = []
        for book in self.books.values():
            for contact in book:
                if (city and contact.city.lower() == city.lower()) or (state and contact.state.lower() == state.lower()):
                    results.append(contact)
        return results

    def count_by_city_state(self):
        city_count = defaultdict(int)
        state_count = defaultdict(int)

        for book in self.books.values():
            for contact in book:
                city_count[contact.city] += 1
                state_count[contact.state] += 1

        return city_count, state_count

    def sort_by_name(self, book_name):
        self.books[book_name].sort(key=lambda c: (c.first_name, c.last_name))

    def sort_by_city(self, book_name):
        self.books[book_name].sort(key=lambda c: c.city)

    def sort_by_state(self, book_name):
        self.books[book_name].sort(key=lambda c: c.state)

    def sort_by_zip(self, book_name):
        self.books[book_name].sort(key=lambda c: c.zip_code)

    def write_to_file(self, file_path):
        with open(file_path, "w") as file:
            for book_name, contacts in self.books.items():
                file.write(f"Address Book: {book_name}\n")
                for contact in contacts:
                    file.write(str(contact) + "\n")

    def read_from_file(self, file_path):
        with open(file_path, "r") as file:
            book_name = None
            for line in file:
                if line.startswith("Address Book:"):
                    book_name = line.split(":")[1].strip()
                    self.books[book_name] = []
                else:
                    fields = line.strip().split(", ")
                    contact = Contact(*fields)
                    self.books[book_name].append(contact)
