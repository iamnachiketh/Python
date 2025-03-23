# lis = []
# lis1 = [" ", 2.34, False]

# lis1[1] = 3.142

# print(lis1)

# lis.append(10)

# lis.insert(1, "hello")

# lis1.remove(0)

# lis1.pop()

number_list = [2, 4.67 ,1 ,9, 87.56]

# lis2.sort()

# print(lis)
# print(lis1)
# print(lis2)

# new_number_list = []

# for i in range(len(number_list)):
#     new_number_list.append(number_list.pop())

# print(new_number_list)


# def check_prime(num):
#     for i in range(2, num):
#         if(num%i == 0): return False
#     return True

# def prime_number(n):
#     prime_values = []
#     for i in range(2,n):
#         if(check_prime(i)):
#             prime_values.append(i)
#         else: continue
#     return prime_values

# n = int(input("Enter a number: "))

# print(prime_number(n))

# dict1 = {
#     "key": 10
# }

# print(dict1["key"])
# dict1["key"] = 20

# print(dict1["key"])

# print(dict1.items())

def store_value():
    squ_dict = {}
    for i in range(1,100):
        squ_dict[i] = i**2
    print(squ_dict.items())

store_value()




