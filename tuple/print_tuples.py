def print_tuples(tup):
    print("Tuple elements at index 2, 4, and 6:")
    print(f"Element at index 2: {tup[2]}")
    print(f"Element at index 4: {tup[4]}")
    print(f"Element at index 6: {tup[6]}")

    
tup = ()
print("Enter 10 numbers (0 to 9) to form a tuple of squares:")
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    tup += (num**2,)

print("\nFinal Tuple:", tup)
print_tuples(tup)

