# Print name dynamicaly
def print_message(name):
    if(len(name) < 3):
        print("Name should be min of 3 characters")
        return
    print(f"Hello {name}, How are you?")

name = input("Enter the username: ")
print_message(name)