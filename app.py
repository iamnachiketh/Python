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

def factorial(n): 
    res = 1
    for i in range(1,n+1):
        res = res * i
    print(res)

n = int(input("Enter the number: "))

print(factorial(n))
