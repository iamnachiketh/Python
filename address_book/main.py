from models.contact import Contact
from models.address_book import AddressBook
from utils.helpers import validate_input

def main():
    book = AddressBook()

    while True:
        print("\n1. Add Address Book")
        print("2. Add Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Search by City/State")
        print("6. Count by City/State")
        print("7. Sort by Name")
        print("8. Sort by City/State/Zip")
        print("9. Save to File")
        print("10. Load from File")
        print("11. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            book_name = input("Enter Address Book name: ")
            book.add_address_book(book_name)

        elif choice == "2":
            book_name = input("Enter Address Book name: ")
            
            if book_name not in book.books:
                print("Address book not found!")
                continue
            
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            address = input("Address: ")
            city = input("City: ")
            state = input("State: ")
            zip_code = validate_input("Zip Code: ", r"^\d{5}$", "Invalid zip code!")
            phone = validate_input("Phone (10 digits): ", r"^\d{10}$", "Invalid phone number!")
            email = validate_input("Email: ", r'^[\w.-]+@[a-zA-Z\d.-]+\.[a-zA-Z]{2,}$', "Invalid email!")

            contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
            book.add_contact(book_name, contact)

        elif choice == "3":
            book_name = input("Enter Address Book name: ")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")

            print("\nEnter new details:")
            updated_contact = Contact(
                input("First Name: "),
                input("Last Name: "),
                input("Address: "),
                input("City: "),
                input("State: "),
                input("Zip Code: "),
                input("Phone: "),
                input("Email: ")
            )

            book.edit_contact(book_name, first_name, last_name, updated_contact)

        elif choice == "4":
            book_name = input("Enter Address Book name: ")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            book.delete_contact(book_name, first_name, last_name)

        elif choice == "9":
            book.write_to_file("data/address_book.txt")
            print("Data saved to file.")

        elif choice == "10":
            book.read_from_file("data/address_book.txt")
            print("Data loaded from file.")

        elif choice == "11":
            break

        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()
