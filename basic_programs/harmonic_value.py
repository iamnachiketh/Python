# Print the Nth harmonic value
def harmonic_value(n):
    res = 1
    for i in range(2,n+1):
        res = res + (1/i)
    return res

try: 
    n = int(input("Enter the number: "))
    if(n == 0):
        print("Please enter the non zero number")
    else: 
        print(harmonic_value(n))
except:
    print("Please enter a valid number")
