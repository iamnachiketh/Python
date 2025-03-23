a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("\nInitial Value of a & b are:")
print(f"a = {a}")
print(f"b = {b}")

temp = a
a = b
b = temp

print("\nAfter traditional swapping:")
print(f"a = {a}")
print(f"b = {b}")
