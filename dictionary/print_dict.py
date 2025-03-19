def print_details(fd):
    for i in fd.items():
        print(f"{i[0]}  -> {i[1]}")

friends_details = {

}

n = int(input("Enter the number of key-value pairs: "))

for i in range(n):
    key = input("Enter the keys: ")
    friends_details[key] = input("Enter the corresponding value: ")

print_details(friends_details)
