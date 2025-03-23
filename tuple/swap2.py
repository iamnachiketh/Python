a = int(input("\nEnter the value of a: "))
b = int(input("Enter the value of b: "))

print("\nInitial Value of a & b are:")
print(f"a = {a}")
print(f"b = {b}")


a, b = b, a

print("\nAfter Pythonic swapping:")
print(f"a = {a}")
print(f"b = {b}")