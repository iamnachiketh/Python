# n = int(input("Enter the number: "))

# for i in range(2,n):
#     if(n%i == 0):
#         print("no")
#         exit(0) 

# print("Yes")

# n = int(input("Enter the number: "))
# res = 1
# for i in range(1,n+1):
#     res = res * i

# print(res)

# def factorial(n): 
#     res = 1
#     for i in range(1,n+1):
#         res = res * i
#     print(res)

# n = int(input("Enter the number: "))

# print(factorial(n))


# Print name dynamicaly
# def print_message(name):
#     if(len(name) < 3):
#         print("Name should be min of 3 characters")
#         return
#     print(f"Hello {name}, How are you?")

# name = input("Enter the username: ")
# print_message(name)


# Percentage of heads vs tails

# import random
# def probability_calculate(n, hcount, tcount):
#     for i in range(n):
#         num = random.random()
#         if num > 0.5 : tcount = tcount + 1
#         else: hcount = hcount + 1
#     return [hcount, tcount]

# n = int(input("Enter the Number of times to flip a coin: "))
# if(n < 0):
#     print("Enter the a positive number")
# else:
#     res = probability_calculate(n, 0, 0)
#     print(f"Percentage of heads: {(res[0]/n)*100}\n Percentage of tails: {(res[1]/n)*100}")


# Check Leap year
# def check_leapyear(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(f"{year} is a leap year.")
#     else:
#         print(f"{year} is not a leap year.")

# year = int(input("Enter a year: "))
# if 1000 <= year <= 9999: 
#     check_leapyear(year)
#     exit(0)
# print("Please entre the 4 digit year")


# Power of 2
def power_of_2(n):
    for i in range(n):
        print(2**i)

n = int(input("Enter the number: "))
if 0 <= n < 31: 
    power_of_2(n)
    exit(0)
print("Please enter the number between 0 and 30")






