# Power of 2
def power_of_2(n):
    for i in range(n):
        print(2**i)

n = int(input("Enter the number: "))
if 0 <= n < 31: 
    power_of_2(n)
    exit(0)
print("Please enter the number between 0 and 30")
