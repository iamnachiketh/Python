n = int(input("Enter the number: "))
res = 1
for i in range(1,n+1):
    res = res * i

print(res)



def factorial(n): 
    res = 1
    for i in range(1,n+1):
        res = res * i
    print(res)

n = int(input("Enter the number: "))

print(factorial(n))
